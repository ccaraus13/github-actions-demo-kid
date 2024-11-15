from unittest.mock import patch
import sys
from lib.args import Args


def test_args_empty_optional():
    testargs = ["check_task_dev.py",
                "--task-definition", "./test_data/task_definition.json",
                "--app-config", "./test_data/application-1.yaml"
                ]
    with patch.object(sys, 'argv', testargs):
        args = Args()
        assert args.task_definition == "./test_data/task_definition.json"
        assert args.app_config == "./test_data/application-1.yaml"


def test_dummy():
    print("dummy test")
