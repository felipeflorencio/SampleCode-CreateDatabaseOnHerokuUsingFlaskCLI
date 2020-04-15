import os
from flask import Flask, jsonify, render_template
import database
import commands
from model import Model

# init flask app instance
app = Flask(__name__)
# setup with the configuration provided by the user / environment
app.config.from_object(os.environ['APP_SETTINGS'])

# setup all our dependencies, for now only database using application factory pattern
database.init_app(app)
commands.init_app(app)

@app.route("/")
def main_page():
    items = Model.query.all()
    return render_template('index.html', items=items)

@app.route("/add/<string:item>", methods=['POST'])
def add_new_item(item):
    model = Model(parameter=item)
    
    # add to the database session
    database.db.session.add(model)
        
    # commit to persist into the database
    database.db.session.commit()
    
    return jsonify({"sucess": model.parameter})

if __name__ == "__main__":
    app.run()