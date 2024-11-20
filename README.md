# Ecommerce Backend

## Local Development Setup
### Create Virtual Enviroment 
'''bash
python -m venv .venv
'''

### Activate Virutal Enviroment(Bash)
'''bash
source .venv/Scripts/Activate
'''

### Install Dev Dependencies
'''bash
pip install -r requirements-dev.txt
'''



### Install Dependencies
'''bash
pip install -r requirements.txt
'''

### Format Code
'''bash
black . --config ./pyproject.toml

### Start Backend Server
'''bash
python -m flask --app main run
'''

### Migration
'''bash
python -m flask --app main db migrate -m "create user auth table"
'''