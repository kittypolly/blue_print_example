# __init__.py는 패키지를 만들기 위해서 필수적으로 있어야 한다.
# import os는 운영체제를 제어할 수 있다.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOA'

# 개인 PC의 바탕화면에 파일이 있다고 가정한다.
# basedir의 형태는 "C:\Users\kanghyun\Desktop\project" 이다.
basedir = os.path.abspath(os.path.dirname(__file__))

# 아래의 결과는 "sqlite:///C:\Users\kanghyun\Desktop\project\data.sqlite" 이다.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from project.patient.views import patients_blueprints
from project.vaccine.views import vaccines_blueprints

app.register_blueprint(patients_blueprints, url_prefix='/patients')
app.register_blueprint(vaccines_blueprints, url_prefix='/vaccines')