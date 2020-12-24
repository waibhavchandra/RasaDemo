action:
	nohup rasa run actions -vv &
bot:
	nohup rasa run -m pm_models -p 5005 --enable-api --cors "*" -vv &
bot-cli:
	rasa run -m pm_models -p 5005 --enable-api --cors "*" -vv
train:
	rasa train --data pm_data --out pm_models
