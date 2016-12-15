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
        i = 0
        for row in result:
            i += 1
            print('{}'.format(i), row['firstname'], row['lastname'])

    def list_all_doctors(self):
        doctors = """
        SELECT *
        FROM DOCTOR;
        """
        result = self.cursor.execute(doctors)
        i = 0
        for doctor in result:
            i += 1
            print('{}'.format(i), doctor['firstname'], doctor['lastname'])

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

    def add_hospital_stay(self, room, startdate, enddate, injury, patient):
        query = """
        INSERT INTO HOSPITAL_STAY (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
        VALUES (?, ?, ?, ?, ?)
        """

        self.cursor.execute(query, (room, startdate, enddate, injury, patient))
        self.__commit()

    def __update_patient(self, attr, patient, value):
        query = """
        UPDATE PATIENT
        SET {0} = ?
        WHERE patient.firstname = ? AND patient.lastname = ?
        """.format(attr)

        self.cursor.execute(query, (value,
                                    patient.split(' ')[0],
                                    patient.split(' ')[1]))
        self.__commit()

    def __update_doctor(self, attr, doctor, value):
        query = """
        UPDATE DOCTOR
        SET {0} = ?
        WHERE doctor.firstname = ? AND doctor.lastname = ?
        """.format(attr)

        self.cursor.execute(query, (value,
                                    doctor.split(' ')[0],
                                    doctor.split(' ')[1]))
        self.__commit()

    def update_doctor_information(self):
        print("Update doctor? (first name, last name?)")
        change = input()
        print("Doctor current first name and last name: ")
        update = input()
        print("New information: ")
        new = input()
        if change == "first name":
            self.__update_doctor("firstname", update, new)
        elif change == "last name":
            self.__update_doctor("lastname", update, new)

    def update_patient_information(self):
        print("Update patient? (first name, last name, age, gender, doctor?)")
        change = input()
        print("Patient current first name and last name: ")
        update = input()
        print("New information: ")
        new = input()
        if change == "first name":
            self.__update_patient("firstname", update, new)
        elif change == "last name":
            self.__update_patient("lastname", update, new)
        elif change == "age":
            self.__update_patient("age", update, new)
        elif change == "gender":
            self.__update_patient("gender", update, new)
        elif change == "doctor":
            self.__update_patient("gender", update, new)
        else:
            print("Invalid information!")

    def __delete_patient(self, fname, lname):
        query = """
        DELETE FROM PATIENT
        WHERE patient.firstname = ? AND patient.lastname = ?
        """
        self.cursor.execute(query, (fname, lname))
        self.__commit()

    def delete_patient(self):
        print("Delete patient? (firstname lastname)")
        to_del = input()
        self.__delete_patient(to_del.split(' ')[0], to_del.split(' ')[1])


def main():
    hospital = HospitalAPI('hospital.db')
    hospital.add_patient("Pesho", "Peshov", 12, 'M', 5)
    hospital.add_doctor("Courtney", "Cake")
    hospital.delete_patient()
    # hospital.update_doctor_information()
    # hospital.update_patient_information()
    hospital.list_all_patients()
    hospital.list_all_doctors()


if __name__ == '__main__':
    main()
