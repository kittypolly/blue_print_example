from project import db

class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String)
    vaccine = db.relationship('Vaccine', backref = 'patient', uselist=False)

    def __init__(self, patient_name):
        self.patient_name = patient_name

    def __repr__(self):
        if self.vaccine:
            return f"환자의 이름은 {self.patient_name} 입니다. 백신은 {self.vaccine.vaccine_name}"
        else:
            return f"환자의 이름은 {self.patient_name} 입니다. 백신은 아직 등록되지 않았습니다."

class Vaccine(db.Model):    
    
    __tablename__ = 'vaccines'

    id = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))


    def __init__(self, vaccine_name, patient_id):
        self.vaccine_name = vaccine_name
        self.patient_id = patient_id

    def __repr__(self):
        return f"{self.vaccine_name}"