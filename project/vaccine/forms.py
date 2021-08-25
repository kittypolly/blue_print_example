from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Vaccine_addform(FlaskForm):

    Vaccine_add = StringField('추가할 백신이름을 입력해주세요:')
    Patient_id = IntegerField('백신을 추가할 환자아이디를 입력해주세요.')
    submit = SubmitField('백신을 해당 아이디에 추가합니다.')