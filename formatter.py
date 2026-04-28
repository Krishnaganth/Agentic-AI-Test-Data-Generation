import json


class Formatter:
    """Small helper to pretty-print results from the orchestrator."""

    def format_result(self, result):
        return json.dumps(result, indent=2, ensure_ascii=False)
