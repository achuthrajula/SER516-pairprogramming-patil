from typing import List
from plyer import notification

from guet.steps.action import Action
from guet.committers import CommittersPrinter


class RemoveCommitterAction(Action):
    def __init__(self, committers):
        super().__init__()
        self.committers = committers

    def execute(self, args: List[str]):
        committer = self.committers.by_initials(args[0])
        found = [c for c in self.committers.all() if c.initials == args[0].lower()]

        if not committer:
            notification.notify(title="Guet",
                                message=f"Remove: No committer exists with initials {args[0]}",
                                app_icon='',
                                timeout=10,
                                toast=True)
        else:
            print('Removed committer')
            Printer = CommittersPrinter(initials_only = False)
            self.committers.remove(committer.initials)
            Printer.print(found)
