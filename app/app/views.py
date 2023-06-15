from app import app, socketio, db
from flask import render_template, jsonify, request
from app.models import User, Text
import os


@app.route("/")
def index():
    users = User.query.all()
    if len(users) == 0:
        # Initialize a row with default values
        default_user = User(name='Delilah Doe', email='delilah@example.com')
        db.session.add(default_user)
        db.session.commit()
        users = [default_user]

    # Assuming the first user in the list, you can modify this logic based on your requirement
    user_id = users[0].id
    return render_template("public/index.html", users=users, user_id=user_id)


@app.route("/about")
def about():
    return "It's about!!!"


@app.route('/env_variable')
def get_env_variable():
    env_var_name = 'MY_ENV_VARIABLE'
    env_var_value = os.environ.get(env_var_name)
    if env_var_value is None:
        return jsonify({'error': f'Environment variable {env_var_name} not found, use -> export MY_ENV_VARIABLE=your_value to set it'}), 404
    else:
        return jsonify({'env_variable': env_var_value})


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    if len(users) == 0:
        # Initialize a row with default values
        default_user = User(name='Ambareen Azam', email='ambu@example.com')
        db.session.add(default_user)
        db.session.commit()
        users = [default_user]

    user_data = []
    for user in users:
        user_data.append(
            {'id': user.id, 'name': user.name, 'email': user.email})

    return jsonify({'users': user_data})


@socketio.on('message')
def handle_message(data):
    text = data['text']
    user_id = data['user_id']

    # Save the text to the database
    user = User.query.get(user_id)
    new_text = Text(text=text, user=user)
    db.session.add(new_text)
    db.session.commit()

    # Broadcast the message to all connected clients
    socketio.emit('message', {'text': text, 'user_id': user_id}, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
