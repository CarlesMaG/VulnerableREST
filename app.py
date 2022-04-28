# Reference: https://apiflask.com/

from authorization import require_role, generate_token
from apiflask import APIFlask, input, output, abort, HTTPTokenAuth
from sampleData import users, patients, hospitals

from schemas import JwtOutSchema, UserInSchema, UserOutSchema
from schemas import PatientInSchema, PatientOutSchema, PatientSensitiveOutSchema
from schemas import HospitalOutSchema, DepartmentOutSchema

app = APIFlask(__name__)
token_auth = HTTPTokenAuth()


@app.post('/api/login')
@input(UserInSchema(partial=True))
@output(JwtOutSchema)
def login_user(data):
    username = data['username']
    password = data['password']
    user_id = None
    for u in users:
        if u['username'] == username and u['password'] == password:
            user_id = u['id']
    if user_id is not None:
        token = JwtOutSchema()
        token.token = generate_token(user_id)
        return token
    else:
        abort(401)


@app.get('/api/v1/user/<string:user_id>')
@output(UserOutSchema)
@require_role(roles=["Doctor", "Auxiliary"])
def get_user_v1(user_id):
    for u in users:
        if u['id'] == str(user_id):
            return u
    abort(404)


@app.get('/api/v1/patient/<string:patient_id>')
@output(PatientOutSchema)
@require_role(roles=["Doctor", "Auxiliary"])
def get_patient(patient_id):
    for p in patients:
        if p['id'] == str(patient_id):
            return p
    abort(404)


@app.post('/api/v1/patient')
@require_role(roles=["Doctor"])
@input(PatientInSchema(partial=True))
@output(PatientOutSchema)
def post_patient(data):
    patients.append(data)
    return {'message': 'Ok', 'status_code': 200}


@app.put('/api/v1/patient')
@require_role(roles=["Doctor"])
@input(PatientInSchema(partial=True))
@output(PatientOutSchema)
def put_patient(data):
    patients.append(data)
    return {'message': 'Ok', 'status_code': 200}


@app.delete('/api/v1/patient/<string:patient_id>')
@require_role(roles=["Doctor", "Auxiliary"])
def delete_patient(patient_id):
    for p in patients:
        if p['id'] == str(patient_id):
            patients.remove(p)
            return {'message': 'Ok', 'status_code': 200}
    abort(404)


@app.get('/api/v1/patient/<string:patient_id>/sensitive')
@output(PatientSensitiveOutSchema)
@require_role(roles=["Doctor"])
def get_patient_sensitive(patient_id):
    for p in patients:
        if p['id'] == str(patient_id):
            return p
    abort(404)


@app.get('/api/v1/admin')
def get_admin_v1():
    return {'message': 'You are not allowed to perform this action', 'status_code': 200}


@app.get('/api/v1/hospital/<string:hospital_id>')
@output(HospitalOutSchema)
def get_hospital_v1(hospital_id):
    for h in hospitals:
        if h['id'] == str(hospital_id):
            return h
    abort(404)


@app.get('/api/v1/hospital/<string:hospital_id>/department/<string:department_id>')
@output(DepartmentOutSchema)
def get_department_v1(hospital_id, department_id):
    for h in hospitals:
        if h['id'] == str(hospital_id):
            for d in h['departments']:
                if d['id'] == str(department_id):
                    return d
    abort(404)

