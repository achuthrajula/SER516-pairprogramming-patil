from typing import List

from guet.committers import Committers2 as Committers
from guet.committers.committer import Committer
from guet.steps.action import Action
from guet.util import Args


class AddCommitter(Action):

    def __init__(self, committers: Committers):
        super().__init__()
        self.committers = committers

    def execute(self, args: List[str]):
        if len(args)%3==0:
            flag=len(args)/3
            count = 0
            while(flag!=0):
                temp_args = args[count:count+3]
                initials, name, email = Args(temp_args).without_flags
                self.committers.add(Committer(name, email, initials))
                print(f'Committer {name} added.')
                flag -= 1
                count +=3
        else:
            print('Insufficient details for adding the committer')
