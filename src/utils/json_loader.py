import os
import json


def read_json(file_path):
    abs_file_path = os.path.abspath(file_path)
    with open(r"C:\Users\vinic\Desktop\GIT\exercise-automation-test\src\desired_caps\desired_caps.json") as f:
        return json.load(f)
