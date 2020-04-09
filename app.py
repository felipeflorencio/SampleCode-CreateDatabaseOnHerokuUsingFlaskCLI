from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Main Page"

@app.route("/add/<string:item>", methods=['POST'])
def add_new_item(item):
    return jsonify({"sucess": item})

if __name__ == "__main__":
    app.run()