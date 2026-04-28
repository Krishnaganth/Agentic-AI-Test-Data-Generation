from utils.llm_client import call_llm


def generate_test_data(context):
    prompt = f"""
    Generate test data:
    - valid
    - invalid
    - boundary
    - edge

    Input:
    {context}

    Return JSON array.
    """
    return call_llm(prompt)


class DataAgent:
    """Generates datasets for given scenarios."""

    def __init__(self, llm_client):
        self.llm = llm_client

    def generate_data(self, scenarios):
        # Return a tiny sample dataset for each scenario
        rows = []
        for s in scenarios if isinstance(scenarios, list) else []:
            if s.get("id") == 1:
                rows.extend([
                    {"id": 1, "name": "Alice", "age": 30, "email": "alice@example.com"},
                    {"id": 2, "name": "Bob", "age": 45, "email": "bob@example.com"},
                ])
            elif s.get("id") == 2:
                rows.extend([
                    {"id": 3, "name": "Baby", "age": 0, "email": "baby@example.com"},
                    {"id": 4, "name": "Old", "age": 120, "email": "old@example.com"},
                ])

        # Ask the LLM to generate additional test cases based on scenarios
        context = {"scenarios": scenarios, "baseline_rows": rows}
        llm_generated = generate_test_data(context)

        return {"baseline": rows, "llm_generated": llm_generated}
