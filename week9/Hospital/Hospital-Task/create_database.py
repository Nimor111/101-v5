import sqlite3


def create_patients_table():
    create_table_patients = """
    CREATE TABLE IF NOT EXISTS PATIENT
    (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      FIRSTNAME TEXT NOT NULL,
      LASTNAME TEXT NOT NULL,
      AGE int NOT NULL,
      GENDER TEXT,
      DOCTOR INT,
      FOREIGN KEY(DOCTOR) REFERENCES DOCTORS(ID)
    )
    """
    return create_table_patients


def create_hospital_stay_table():
    create_table_hospital_stay = """
    CREATE TABLE IF NOT EXISTS HOSPITAL_STAY
    (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      ROOM INT NOT NULL,
      STARTDATE TEXT NOT NULL,
      ENDDATE DATE,
      INJURY TEXT NOT NULL,
      PATIENT INT,
      FOREIGN KEY(PATIENT) REFERENCES PATIENTS(ID)
    )
    """
    return create_table_hospital_stay


def create_doctors_table():
    create_table_doctors = """
    CREATE TABLE IF NOT EXISTS DOCTOR
    (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      FIRSTNAME TEXT NOT NULL,
      LASTNAME TEXT NOT NULL
    )
    """
    return create_table_doctors


def insert_patients(patients):
    pass


def create_database(name):
    DB_NAME = name
    db = sqlite3.connect(DB_NAME)
    db.row_factory = sqlite3.Row
    c = db.cursor()

    drop_tables = [""" DROP TABLE IF EXISTS PATIENT """,
                   """ DROP TABLE IF EXISTS HOSPITAL_STAY """,
                   """ DROP TABLE IF EXISTS DOCTOR """]
    for drop in drop_tables:
        c.execute(drop)
        db.commit()

    create_tables = [create_patients_table(), create_doctors_table(),
                     create_hospital_stay_table()]

    for table in create_tables:
        c.execute(table)
        db.commit()

    insert_patient = """
    INSERT INTO PATIENT ( FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR )
    VALUES(?, ?, ?, ?, ?)
    """
    insert_doctor = """
    INSERT INTO DOCTOR ( FIRSTNAME, LASTNAME )
    VALUES(?, ?)
    """
    insert_hospital_stay = """
    INSERT INTO HOSPITAL_STAY (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
    VALUES (?, ?, ?, ?, ?)
    """

    patients = [('Rositsa', 'Zlateva', 22, 'F', 1),
                ('Kamen', 'Kotsev', 22, 'M', 2),
                ('Monika', 'Valerieva', 30, 'F', 2),
                ('Kristina', 'Valchanova', 21, 'F', 1),
                ('Ivaylo', 'Bachvarov', 23, 'M', 3),
                ('Pandio', 'Pandev', 4, 'M', 3)]

    c.executemany(insert_patient, patients)
    db.commit()

    hospital_stays = [(3, '2016-10-10', '2016-10-11', 'crazy', 1),
                      (6, '2016-10-12', '2016-10-15', 'headache', 2),
                      (2, '2016-09-30', '2016-10-01', 'crazy', 3),
                      (5, '2016-10-17', '2016-10-20', 'pregnancy', 4),
                      (3, '2016-10-12', '2016-10-12', 'кidney сtones', 5),
                      (7, '2016-10-09', '2016-10-12', 'headache', 6),
                      (1, '2016-10-09', '2016-10-11', 'hernia', 7),
                      (1, '2016-10-23', '2016-10-25', 'toothache', 1)]

    c.executemany(insert_hospital_stay, hospital_stays)
    db.commit()

    doctors = [('Pavlina', 'Zdravkova'),
               ('Valentina', 'Yordanova'),
               ('Albena', 'Bachvarova')]

    c.executemany(insert_doctor, doctors)
    db.commit()

    return (db, c)


def main():
    pass  # create_database("hospital.db")


if __name__ == '__main__':
    main()
