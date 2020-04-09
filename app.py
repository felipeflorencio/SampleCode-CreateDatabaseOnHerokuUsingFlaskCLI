import os
from flask import Flask, jsonify
import database

# init flask app instance
app = Flask(__name__)
# setup with the configuration provided by the user / environment
app.config.from_object(os.environ['APP_SETTINGS'])

# setup all our dependencies, for now only database using application factory pattern
database.init_app(app)

@app.route("/")
def main_page():
    return "Main Page"

@app.route("/add/<string:item>", methods=['POST'])
def add_new_item(item):
    return jsonify({"sucess": item})

if __name__ == "__main__":
    app.run()