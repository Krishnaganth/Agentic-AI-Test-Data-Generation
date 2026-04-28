from utils.llm_client import call_llm


def extract_requirement(requirement):
    prompt = f"""
    Extract:
    - feature name
    - fields

    Requirement:
    {requirement}

    Return JSON only.
    """
    return call_llm(prompt)


class RequirementAgent:
    """Generates high-level requirements for the test data generator."""

    def __init__(self, llm_client):
        self.llm = llm_client

    def generate_requirements(self):
        # Placeholder implementation. Replace with calls to an LLM in the future.
        requirements = [
            "Generate diverse test records covering edge cases",
            "Preserve realistic value distributions",
        ]

        # Demonstrate using extract_requirement to convert free-text
        parsed = []
        for r in requirements:
            parsed.append(extract_requirement(r))

        return parsed
