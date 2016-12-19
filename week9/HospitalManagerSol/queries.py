DROP_USER_TABLE = '''
    DROP TABLE IF EXISTS USER
'''

DROP_PATIENT_TABLE = '''
    DROP TABLE IF EXISTS PATIENT
'''

DROP_DOCTOR_TABLE = '''
    DROP TABLE IF EXISTS DOCTOR
'''

DROP_HOSPITAL_STAY_TABLE = '''
    DROP TABLE IF EXISTS HOSPITAL_STAY
'''

DROP_VISITATION_TABLE = '''
    DROP TABLE IF EXISTS VISITATION
'''


CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS USER (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        IS_ACTIVE INTEGER NOT NULL DEFAULT 0,
        AGE INTEGER
    )
'''

CREATE_DOCTOR_TABLE = '''
    CREATE TABLE IF NOT EXISTS DOCTOR (
        ID INTEGER PRIMARY KEY,
        ACADEMIC_TITLE TEXT,
        VISITATION_HOURS TEXT DEFAULT 'N/A',
        FOREIGN KEY (ID) REFERENCES USER(ID)
    )
'''

CREATE_PATIENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS PATIENT (
        ID INTEGER PRIMARY KEY,
        DOCTOR_ID INTEGER,
        FOREIGN KEY (ID) REFERENCES USER(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''

CREATE_HOSPITAL_STAY_TABLE = '''
    CREATE TABLE IF NOT EXISTS HOSPITAL_STAY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STARTDATE TEXT NOT NULL,
        ENDDATE TEXT,
        ROOM INTEGER NOT NULL,
        INJURY TEXT NOT NULL,
        PATIENT_ID INTEGER,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID)
    )
'''

CREATE_VISITATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS VISITATION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PATIENT_ID INTEGER,
        DOCTOR_ID INTEGER NOT NULL,
        START_HOUR TEXT NOT NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''

INSERT_INTO_HOSPITAL_STAY = '''
    INSERT INTO HOSPITAL_STAY (STARTDATE, ENDDATE, ROOM, INJURY, PATIENT_ID)
    VALUES (?, ?, ?, ?, ?)
'''

INSERT_INTO_USER = '''
    INSERT INTO USER ( USERNAME, PASSWORD, AGE )
    VALUES (?, ?, ?)
'''

INSERT_INTO_VISITATION = '''
    INSERT INTO VISITATION (PATIENT_ID, DOCTOR_ID, START_HOUR)
    VALUES (?, ?, ?)
'''

PROMOTE_TO_PATIENT = '''
    INSERT INTO PATIENT (ID, DOCTOR_ID)
    VALUES (?, ?)
'''

PROMOTE_TO_DOCTOR = '''
    INSERT INTO DOCTOR ( ID, ACADEMIC_TITLE )
    VALUES (?, ?)
'''

SELECT_DOCTORS = '''
    SELECT * FROM DOCTOR
'''

SELECT_PATIENTS = '''
    SELECT * FROM PATIENT
'''

SELECT_USERS = '''
    SELECT * FROM USER
'''

SELECT_LAST_USER = '''
    SELECT *
    FROM user
    WHERE user.id = ( SELECT MAX(id) FROM USER )
'''

SELECT_DOCTOR_NAME = '''
    SELECT user.username, doctor.academic_title
    FROM doctor
    LEFT JOIN user
    ON doctor.id = user.id
'''

SELECT_SPECIFIC_DOCTOR = '''
    SELECT doctor.id, user.username, doctor.academic_title
    FROM doctor
    LEFT JOIN user
    ON doctor.id = user.id
    LIMIT 1 OFFSET ?
'''

UPDATE_LOGIN = '''
    UPDATE user
    SET is_active = 1
    WHERE id = ?
'''

UPDATE_LOGOUT = '''
    UPDATE USER
    SET IS_ACTIVE = 0
    WHERE user.username = ?
'''

UPDATE_VISITATION_HOURS = '''
    UPDATE doctor
    SET visitation_hours = ?
    WHERE doctor.id = ?
'''

GET_PATIENT_BY_USERNAME = '''
    SELECT *
    FROM patient
    JOIN user ON patient.id = user.id
    WHERE user.username = ?
'''

GET_ACADEMIC_TITLE = '''
    SELECT doctor.academic_title
    FROM patient
    JOIN doctor ON patient.doctor_id = doctor.id
    JOIN user ON patient.id = user.id
    WHERE user.username = ?
'''

GET_HOSPITAL_STAYS = '''
    SELECT h.startdate, h.room, h.injury
    FROM hospital_stay AS h
    JOIN patient ON patient.id = h.patient_id
    WHERE patient.id = ?
'''

UPDATE_USERNAME = '''
    UPDATE user
    SET username = ?, age = ?
    WHERE username = ?
'''

UPDATE_DOCTOR = '''
    UPDATE patient
    SET doctor_id = ?
    WHERE patient.id = ?
'''

GET_VISITATION_HOURS = '''
    SELECT doctor.visitation_hours
    FROM patient
    JOIN doctor ON patient.doctor_id = doctor.id
    WHERE patient.id = ?
'''

GET_DOCTOR_PATIENTS = '''
    SELECT
    GROUP_CONCAT(user.username) AS patients
    FROM user
    JOIN patient ON patient.id = user.id
    WHERE patient.doctor_id = ?
'''

GET_DOCTOR_ID_BY_NAME = '''
    SELECT doctor.id
    FROM doctor
    JOIN user ON user.id = doctor.id
    WHERE user.username = ?
'''

GET_DOCTOR_BY_USERNAME = '''
    SELECT *
    FROM doctor
    JOIN user ON user.id = doctor.id
    WHERE user.username = ?
'''

DELETE_VISITATION_HOURS = '''
    UPDATE doctor
    SET visitation_hours = 'N/A'
    WHERE doctor.id = ?
'''


GET_ROOM_AND_DURATION_OF_STAY = '''
    SELECT user.username, hospital_stay.room,
    hospital_stay.startdate, hospital_stay.enddate
    FROM hospital_stay
    JOIN patient ON patient.id = hospital_stay.patient_id
    JOIN user ON patient.id = user.id
    WHERE patient.doctor_id = ?;
'''
