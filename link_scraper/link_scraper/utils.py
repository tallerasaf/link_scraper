import json
from typing import Dict

DEFAULT_INDENT = 2


def get_pretty_json(some_dict: Dict) -> str:
    return json.dumps(some_dict, indent=DEFAULT_INDENT, sort_keys=True)
