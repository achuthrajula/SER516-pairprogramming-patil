from typing import List

from guet.commands import CommandMap
from guet.steps.action import Action


class UsageAction(Action):
    def __init__(self, command_map: CommandMap):
        super().__init__()
        self.command_map = command_map

    def execute(self, args: List[str]):
        pass
       
