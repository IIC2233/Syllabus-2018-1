import flask
import json
app = flask.Flask(__name__)

@app.route("/")
def index():
   return "Hello World"

@app.route("/json")
def retornar_json():
    # /json
    return json.dumps({"arg_1": 1})

@app.route("/parametros", methods=["GET"])
def recibir_parametros():
    # /parametros?username=herny
    username = flask.request.args.get('username')
    return json.dumps({"USUARIO": username})

if __name__ == "__main__":
   app.run()