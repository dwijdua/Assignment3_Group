from info import *
from datetime import datetime

# route to get all students
@app.route('/info', methods=['GET'])
def get_students():
    '''Function to get all the students in the database'''
    return jsonify({'Students': Info.get_all_students()})

# route to get students by id
@app.route('/info/<int:Id_student>', methods=['GET'])
def get_students_by_id(Id_student):
    print(Id_student)
    return_value = Info.get_students_by_id(Id_student)
    return jsonify(return_value)

# route to add new stsudent
@app.route('/info', methods=['POST'])
def add_student():
    '''Function to add new student to  database'''
    request_data = request.get_json()  # getting data from client
    Info.add_student(request_data["firstName"], request_data["lastName"],
                    request_data["dofb"], request_data["amount_due"])
    response = Response("Student added", 201, mimetype='application/json')
    return response

# route to update student with PUT method
@app.route('/info/<int:Id_student>', methods=['PUT'])
def update_student(Id_student):
    '''Function to edit student in our database using student id'''
    request_data = request.get_json()
    Info.update_student(Id_student, request_data['firstName'], request_data['lastName'], request_data['dofb'], request_data["amount_due"])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response

# route to delete student using the DELETE method
@app.route('/info/<int:Id_student>', methods=['DELETE'])
def remove_student(Id_student):
    '''Function to delete student from our database'''
    Info.delete_student(Id_student)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=8088, debug=True)