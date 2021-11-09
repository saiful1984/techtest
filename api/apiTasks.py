from flask_restful import Resource
import logging as logger


class apiTasks(Resource):
    '''
    Contains functions that define the HTTP methods
    '''
    def get(self, name):
        '''
        Performs the READ function for CRUD operation
        '''
        logger.info("Inside get method")
        return {"name": name}, 200

    def post(self):
        '''
        Performs the CREATE function for CRUD operation
        '''
        logger.info("Inside post method")
        return {"function": "Inside post method"},200

    def put(self):
        '''
        Performs the UPDATE function for CRUD operation
        '''
        logger.info("Inside put method")
        return {"function": "Inside put method"},200

    def delete(self):
        '''
        Performs the DELETE function for rest api
        '''
        logger.info("Inside delete method")
        return {"function": "Inside delete method"},200
