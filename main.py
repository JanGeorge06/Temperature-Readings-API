from datetime import datetime
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

cred = credentials.Certificate('iotproject-f3325-firebase-adminsdk-ozxun-9093ec310e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route('/')
def hello():
    return "REST API for Firestore \n Made with Flask"


# Get single room
@app.route('/rooms/<int:room>', methods=['GET'])
def get_temp(room):
    rooms = db.collection('room' + str(room))
    docs = rooms.stream()
    data = []
    for doc in docs:
        temp = str(doc.to_dict()['temp'])
        date = str(doc.to_dict()['date'])
        data.append({'temp': temp, 'date': date})

    return jsonify(data)


# Get all rooms data
@app.route('/rooms', methods=['GET'])
def get_users():
    room1 = db.collection('room1')
    room2 = db.collection('room2')
    room3 = db.collection('room3')
    docs1 = room1.stream()
    docs2 = room2.stream()
    docs3 = room3.stream()
    data1 = []
    data2 = []
    data3 = []
    for doc in docs1:
        temp = str(doc.to_dict()['temp'])
        date = str(doc.to_dict()['date'])
        data1.append({'temp': temp, 'date': date})
    for doc in docs2:
        temp = str(doc.to_dict()['temp'])
        date = str(doc.to_dict()['date'])
        data2.append({'temp': temp, 'date': date})
    for doc in docs3:
        temp = str(doc.to_dict()['temp'])
        date = str(doc.to_dict()['date'])
        data3.append({'temp': temp, 'date': date})

    dic = {
        "Room1": data1,
        "Room2": data2,
        "Room3": data3
    }
    return jsonify(dic)


@app.route('/add', methods=['POST'])
def add_document():
    body = request.json
    temp = body['temp']
    room = body['room']
    if temp == "" or room == "":
        return 'Please pass values'
    else:
        doc = db.collection(room).document()
        date = datetime.now()
        doc.set(
            {
                "temp": temp,
                "date": date
            }
        )
        return "Document created successfully at " + str(date)
