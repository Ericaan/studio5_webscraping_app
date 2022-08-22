import csv

import bcrypt
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
def create_project(userId, pname, my_url, my_url2):
    today = datetime.datetime.now()
    # convert today as string instead of timestamp
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    doc = db.collection('Project').document()
    doc.set(
        {
            'projectId': doc.id,
            'userId': userId,
            'projectName': pname,
            'URL': my_url,
            'URL2': my_url2,
            'lastDate': date_time,
            'dataDownload': 'false',
            # 'userInput': None
        }
    )


# Read the project based on the name
# returns project id
def read_project(pname):
    docs = db.collection('Project').where('projectName', "==", pname).stream()
    for doc in docs:
        return doc.id


def return_userid_by_pname(pname):
    docs = db.collection('Project').where('projectName', "==", pname).stream()
    for doc in docs:
        user_id = doc.to_dict().get('userId')
    return user_id


def read_project_url(pid):
    docs = db.collection('Project').where('projectId', '==', pid).stream()
    for doc in docs:
        url = doc.to_dict().get('URL')
    return url

def read_project_url2(pid):
    docs = db.collection('Project').where('projectId', '==', pid).stream()
    for doc in docs:
        url2 = doc.to_dict().get('URL2')
    return url2


def read_project_name(pid):
    docs = db.collection('Project').where('projectId', '==', pid).stream()
    for doc in docs:
        pname = doc.to_dict().get('projectName')
    return pname


def read_user_input(pid):
    docs = db.collection('Project').where('projectId', '==', pid).stream()
    data = {}
    for doc in docs:
        data = doc.to_dict().get('userInput')
    return data



def read_specific_fields(userId):
        docs = db.collection('Project').where('userId', '==', userId).stream()
        data = []
        # assign keys
        keys = ["Project ID", "Project Name", "URL", "URL2", "Data Download", "Last Date"]
        if docs == []:
            with open('project_details.csv', 'w') as f:
                write = csv.writer(f)
                write.writerow(keys)
        else:
            for doc in docs:
                projectId = doc.get('projectId')
                projectName = doc.get('projectName')
                url = doc.get('URL')
                url2 = doc.get('URL2')
                dataDownload = doc.get('dataDownload')
                lastDate = doc.get('lastDate')
                data.append(projectId)
                data.append(projectName)
                data.append(url)
                data.append(url2)
                data.append(dataDownload)
                data.append(lastDate)

            # new_list = np.array_split(data, 3)
            # print((new_list))
            def list_split(list, n):
                for x in range(0, len(list), n):
                    split = list[x: n + x]
                    # yield = used to convert function into generator
                    # return = used to return the result to the caller statement
                    yield split
            # 5 values
            new_list =list(list_split(data, 6))

            with open('project_details.csv', 'w') as f:
                write = csv.writer(f)
                write.writerow(keys)
                write.writerows(new_list)

# UPDATE the project
def update_project(id, pname, my_url, my_url2, user_input):
    today = datetime.datetime.now()
    db.collection('Project').document(id).update(
        {
            'projectName': pname,
            'URL': my_url,
            'URL2': my_url2,
            'lastDate': today.strftime("%m/%d/%Y, %H:%M:%S"),
            'dataDownload': 'false',
            'userInput': user_input
        }
    )


# DELETE the project
def delete_project(id):
    db.collection('Project').document(id).delete()



def create_user(email, password):
    doc = db.collection('User').document()
    doc.set(
        {
            'userId': doc.id,
            'email': email,
            'password': password
        }
    )

def checking_user_email(email):
    docs = db.collection('User').where('email', '==', email).get()
    # print(docs)
    if docs == []:
        return "Available"
    else:
        return "Exists"

def checking_user_pass(email):
    docs = db.collection('User').where('email', '==', email).get()
    for doc in docs:
        user_pass = doc.to_dict().get('password')
        return (user_pass)

def pass_userrId(email):
    docs = db.collection('User').where('email', '==', email).get()
    for doc in docs:
        userId = doc.to_dict().get('userId')
        return (userId)

def return_user_email(id):
    docs = db.collection('User').where('userId', '==', id).get()
    for doc in docs:
        email = doc.to_dict().get('email')
    return email

def return_user_pass(id):
    docs = db.collection('User').where('userId', '==', id).get()
    for doc in docs:
        password = doc.to_dict().get('password')
    return password

def update_user(id, password):
    db.collection('User').document(id).update(
        {
            'password': password
        }
    )

def delete_user(id):
    db.collection('User').document(id).delete()

def delete_project_with_userId(id):
    # delete every project, user's created
    docs = db.collection('Project').where('userId', '==', id).stream()
    for doc in docs:
        db.collection('Project').document(doc.id).delete()

