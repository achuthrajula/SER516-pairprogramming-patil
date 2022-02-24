from guet.commands import CommandFactory
from guet.files import FileSystem
from guet.steps import Step
from guet.steps.check import HelpCheck, VersionCheck
from guet.steps.preparation import InitializePreparation
from guet.util import HelpMessageBuilder
from guet.util import Args
from ._issues import GetIssues

_HELP_MESSAGE = HelpMessageBuilder('guet issues',
                                   'Fetch Issues from GitHub') \
    .build()


class IssuesCommandFactory(CommandFactory):
    def __init__(self,
                 file_system: FileSystem):

        self.file_system = file_system \


    def build(self) -> Step:
        return VersionCheck() \
            .next(HelpCheck(_HELP_MESSAGE, stop_on_no_args=True)) \
            .next(InitializePreparation(self.file_system)) \
            .next(GetIssues())
