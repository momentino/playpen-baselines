from agents.llm_agent import LlmAgent

from playpen import playpengame
from playpen.playpengame.playpengame import num_players
from playpen.agents import Agent
from playpen.utils.run_utils import read_gen_args

from typing import List
import argparse

stdout_logger = playpengame.get_logger("benchmark.run")

def create_agents(args: argparse.Namespace) -> List[Agent]:
    min_num_agents, max_num_agents = num_players(args.game)
    agents = [LlmAgent(m, m, read_gen_args(args)) for m in args.models]
    if len(agents) > max_num_agents:
        message = f"Too many agents for this game. The maximum number of player agents for this game is {max_num_agents}"
        stdout_logger.error(message)
        raise ValueError(message)
    elif len(agents) < min_num_agents:
        message = f"The number of agents was insufficient for playing the game. Creating {min_num_agents - len(agents)} agents with the last model specified in the arguments."
        stdout_logger.warning(message)
        m = args.models[-1]
        agents.extend([LlmAgent(m, m, read_gen_args(args)) for _ in range(min_num_agents - len(agents))])
    return agents
