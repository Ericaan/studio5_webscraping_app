import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
import datetime

cred_object = credentials.Certificate("./pythonfirebase-c03ae-firebase-adminsdk-6gimp-6133025366.json")
default_app = firebase_admin.initialize_app(cred_object)
db = firestore.client()
fb = firebase.FirebaseApplication('https://pythonfirebase-c03ae-default-rtdb.firebaseio.com/', None)


# create a new project
def create_project(pname, my_url):
    today = datetime.datetime.now()
    # convert today as string instead of timestamp
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    doc = db.collection('Project').document()
    doc.set(
        {
            'projectId': doc.id,
            'projectName': pname,
            'URL': my_url,
            'lastDate': date_time,
            'dataDownload': 'false',
            'userInput': None
        }
    )


# Read the project based on the name
# returns project id
def read_project(pname):
    docs = db.collection('Project').where('projectName', "==", pname).stream()
    for doc in docs:
        return doc.id


# return all the projects
def read_all_projects():
    docs = db.collection('Project').stream()
    dict = []
    for doc in docs:
        dict.append(doc("URL").to_dict())
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

def read_specific_fields():
	docs = db.collection('Project').stream()
	data = []
	for doc in docs:
		projectId = doc.get('projectId')
		projectName = doc.get('projectName')
		url = doc.get('URL')
		dataDownload = doc.get('dataDownload')
		lastDate = doc.get('lastDate')
		data.append(projectId)
		data.append(projectName)
		data.append(url)
		data.append(dataDownload)
		data.append(lastDate)
	#assign keys
	keys = ["Project ID", "Project Name", "URL", "Data Download", "Last Date"]
	# new_list = np.array_split(data, 3)
	# print((new_list))
	def list_split(list, n):
		for x in range(0, len(list), n):
			split = list[x: n + x]
			# yield = used to convert function into generator
			# return = used to return the result to the caller statement
			yield split
	# 5 values
	new_list =list(list_split(data, 5))

	with open('project_details.csv', 'w') as f:
		write = csv.writer(f)
		write.writerow(keys)
		write.writerows(new_list)

# UPDATE the project
def update_project(id, pname, my_url, user_input):
    today = datetime.datetime.now()
    db.collection('Project').document(id).update(
        {
            'projectName': pname,
            'URL': my_url,
            'lastDate': today.strftime("%m/%d/%Y, %H:%M:%S"),
            'dataDownload': 'false',
            'userInput': user_input
        }
    )


# DELETE the project
def delete_project(id):
    db.collection('Project').document(id).delete()
