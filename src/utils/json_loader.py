import os
import json


def read_json(file_path):
    abs_file_path = os.path.abspath(file_path)
    with open(abs_file_path) as f:
        return json.load(f)
