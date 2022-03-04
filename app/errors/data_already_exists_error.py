from werkzeug.exceptions import HTTPException

class DataAlreadyExistsError(HTTPException):
    description = {"error_message": "key value already registered"} 
   