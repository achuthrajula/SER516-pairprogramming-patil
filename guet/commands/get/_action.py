import PySimpleGUI as sg
from pickle import NONE
from typing import List

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
                print('get: No committers')
            else:
                print(f"get: {pre_print} {committers}")
        elif args[0] == 'current':
            committers = self.current.get()
            pre_print = 'Current committers'
            committers = list(filter(None, committers))
            if committers == []:
                print("get: No active committers")
            else:
                print(f"guet: {pre_print} {committers}")
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