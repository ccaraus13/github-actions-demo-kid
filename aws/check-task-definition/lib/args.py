import argparse


class Args:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Dummy executor", exit_on_error=True)
        parser.add_argument("--task-definition", required=True, help="Task Definition json file")
        parser.add_argument("--app-config", required=False, help="Application properties yaml files")

        args = parser.parse_args()

        self.task_definition = args.task_definition
        self.app_config = args.app_config

    def __str__(self) -> str:
        return f"""  "task_definition": "{self.task_definition},",
                    "app_config": "{self.app_config}" 
                    """

