from flask import Flask
from flask_restful import Api
from api.apiTasks import apiTasks
import logging as logger

logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)
restServer = Api(flaskAppInstance)


restServer.add_resource(apiTasks, "/api/v1.0/apiTasks/<string:name>")

if __name__ == '__main__':
    logger.info("Starting the app")

    flaskAppInstance.run(
        host='localhost',
        port=8000,
        debug=True,
        use_reloader=True
    )
