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
        printer = CommittersPrinter(initials_only=False)
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
        else:
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
