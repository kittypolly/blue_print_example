from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Patient
from project.patient.forms import Patient_addform, Patient_delform

# Blueprint를 가져왔고 project 폴더에서 db를 가져왔다.
# 필요한 모듈만 가져올 수 있도록 했다.
# 기존에 있던 main.py 에서 뷰와 폼 부분을 떼어 왔다.
# url_for 부분을 수정했다.

patients_blueprints = Blueprint('patients', __name__,
                                template_folder = 'templates/patients')

@patients_blueprints.route('/add_patient', methods=['GET','POST'])
def add_patient():

    form = Patient_addform()

    if form.validate_on_submit():

        add_patient = form.Patient_add.data
        new_patient = Patient(add_patient)
        db.session.add(new_patient)
        db.session.commit()

        return redirect(url_for('patients.list'))

    return render_template('add_patient.html', form=form)

@patients_blueprints.route('/list')
def list():

    patients = Patient.query.all()
    return render_template('list.html', patients=patients) 


@patients_blueprints.route('/delete', methods=['GET','POST'])
def delete():

    form = Patient_delform()

    if form.validate_on_submit():

        del_patient = form.Patient_del.data
        deleted_patient = Patient.query.get(del_patient)
        db.session.delete(deleted_patient)
        db.session.commit()
    
        return redirect(url_for('patients.list'))

    return render_template('delete.html', form=form)