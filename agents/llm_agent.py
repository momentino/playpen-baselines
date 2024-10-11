from playpen.agents import Agent
from backends import read_model_spec, get_model_for

from typing import Dict, Any


class LlmAgent(Agent):
    def __init__(self, agent_name: str, model_name: str, gen_args: Dict[str, Any]):
        super().__init__(name=agent_name)

        model_spec = read_model_spec(model_name)
        self.model = get_model_for(model_spec)
        self.model.set_gen_args(**gen_args)

    def act(self):
        prompt, response, response_text = self.model.generate_response(self.observations)
        return prompt, response, response_text

    def observe(self, observation, reward, termination, truncation, info):
        self.observations.append(observation)

    def shutdown(self):
        pass
