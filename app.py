from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/arcgis-dss', methods=['GET','POST'])
def arcgis():
    return render_template('arcgis-dss.html')


socketio.run(app, host="0.0.0.0", port=8888, log_output=True)