from typing import List

from guet.steps.action import Action
from guet.committers import CommittersPrinter


class RemoveCommitterAction(Action):
    def __init__(self, committers):
        super().__init__()
        self.committers = committers

    def execute(self, args: List[str]):
        for i in range(0, len(args)):
            committer = self.committers.by_initials(args[i])
            found = [c for c in self.committers.all() if c.initials ==
                     args[i].lower()]

            if not committer:
                print(f"Remove: No committer exists with initials {args[i]}")

            else:
                print('Removed committer')
                Printer = CommittersPrinter(initials_only=False)
                self.committers.remove(committer.initials)
                Printer.print(found)