from agents.requirement_agent import RequirementAgent, extract_requirement
from agents.constraint_agent import ConstraintAgent, extract_constraints
from agents.scenario_agent import ScenarioAgent, classify_scenarios
from agents.data_agent import DataAgent, generate_test_data
from agents.validation_agent import ValidationAgent, validate_data


class Orchestrator:
    """Simple orchestrator that runs agents in sequence and returns a combined result."""

    def __init__(self, llm_client, formatter):
        self.llm = llm_client
        self.formatter = formatter
        self.requirement_agent = RequirementAgent(self.llm)
        self.constraint_agent = ConstraintAgent(self.llm)
        self.scenario_agent = ScenarioAgent(self.llm)
        self.data_agent = DataAgent(self.llm)
        self.validation_agent = ValidationAgent(self.llm)

    def run(self):
        requirements = self.requirement_agent.generate_requirements()
        constraints = self.constraint_agent.generate_constraints(requirements)
        scenarios = self.scenario_agent.generate_scenarios(requirements, constraints)
        dataset = self.data_agent.generate_data(scenarios)
        validation = self.validation_agent.validate(dataset, constraints)

        return {
            "requirements": requirements,
            "constraints": constraints,
            "scenarios": scenarios,
            "dataset": dataset,
            "validation": validation,
        }


def run_pipeline(requirement):

    req = extract_requirement(requirement)

    constraints = extract_constraints(requirement)

    combined = f"""
    Requirement: {req}
    Constraints: {constraints}
    """

    scenarios = classify_scenarios(combined)

    full_context = f"""
    {combined}
    Scenarios: {scenarios}
    """

    data = generate_test_data(full_context)

    validated = validate_data(data)

    return {
        "requirement": req,
        "constraints": constraints,
        "scenarios": scenarios,
        "data": validated,
    }
