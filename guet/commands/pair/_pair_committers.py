from typing import List
from plyer import notification

from guet.committers import Committers2 as Committers
from guet.committers import CurrentCommitters
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
        if args[0] == 'clear-log':
            file = open("logfile.log","r+")
            file.truncate(0)
            file.close()
        else:
            pairing_strategy  = args[0].lower()
            if pairing_strategy in ["do","sj"]:
                committer_initials = [arg.lower() for arg in args[1:3]]
                found = [committer for committer in self.committers.all(
                ) if committer.initials in committer_initials]

                if pairing_strategy == "do":
                    final_strategy = strategies['do']
                else:
                    final_strategy = strategies['sj']
                
                for i in range(0,2):
                    self.committers.remove(found[i].initials)
                    for j in ["Driver",'Observer','Senior','Junior']:
                        if j in found[i].name:
                            found[i].name = found[i].name.replace(f"({j})","")
                    found[0].name = f"{found[0].name}({final_strategy[1]})"
                    found[1].name = f"{found[1].name}({final_strategy[0]})"
                    self.committers.add(found[i])
                self.current_committers.set(found)    
                notification.notify(title="Guet",
                                    message=f"Current pairing strategy is {final_strategy[0]} and {final_strategy[1]}\n {found[0].name} \n {found[1].name}",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)

            else:
                notification.notify(title="Guet",
                                    message="Enter a valid pairing strategy",
                                    app_icon='',
                                    timeout=10,
                                    toast=True)