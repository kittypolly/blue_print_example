from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Vaccine
from project.vaccine.forms import Vaccine_addform

# Blueprint를 가져왔고 project 폴더에서 db를 가져왔다.
# 필요한 모듈만 가져올 수 있도록 했다.
# 기존에 있던 main.py 에서 뷰와 폼 부분을 떼어 왔다.
# url_for 부분을 수정했다.

vaccines_blueprints = Blueprint('vaccines', __name__,
                                template_folder = 'templates/vaccines')

@vaccines_blueprints.route('/add_vaccine', methods=['GET','POST'])
def add_vaccine():

    form = Vaccine_addform()

    if form.validate_on_submit():

        add_vaccine = form.Vaccine_add.data
        rel_patient_id = form.Patient_id.data
        new_vaccine = Vaccine(add_vaccine, rel_patient_id)
        db.session.add(new_vaccine)
        db.session.commit()
    
        # url_for에 들어갈 내용은 Blueprint의 첫 변수.[함수의 이름]이다.
        return redirect(url_for('patients.list'))

    return render_template('add_vaccine.html', form=form)