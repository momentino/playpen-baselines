# Baselines for the Playpen Challenge
This repository is a space where baseline agents designed to integrate with the Playpen are implemented. 

**The following baselines are currently implemented:**
- **ZeroShotLLMAgent**: a simple LLM agent with no training logic. It is suitable for performing zero-shot inference on already existing LLMs.
# How to use
First of all, create your own conda environment  
`conda create --name playpen_baselines python=3.10.15`  

Then, install the requirements
`pip install -r requirements.txt`  
# How to run the baselines
## ZeroShotLLMAgent

To run a specific game with a single player (e.g. privateshared):  
  `$> python3 scripts/cli.py run -g privateshared -m model_name`  

To run a specific game with n players (e.g. taboo): _Be mindful, you cannot specify more models than the number allowed by the game_  
  `$> python3 scripts/cli.py run -g taboo -m model_name model_name2 model_name3 ...`  

If the game supports model expansion (using the single specified model for all players):  
  `$> python3 scripts/cli.py run -g taboo -m model_name`  
# How to list games
  `$> python3 scripts/cli.py ls
`  
