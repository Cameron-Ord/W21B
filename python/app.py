#importing
import json
from flask import Flask,request
import dbhelper
import api_helper
app = Flask(__name__)

#making a post request to insert a philosopher

@app.post('/api/input_philosopher')
#function gets called on api request

def input_philosopher():
   try:
      #calls the function in api_helper to loop through the informatin sent
      error=api_helper.check_endpoint_info(request.json, ['name', 'bio','dob', 'dod','image_url']) 
      if(error !=None):
         return "something went wrong"
      #calls the proceedure to insert sent information into the DB
      results = dbhelper.run_proceedure('CALL insert_philosopher(?,?,?,?,?)', [request.json.get('name'), request.json.get('bio'), request.json.get('dob'), request.json.get('dod'), request.json.get('image_url'),])
      #returns results from db run_proceedure
      return json.dumps(results, default=str)
   #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')
@app.post('/api/input_quote')
def input_quote():
   try:
      #calls the function in api_helper to loop through the informatin sent
      error=api_helper.check_endpoint_info(request.json, ['philosopher_id', 'content']) 
      if(error !=None):
         return "something went wrong"
      #calls the proceedure to insert sent information into the DB
      results = dbhelper.run_proceedure('CALL insert_quote(?,?)', [request.json.get('philosopher_id'), request.json.get('content')])
      #returns results from db run_proceedure
      return json.dumps(results, default=str)
   #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')
      
#runs function on get request
@app.get('/api/return_all')
def return_all():
   try:
      #calling run proceedure to communicate with the DB, takes no arguments
      results = dbhelper.run_proceedure('CALL return_all()', [])
      #if a list is returened, returns the results
      if(type(results) == list):
         return json.dumps(results, default=str)
      else:
         return "something went wrong"
   #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')

#runs function on get request
@app.get('/api/return_specific_philosopher')
def get_philo():
   try:
      #calling run proceedure to communicate with the DB, takes 1 argument
      philo_id = request.args.get('philo_id')
      results = dbhelper.run_proceedure('CALL return_spec_p(?)', [philo_id])
      #if a list is returened, returns the results
      if(type(results) == list):
         return json.dumps(results, default=str)
      else:
         return "something has gone wrong."
   #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')   
#running @app
app.run(debug=True)
