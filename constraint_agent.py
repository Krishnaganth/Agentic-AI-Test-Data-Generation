from utils.llm_client import call_llm


def extract_constraints(requirement):
    prompt = f"""
    Extract validation rules and constraints.

    Requirement:
    {requirement}

    Return JSON only.
    """
    return call_llm(prompt)


class ConstraintAgent:
    """Produces constraints derived from requirements (e.g., data schemas, ranges)."""

    def __init__(self, llm_client):
        self.llm = llm_client

    def generate_constraints(self, requirements):
        # If requirements are raw strings or LLM responses, run extraction
        constraints = {
            "schema": {
                "id": "int",
                "name": "string",
                "age": "int",
                "email": "string",
            },
            "age_range": [0, 120],
        }

        # Demonstrate using the LLM to extract per-requirement constraints
        extracted = []
        for r in requirements:
            extracted.append(extract_constraints(r))

        # Return both the deterministic baseline and LLM-extracted results
        return {"baseline": constraints, "extracted": extracted}
