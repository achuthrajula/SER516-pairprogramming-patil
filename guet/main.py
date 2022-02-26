import PySimpleGUI as sg
import shlex
import logging

from guet.commands import CommandMap
from guet.commands.add import AddCommandFactory
from guet.commands.get import GetCommandFactory
from guet.commands.help import HelpCommandFactory
from guet.commands.init import InitCommandFactory
from guet.commands.remove import RemoveCommandFactory
from guet.commands.set import SetCommittersCommand
from guet.commands.pair import PairCommittersCommand
from guet.commands.yeet import YeetCommandFactory
from guet.commands.team import GetTaigaFactory
from guet.commands.issues import IssuesCommandFactory
from guet.commands.coauthor import SetCoauthorFactory
from guet.committers import Committers2, CurrentCommitters
from guet.files import FileSystem
from guet.git import GitProxy
from guet.util import add_command_help_if_invalid_command_given
from guet.util.errors import log_on_error

menu_def = [['User Preferences', ['Select theme', sg.theme_list()]]]


@log_on_error
def main():
    file_system = FileSystem()
    committers = Committers2(file_system)
    git = GitProxy()
    current_committers = CurrentCommitters(file_system, committers)
    current_committers.register_observer(git)

    sg.theme('DarkTeal9')
    sg.set_options(element_padding=(0, 0))      
    layout = [[sg.Output(size=(60,20))],[sg.Text(

        "1. help \n"
        "2. init \n"
        "3. add \n"
        "4. get \n"
        "5. set \n"
        "6. remove \n"
        "7. taiga-teammates \n"
        "8. issues \n"
        "9. co-author \n"
        "10. pair \n"
        "11. yeet \n"
    )],
        [sg.Push(),sg.Input(),sg.Push()],
        [sg.Text(size=(40, 1), key='message')],
        [sg.Push(),sg.Button('Execute', bind_return_key=True),sg.Button('Start',key='button'),sg.Button('Quit'),sg.Push()],[sg.Menu(menu_def), ]]

    window = sg.Window('Guet', layout, finalize=True, resizable=True, grab_anywhere=True)

    while True:
        event, values = window.read()

        committers_list = current_committers.get()
        committers_list = list(filter(None, committers_list))
        initials_list = [i.initials for i in committers_list]
        current_initials = ''
        for i in initials_list:
                current_initials += f"{str(i)} "

        if event == 'button':
                event = window[event].GetText()
            
        command_map = CommandMap()

        command_map.add_command('help', HelpCommandFactory(
            command_map, file_system), 'Display guet usage')
        command_map.add_command(
            'co-author', SetCoauthorFactory(file_system), 'Sets co-author in the comment section of the task in Taiga')
        command_map.add_command('init', InitCommandFactory(
            GitProxy(), file_system), 'Start guet tracking in the current repository')
        command_map.add_command('add', AddCommandFactory(
            file_system, committers, git), 'Add committer for tracking')
        command_map.add_command('get', GetCommandFactory(
            file_system, committers, current_committers), 'List information about committers')
        command_map.add_command('set', SetCommittersCommand(
            file_system, committers, current_committers, git), 'Set committers for current repository')
        command_map.add_command('pair', PairCommittersCommand(
            file_system, committers, current_committers, git), 'Set pairing strategy')
        command_map.add_command('remove', RemoveCommandFactory(
            file_system, committers), 'Remove committer')
        command_map.add_command(
            'taiga-teammates', GetTaigaFactory(file_system), 'Get Taiga teammates')
        command_map.add_command('yeet',
                                YeetCommandFactory(file_system, git),
                                'Remove guet configurations')
        command_map.add_command('issues', 
                                IssuesCommandFactory(file_system),
                                'Fetch Issues from GitHub')
       

        args = add_command_help_if_invalid_command_given(
            shlex.split(values[0]))

        if event in sg.theme_list():
            args = event
        else:
            command = command_map.get_command(args[0]).build()
            command.play(args[1:])

        file_system.save_all()

        if event == "Start":
                
                Log_Format = "%(asctime)s  %(message)s"

                logging.basicConfig(filename = "logfile.log",
                        filemode = "w",
                        format = Log_Format, 
                        level = logging.ERROR)

                logger = logging.getLogger()
                logger.error(f"| Session started | {current_initials}")
                window['button'].update(text='Stop')

        if event == "Stop":

                Log_Format = "%(asctime)s %(message)s "

                logging.basicConfig(filename = "logfile.log",
                        filemode = "w",
                        format = Log_Format, 
                        level = logging.ERROR)

                logger = logging.getLogger()
                logger.error(f"| Session stopped | {current_initials}")
                window['button'].update(text='Start')

        if event in (sg.WIN_CLOSED, 'Quit'):
            print(event)
            break
