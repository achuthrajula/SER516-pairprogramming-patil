from typing import List
from plyer import notification

from guet.committers import Committers2 as Committers
from guet.committers import CommittersPrinter, CurrentCommitters
from guet.steps.action import Action


class PairCommittersAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        strategies = {
            "do" : ["Driver","Observer"],
            "sj" : ["Senior", "Junior"],
        }
        pairing_strategy  = args[0].lower()
        if pairing_strategy in ["do","sj"]:
            committer_initials = [arg.lower() for arg in args[1:3]]
            found = [committer for committer in self.committers.all(
            ) if committer.initials in committer_initials]

            if pairing_strategy == "do":
                final_strategy = strategies['do']

            else:
                final_strategy = strategies['sj']
            self.current_committers.set(found)

            notification.notify(title="Guet",
                                message=f"Current pairing strategy is {final_strategy[0]} and {final_strategy[1]}\n {final_strategy[0]}:{found[1].name} \n {final_strategy[1]}:{found[0].name}",
                                app_icon='',
                                timeout=20,
                                toast=True)
            printer = CommittersPrinter(initials_only=False)

        else:
            notification.notify(title="Guet",
                                message="Enter a valid pairing strategy",
                                app_icon='',
                                timeout=10,
                                toast=True)