import sqlite3
from queries import *
from settings import *
from random import choice
from users import User, Doctor, Patient
from datetime import datetime, timedelta

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def insert_user(user):
    c.execute(INSERT_INTO_USER, (user.username,
                                 user.password,
                                 user.age))

    db.commit()


def promote_to_doctor(user, academic_title):
    c.execute(SELECT_LAST_USER)
    users = c.fetchall()
    doctor = Doctor()
    doctor.init_components(academic_title)

    print("user = ", users)
    doctor = (users[0]['id'], doctor.academic_title)

    c.execute(PROMOTE_TO_DOCTOR, doctor)
    db.commit()


def promote_to_patient(user, doctor=None):
    c.execute(SELECT_LAST_USER)
    users = c.fetchall()
    patient = Patient()
    c.execute(SELECT_SPECIFIC_DOCTOR, (int(doctor) - 1, ))
    doctor = c.fetchall()
    patient.init_components(doctor[0]['id'])

    patient = (users[0]['id'], patient.doctor_id)

    c.execute(PROMOTE_TO_PATIENT, patient)
    db.commit()


def add_visitation(username, starthour):
    c.execute(GET_PATIENT_BY_USERNAME, (username, ))
    patient = c.fetchall()

    c.execute(INSERT_INTO_VISITATION, (patient[0]['id'],
                                       patient[0]['doctor_id'],
                                       starthour))
    db.commit()


def get_academic_title(username):
    c.execute(GET_ACADEMIC_TITLE, (username, ))
    title = c.fetchone()
    return title


def add_hospital_stay(username, injury, startdate, enddate):
    c.execute(GET_PATIENT_BY_USERNAME, (username, ))
    patient = c.fetchone()

    room = choice(ROOM_NUMBERS)

    c.execute(INSERT_INTO_HOSPITAL_STAY, (startdate,
                                          enddate,
                                          room,
                                          injury,
                                          patient['id']))
    db.commit()


def view_hospital_stays(username):
    c.execute(GET_PATIENT_BY_USERNAME, (username, ))
    patient = c.fetchone()

    c.execute(GET_HOSPITAL_STAYS, (patient['id'], ))
    stays = c.fetchall()
    res = []

    for stay in stays:
        res.append((stay['startdate'], stay['room'], stay['injury']))

    return res


def update_username_and_age(username, new_username, new_age):
    c.execute(UPDATE_USERNAME, (new_username, new_age, username))
    db.commit()


def update_patient_doctor(username, new_doctor_id):
    c.execute(GET_PATIENT_BY_USERNAME, (username, ))
    patient = c.fetchone()

    c.execute(SELECT_SPECIFIC_DOCTOR, (int(new_doctor_id) - 1, ))
    doctor = c.fetchone()

    c.execute(UPDATE_DOCTOR, (doctor['id'], patient['id']))
    db.commit()


def get_visitation_hours(username):
    c.execute(GET_PATIENT_BY_USERNAME, (username, ))
    patient = c.fetchone()

    c.execute(GET_VISITATION_HOURS, (patient['id'], ))
    hours = c.fetchone()['visitation_hours']

    return hours


def get_doctor_patients(username):
    c.execute(GET_DOCTOR_ID_BY_NAME, (username, ))
    doctor = c.fetchone()

    c.execute(GET_DOCTOR_PATIENTS, (doctor['id'], ))
    patients = c.fetchall()

    for patient in patients:
        print("{}".format(patient['patients']))


def update_visitation_hours(username, hours):
    c.execute(GET_DOCTOR_ID_BY_NAME, (username, ))
    doctor = c.fetchone()

    c.execute(UPDATE_VISITATION_HOURS, (hours, doctor['id']))
    db.commit()


def delete_visitation_hours(username):
    c.execute(GET_DOCTOR_ID_BY_NAME, (username, ))
    doctor = c.fetchone()

    c.execute(DELETE_VISITATION_HOURS, (doctor['id'], ))
    db.commit()


def get_rooms_and_duration(username):
    c.execute(GET_DOCTOR_BY_USERNAME, (username, ))
    doc = c.fetchone()

    c.execute(GET_ROOM_AND_DURATION_OF_STAY, (doc['id'], ))
    patients = c.fetchall()

    for patient in patients:
        print("{} in room {} for {}".format(patient['username'],
                                            patient['room'],
                                            str(datetime.strptime(
                                                patient['enddate'],
                                                '%Y-%m-%d') -
                                            datetime.strptime(
                                                patient['startdate'],
                                                '%Y-%m-%d')).split(',')[0]))
