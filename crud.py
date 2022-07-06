
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
import datetime

cred_object = credentials.Certificate("./pythonfirebase-c03ae-firebase-adminsdk-6gimp-6133025366.json")
default_app = firebase_admin.initialize_app(cred_object)
db = firestore.client()
fb = firebase.FirebaseApplication('https://pythonfirebase-c03ae-default-rtdb.firebaseio.com/',None)

# create a new project
def create_project(pname,my_url,input1,input2):
	today = datetime.datetime.now()
	db.collection('Project').document().set(
		{
			'projectName':pname,
            'URL': my_url,
			'lastDate': today,
            'dataDownload':'false',
			'userInput': [input1,input2]
		}
	)

# Read the project based on the name
# returns project id
def read_project(pname):
    docs = db.collection('Project').where('projectName',"==",pname).stream()
    for doc in docs:
        return doc.id

# return all the projects
def read_all_projects():
    docs = db.collection('Project').stream()
    for doc in docs:
        print( doc.to_dict())

# UPDATE the project
def update_project(id,pname,my_url,input1,input2):
    today = datetime.datetime.now()
    db.collection('Project').document(id).update(
		{
			'projectName':pname,
            'URL': my_url,
			'lastDate': today,
            'dataDownload':'false',
			'userInput': [input1,input2]
		}
	)

# DELETE the project
def delete_project(id):
  db.collection('Project').document(id).delete()

