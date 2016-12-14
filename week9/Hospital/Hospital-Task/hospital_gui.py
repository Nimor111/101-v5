from create_database import *


class HospitalAPI:

    def __init__(self, name):
        self.name = name
        self.db = create_database(self.name)[0]
        self.cursor = create_database(self.name)[1]

    def close(self):
        self.db.close()

    def __del__(self):
        self.close()

    def __commit(self):
        self.db.commit()

    def list_all_patients(self):
        patients = """
        SELECT *
        FROM PATIENT;
        """
        result = self.cursor.execute(patients)

        for row in result:
            print(row['firstname'], row['lastname'])

    def list_all_doctors(self):
        doctors = """
        SELECT *
        FROM DOCTOR;
        """
        result = self.cursor.execute(doctors)

        for doctor in result:
            print(doctor['firstname'], doctor['lastname'])

    def add_patient(self, firstname, lastname, age,
                    gender, doctor):
        query = """
        INSERT INTO PATIENT (FIRSTNAME, LASTNAME, AGE,
                             GENDER, DOCTOR)
        VALUES( ?, ?, ?, ?, ?)
        """

        self.cursor.execute(query, (firstname, lastname, age, gender, doctor))
        self.__commit()

    def add_doctor(self, firstname, lastname):
        query = """
        INSERT INTO DOCTOR (FIRSTNAME, LASTNAME)
        VALUES( ?, ? )
        """

        self.cursor.execute(query, (firstname, lastname))
        self.__commit()


def main():
    hospital = HospitalAPI('hospital.db')
    hospital.add_patient("Pesho", "Peshov", 12, 'M', 5)
    hospital.add_doctor("I", "Cake")
    hospital.list_all_patients()
    hospital.list_all_doctors()


if __name__ == '__main__':
    main()
