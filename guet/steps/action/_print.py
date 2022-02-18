from .action import Action
from plyer import notification


class PrintAction(Action):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def execute(self, _):
        notification.notify(title="Guet",
                            message="init: guet successfully started in this repository.",
                            app_icon='',
                            timeout=10,
                            toast=True)
