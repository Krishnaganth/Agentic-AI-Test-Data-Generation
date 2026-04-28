from utils.llm_client import call_llm


def validate_data(data):
    prompt = f"""
    Validate this test data and correct classification if needed:

    {data}

    Return corrected JSON.
    """
    return call_llm(prompt)


class ValidationAgent:
    """Validates generated data against constraints."""

    def __init__(self, llm_client):
        self.llm = llm_client

    def validate(self, dataset, constraints):
        # Simple deterministic checks
        issues = []
        age_min, age_max = constraints.get("age_range", [0, 120])
        for row in dataset:
            age = row.get("age")
            if age is None:
                issues.append({"row": row, "issue": "missing age"})
            elif not (age_min <= age <= age_max):
                issues.append({"row": row, "issue": f"age {age} out of range"})

        # Ask LLM to validate/correct classification where helpful
        llm_feedback = validate_data({"dataset": dataset, "constraints": constraints})

        return {"valid": len(issues) == 0, "issues": issues, "llm_feedback": llm_feedback}
