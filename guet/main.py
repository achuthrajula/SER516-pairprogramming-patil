import PySimpleGUI as sg

from guet.commands import CommandMap
from guet.commands.add import AddCommandFactory
from guet.commands.get import GetCommandFactory
from guet.commands.help import HelpCommandFactory, UnknownCommandFactory
from guet.commands.init import InitCommandFactory
from guet.commands.remove import RemoveCommandFactory
from guet.commands.set import SetCommittersCommand
from guet.commands.pair import PairCommittersCommand
from guet.commands.yeet import YeetCommandFactory
from guet.committers import Committers2, CurrentCommitters
from guet.files import FileSystem
from guet.git import GitProxy
from guet.util import add_command_help_if_invalid_command_given
from guet.util.errors import log_on_error

menu_def = [['User Preferences', ['Select theme',sg.theme_list()]]]

@log_on_error
def main():
    file_system = FileSystem()
    committers = Committers2(file_system)
    git = GitProxy()
    current_committers = CurrentCommitters(file_system, committers)
    current_committers.register_observer(git)

    sg.theme('DarkTeal9')
    sg.set_options(element_padding=(0, 0))      
    layout = [[sg.Text(
        "1. help \n"
        "2. init \n"
        "3. add \n"
        "4. get \n"
        "5. set \n"
        "6. pair \n"
        "7. remove \n"
        "8. yeet"
    )],
        [sg.Input()],
        [sg.Text(size=(40, 1), key='message')],
        [sg.Button('Execute', bind_return_key=True)], [sg.Button('Quit')],[sg.Menu(menu_def), ]]

    window = sg.Window('Guet', layout, finalize=True, resizable=True)

    while True:
        event, values = window.read()

        command_map = CommandMap()


        command_map.add_command('help', HelpCommandFactory(
            command_map, file_system), 'Display guet usage')
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
        command_map.add_command('yeet',
                                YeetCommandFactory(file_system, git),
                                'Remove guet configurations')
        command_map.set_default(UnknownCommandFactory(command_map))
        
        args = add_command_help_if_invalid_command_given(values[0].split())
        
        if event in sg.theme_list():
            args = event
        else:
            command = command_map.get_command(args[0]).build()
            command.play(args[1:])
        
        file_system.save_all()

        if event in (sg.WIN_CLOSED, 'Quit'):
            print(event)
            break
