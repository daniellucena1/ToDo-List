from flask import Flask
from routes.home import home_route
from routes.tasks import task_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(task_route, url_prefix='/tasks')
