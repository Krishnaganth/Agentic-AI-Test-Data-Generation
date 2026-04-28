from utils.llm_client import call_llm


def classify_scenarios(context):
    prompt = f"""
    Identify test scenarios:
    - positive
    - negative
    - boundary
    - edge
    - equivalence
    - null/empty
    - invalid format

    Input:
    {context}

    Return JSON.
    """
    return call_llm(prompt)


class ScenarioAgent:
    """Expands requirements+constraints into concrete scenarios to synthesize."""

    def __init__(self, llm_client):
        self.llm = llm_client

    def generate_scenarios(self, requirements, constraints):
        # Use baseline deterministic scenarios
        baseline = [
            {"id": 1, "description": "normal distribution of ages"},
            {"id": 2, "description": "edge ages: 0 and 120"},
        ]

        # Build a context string for the classifier
        context = {
            "requirements": requirements,
            "constraints": constraints,
        }

        classified = classify_scenarios(context)

        return {"baseline": baseline, "classified": classified}
