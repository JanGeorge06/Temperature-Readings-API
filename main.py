from flask import Flask, request

app = Flask(__name__)

data = {

}


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return data.get(id, "Not Found")


@app.route('/users', methods=['GET'])
def get_users():
    return data


@app.route('/login', methods=['POST'])
def sign_in():
    body = request.json
    if body['username'] == "":
        return "Enter a username"
    elif not checkIfUsernameExists(body['username']):
        return "Username does not exist"
    elif not checkIfPasswordCorrectMatches(body['username']):
        return "Password is incorrect"
    else:
        return "Logged in successfully"


@app.route('/signup', methods=['POST'])
def sign_up():
    body = request.json
    if body['username'] == "" or body['password'] == "":
        return "Please fill fields"
    if checkIfUsernameExists(body['username']):
        return "Username already exists"
    else:
        if not bool(data):
            data[1] = body
            return "Signed up!"
        else:
            data[list(data.keys())[-1] + 1] = body
            return "Signed up!"


def checkIfUsernameExists(username):
    usernames = []
    i = 1
    for user in data:
        usernames.append(data.get(i)['username'])
        i = i + 1
    if username in usernames:
        return True
    else:
        return False


def checkIfPasswordCorrectMatches(username):
    body = request.json
    password = body['password']
    data_tolist = list(data.values())
    print(data_tolist)
    user_pass = {}
    i = 0
    for user in data_tolist:
        user_pass[data_tolist[i]['username']] = data_tolist[i]['password']
        i = i + 1
    if user_pass[username] != password:
        return False
    else:
        return True
