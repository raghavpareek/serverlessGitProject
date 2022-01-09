import json
import urllib3 
import os
from datetime import datetime
def helloWorld(event, context):
     return {
         'statusCode' : 200,
         'body' : json.dumps("Hello Bewgle")
     }
