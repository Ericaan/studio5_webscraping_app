
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
def create_project(pname,my_url):
	today = datetime.datetime.now()
	# convert today as string instead of timestamp
	date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
	doc = db.collection('Project').document()
	doc.set(
		{
			'projectId': doc.id,
			'projectName':pname,
			'URL': my_url,
			'lastDate': date_time,
			'dataDownload':'false',
			'userInput': None
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
	dict = []
	for doc in docs:
		dict.append(doc.to_dict())
	return dict

def read_project_url(id):
	docs = db.collection('Project').where('projectId', '==', id).stream()
	for doc in docs:
		url = doc.to_dict().get('URL')
	return url

def read_project_inputs(id):
	docs = db.collection('Project').where('projectId', '==', id).stream()
	for doc in docs:
		inputs = doc.to_dict().get('userInput')
	return inputs

def read_project_name(id):
	docs = db.collection('Project').where('projectId', '==', id).stream()
	for doc in docs:
		pname = doc.to_dict().get('projectName')
	return pname

# UPDATE the project
def update_project(id,pname,my_url,userInput):
    today = datetime.datetime.now()
    db.collection('Project').document(id).update(
		{
			'projectName':pname,
            'URL': my_url,
			'lastDate': today,
            'dataDownload':'false',
			'userInput': userInput
		}
	)

# DELETE the project
def delete_project(id):
  db.collection('Project').document(id).delete()

