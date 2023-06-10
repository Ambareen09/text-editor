from app import app
from flask import render_template, Flask, jsonify
import os

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return "It's about!!!"

@app.route('/env_variable')
def get_env_variable():
    env_var_name = 'MY_ENV_VARIABLE'
    env_var_value = os.environ.get(env_var_name)
    if env_var_value is None:
        return jsonify({'error': f'Environment variable {env_var_name} not found'}), 404
    else:
        return jsonify({'env_variable': env_var_value})