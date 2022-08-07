from settings import *
import json
from datetime import datetime

db = SQLAlchemy(app)

class Info(db.Model):
    __tablename__ = 'info'  # creating a table name
    Id_student = db.Column(db.Integer, primary_key=True)  # this is the primary key
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    dofb = db.Column(db.String(80))
    amount_due = db.Column(db.Integer, default = 0, nullable=False)

    # nullable is false so the column can't be empty

    def json(self):
        return {'Id_student': self.Id_student, 'firstName': self.firstName,
                'lastName': self.lastName, 'dofb': self.dofb, 'amount_due': self.amount_due}
        # this method we are defining will convert our output to json    

    
    def add_student(_firstName, _lastName, _dofb, _amount_due):
        # creating an instance of students constructor
        new_student = Info(firstName=_firstName, lastName=_lastName, dofb=_dofb, amount_due = _amount_due)
        db.session.add(new_student)  # add new student to database session
        db.session.commit()  # commit changes to session

    def get_all_students():
        '''function to get all students in our database'''
        return [Info.json(student) for student in Info.query.all()]

    def get_students_by_id(_Id_student):
        print(_Id_student)
        '''function to get student using the id of the student as parameter'''
        return [Info.json(Info.query.filter_by(Id_student=_Id_student).first())]

    def update_student(_Id_student, _firstName, _lastName, _dofb, _amount_due):
        '''function to update the details of a student using the id as parameters'''
        students_to_update = Info.query.filter_by(Id_student=_Id_student).first()
        students_to_update.firstName = _firstName
        students_to_update.lastName = _lastName
        students_to_update.dofb = _dofb
        students_to_update.amount_due = _amount_due
        db.session.commit()

    def delete_student(_Id_student):
        '''function to delete a student from our database using
           the id of the student as a parameter'''
        Info.query.filter_by(Id_student=_Id_student).delete()
        # filter student by id and delete
        db.session.commit()  # commiting the new change to our database