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
  `python3 scripts/cli.py run -g privateshared -m model_name`  

To run a specific game with n players (e.g. taboo): _Be mindful, you cannot specify more models than the number allowed by the game_  
  `python3 scripts/cli.py run -g taboo -m model_name model_name2 model_name3 ...`  

If the game supports model expansion (using the single specified model for all players):  
  `python3 scripts/cli.py run -g taboo -m model_name`  
# How to score games (e.g taboo)
  `python scripts/cli.py score -g taboo`
  If you want to score specific experiments (Please refer to the playpen repository for additional details, \link[here]{https://github.com/momentino/playpen}) 
  `python scripts/cli.py score -g taboo -e high_en`
# How to generate transcripts from the games (e.g. taboo)
  -e is optional (it has analogous effect as for the score command, generating transcripts only for a specific experiment)
  `python scripts/cli.py transcribe -g taboo -e high_en`
# How to list games
  `$> python3 scripts/cli.py ls
`  
