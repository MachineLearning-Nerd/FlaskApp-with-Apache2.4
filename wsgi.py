import sys, os, logging
logging.basicConfig(stream=sys.stderr) 

PROJECT_DIR = "D:/LEARNING/Blogs/Medium/Flask development using Apache Server/flaskapp"
virtual_env = "D:/LEARNING/Blogs/Medium/Flask development using Apache Server/flaskapp/.venv"
activate_this = os.path.join(virtual_env, 'Scripts', 'activate_this.py')
exec(open(activate_this).read(),dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from hello import app as application