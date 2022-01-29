# import flask framework
from flask import Flask

# logger to log and trace while the application is running
import logging as logger

# configure the logger
logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)


from application_apis import *
flaskAppInstance.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
