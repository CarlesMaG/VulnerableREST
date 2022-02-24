from apiflask import  Schema
from apiflask.fields import Integer, String, UUID
from apiflask.validators import Length, OneOf


class UserInSchema(Schema):
    id = String(required=True, validate=Length(0, 128))
    username = String(required=True, validate=Length(0, 128))
    password = String(required=True, validate=Length(0, 128))
    mail = String(required=True, validate=Length(0, 128))


class UserOutSchema(Schema):
    id = String()
    username = String()
    mail = String()


class JwtOutSchema(Schema):
    token = String()


class PatientInSchema(Schema):
    id = String(required=True, validate=Length(0, 128))
    name = String(required=True, validate=Length(0, 20))
    surname = String(required=True, validate=Length(0, 20))
    sensitive_data = String(required=True, validate=Length(0, 100))


class PatientOutSchema(Schema):
    id = String()
    name = String()
    surname = String()


class PatientSensitiveOutSchema(Schema):
    id = String()
    name = String()
    surname = String()
    sensitive_data = String()


class HospitalOutSchema(Schema):
    id = String()
    name = String()
    address = String()
    phone = String()
