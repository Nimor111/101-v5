import sqlite3
import getpass
import datetime
from random import choice
from settings import *
from queries import *
from users import User, Doctor, Patient
from password import encode_pass


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def create_database():
    c.execute(CREATE_USER_TABLE)
    c.execute(CREATE_DOCTOR_TABLE)
    c.execute(CREATE_PATIENT_TABLE)
    c.execute(CREATE_HOSPITAL_STAY_TABLE)
    c.execute(CREATE_VISITATION_TABLE)
    db.commit()


def drop_database_tables():
    c.execute(DROP_USER_TABLE)
    c.execute(DROP_DOCTOR_TABLE)
    c.execute(DROP_PATIENT_TABLE)
    c.execute(DROP_HOSPITAL_STAY_TABLE)
    c.execute(DROP_VISITATION_TABLE)
    db.commit()


def insert_users():
    users = [("Dr. Albena Bachvarova", "123456", 47),
             ("Kristina Valchanova", "123123", 20),
             ("Dr. Pavlina Zdravkova", "111111", 56),
             ("Pandio Pandev", "panda", 4),
             ("Slayana Monkova", "159357", 21),
             ("Kiril Ivanov", "kireto", 22),
             ("Dr. Georgi Georgiev", "doctora", 50)]
    c.executemany(INSERT_INTO_USER, users)
    db.commit()


def promote_to_doctors():
    c.execute(SELECT_USERS)
    users = c.fetchall()
    doctors = []

    for user in users:
        if 'Dr.' in user['username']:
            academic_title = choice(ACADEMIC_TITLES)
            doctors.append((user['id'], academic_title))

    c.executemany(PROMOTE_TO_DOCTOR, doctors)
    db.commit()


def promote_to_patients():
    c.execute(SELECT_USERS)
    users = c.fetchall()
    patients = []
    doctors = c.execute(SELECT_DOCTORS)
    doc_ids = [doc['id'] for doc in doctors]

    for user in users:
        if 'Dr.' not in user['username']:
            doctor = choice(doc_ids)
            patients.append((user['id'], doctor))

    c.executemany(PROMOTE_TO_PATIENT, patients)
    db.commit()


def add_doctors_visitations():
    pass


def add_hospital_stays():
    c.execute(SELECT_PATIENTS)
    patients = c.fetchall()

    for patient in patients:
        room = choice(ROOM_NUMBERS)
        injury = choice(INJURIES)
        startdate = str(datetime.datetime.now()).split()[0]
        enddate = str(datetime.datetime.now()).split()[0]

        c.execute(INSERT_INTO_HOSPITAL_STAY, (startdate,
                                              enddate,
                                              room,
                                              injury,
                                              patient['id']))
    db.commit()


def patient_visitations():
    c.execute(SELECT_PATIENTS)
    patients = c.fetchall()
    c.execute(SELECT_DOCTORS)
    doctors = c.fetchall()
    docids = [doctor['id'] for doctor in doctors]

    for patient in patients:
        startdate = str(datetime.datetime.now()).split()[0]
        doctor = choice(docids)

        c.execute(INSERT_INTO_VISITATION, (patient['id'],
                                           doctor,
                                           startdate))

    db.commit()


def create_and_fill_data():
    drop_database_tables()
    create_database()
    insert_users()
    promote_to_doctors()
    promote_to_patients()
    add_doctors_visitations()
    add_hospital_stays()
    patient_visitations()


def main():
    pass


if __name__ == '__main__':
    main()
