import PySimpleGUI as sg
from pickle import NONE
from typing import List
from plyer import notification

from guet.committers import Committers2 as Committers
from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action


class GetCommittersAction(Action):

    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current = current_committers

    def execute(self, args: List[str]):
        if args[0] == 'all':
            committers = self.committers.all()
            pre_print = 'All committers'
            if committers == []:
                notification.notify(title="Guet",
                                    message="get: No committers",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)
            else:
                notification.notify(title="Guet",
                                    message=f"get: {pre_print} {committers}",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)
        elif args[0] == 'current':
            committers = self.current.get()
            pre_print = 'Current committers'
            committers = list(filter(None, committers))
            if committers == []:
                notification.notify(title="Guet",
                                    message="get: No active committers",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)
            else:
                notification.notify(title="Guet",
                                    message=f"guet: {pre_print} {committers}",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)
        elif args[0] == 'pair-log':
            file_name = "logfile.log"
            file = open(file_name, "r")
            data = []
            order = ["date", "message", "committers"]

            for line in file.readlines():
                details = line.split("|")
                details = [x.strip() for x in details]
                structure = {key:value for key, value in zip(order, details)}
                data.append(structure)

            for log in data:
                print(f"{log['message']} by {log['committers']} at {log['date']}")