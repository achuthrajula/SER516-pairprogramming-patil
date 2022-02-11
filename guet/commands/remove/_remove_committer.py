from typing import List
from plyer import notification

from guet.steps.action import Action


class RemoveCommitterAction(Action):
    def __init__(self, committers):
        super().__init__()
        self.committers = committers

    def execute(self, args: List[str]):
        committer = self.committers.by_initials(args[0])
        if not committer:
            notification.notify(title="Guet",
                                message=f"Remove: No committer exists with initials {args[0]}",
                                app_icon='',
                                timeout=10,
                                toast=True)
        else:
            self.committers.remove(committer.initials)
