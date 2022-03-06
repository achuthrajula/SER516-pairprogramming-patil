from .action import Action

class PrintAction(Action):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def execute(self, _):
        print("init: guet successfully started in this repository.")
