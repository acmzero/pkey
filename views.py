from flask import Flask
from flask import request

import hashlib

from models import db, User, app

@app.route('/api/users/create', methods = ['POST'])
def createUser():
  data = {}
  data['username'] = request.args.get('username')

  users = User.query.filter(User.username == data['username'])
  if (len(users.all()) > 0):
    return "User already exists"
  data['email'] = request.args.get('email')
  passwordU = request.args.get('password')
  data['password'] = hashlib.sha1(passwordU).hexdigest()

  user = User(data)
  db.session.add(user)
  db.session.commit()

  return str(user.id)

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
