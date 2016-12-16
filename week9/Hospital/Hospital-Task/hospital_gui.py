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
        FROM PATIENT
        """
        result = self.cursor.execute(patients)
        i = 0
        for row in result:
            print(row['id'], row['firstname'], row['lastname'])

    def list_all_doctors(self):
        doctors = """
        SELECT *
        FROM DOCTOR
        """
        result = self.cursor.execute(doctors)
        i = 0
        for doctor in result:
            print(doctor['id'], doctor['firstname'], doctor['lastname'])

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

    def __update_patient(self, attr, patient_id, value):
        query = """
        UPDATE PATIENT
        SET {0} = ?
        WHERE patient.id = ?
        """.format(attr)

        self.cursor.execute(query, (value, patient_id))
        self.__commit()

    def __update_doctor(self, attr, doctor_id, value):
        query = """
        UPDATE DOCTOR
        SET {0} = ?
        WHERE doctor.id = ?
        """.format(attr)

        self.cursor.execute(query, (value, doctor_id))
        self.__commit()

    def __update_hospital_stay(self, attr, patient_id, value):
        query = """
        UPDATE HOSPITAL_STAY
        SET {0} = ?
        WHERE hospital_stay.patient IN (SELECT
                                        FROM patient
                                        WHERE patient.id = ?
        """.format(attr)

        self.cursor.execute(query, (value, patient_id))
        self.__commit()

    def update_hospital_information(self):
        print("Update stay of patient? (id)")
        update = input()
        print("Attribute to change? (room, startdate, enddate, \
                                     injury, patient? ")
        change = input()
        print("New information: ")
        new = input()
        if change == "room":
            self.__update_hospital_stay("room", update, new)
        elif change == "startdate":
            self.__update_hospital_stay("startdate", update, new)
        elif change == "enddate":
            self.__update_hospital_stay("enddate", update, new)
        elif change == "injury":
            self.__update_hospital_stay("injury", update, new)
        elif change == "patient":
            self.__update_patient("patient", update, new)
        else:
            print("Invalid information!")

    def update_doctor_information(self):
        print("Update doctor? (id)")
        change = input()
        print("Doctor current first name and last name: ")
        update = input()
        print("New information: ")
        new = input()
        if change == "first name":
            self.__update_doctor("firstname", update, new)
        elif change == "last name":
            self.__update_doctor("lastname", update, new)
        else:
            print("Invalid information!")

    def update_patient_information(self):
        print("Update patient? (first name, last name, age, gender, doctor?)")
        change = input()
        print("Patient id?")
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

    def __delete_patient(self, patient_id):
        query = """
        DELETE
        FROM PATIENT
        WHERE patient.id = ?;
        """
        self.cursor.execute(query, patient_id)
        self.__commit()

    def __delete_doctor(self, doctor_id):
        query = """
        DELETE
        FROM DOCTOR
        WHERE doctor.id = ?
        """
        self.cursor.execute(query, (patient_id))
        self.__commit()

    def __delete_hospital_stay(self, patient_id):
        query = """
        DELETE
        FROM hospital_stay
        WHERE hospital_stay.patient IN ( SELECT patient.id
                                         FROM patient
                                         WHERE patient.id = ?
        """
        self.cursor.execute(query, (patient_id))
        self.__commit()

    def delete_patient(self):
        print("Delete patient? (id)")
        to_del = input()
        self.__delete_patient(to_del)

    def delete_doctor(self):
        print("Delete doctor? (id)")
        to_del = input()
        self.__delete_doctor(to_del)

    def delete_hospital_stay(self):
        print("Delete stay? (patient id)")
        to_del = input()
        self.__delete_hospital_stay(to_del)

    def __list_all_patients_doctor(self, fname, lname):
        query = """
        SELECT
        GROUP_CONCAT(patient.firstname || " " || patient.lastname) AS patients
        FROM doctor
        LEFT JOIN patient
        ON doctor.id = patient.doctor
        WHERE doctor.firstname = ? AND doctor.lastname = ?
        GROUP BY doctor.id
        """
        result = self.cursor.execute(query, (fname, lname))

        for row in result:
            print(row['patients'])

    def all_doctor_patients(self):
        print("Which doctor's patients would you like to see?")
        print("Input in format: firstname lastname")
        doctor = input()
        self.__list_all_patients_doctor(doctor.split(' ')[0],
                                        doctor.split(' ')[1])

    def __patients_by_injury(self, injury):
        query = """
        SELECT GROUP_CONCAT(patient.firstname || " " || patient.lastname) AS p
        FROM hospital_stay
        LEFT JOIN patient ON hospital_stay.patient = patient.id
        WHERE hospital_stay.injury = ?
        GROUP BY hospital_stay.injury
        """
        result = self.cursor.execute(query, (injury,))

        for row in result:
            print(row['p'])

    def list_sick_patients_by_injury(self):
        print("Patients with which sickness would you like to see?")
        sickness = input()

        self.__patients_by_injury(sickness)

    def __patients_between_dates(self, startdate1, startdate2):
        query = """
        SELECT GROUP_CONCAT(patient.firstname || " " || patient.lastname) AS p
        FROM patient
        LEFT JOIN hospital_stay ON patient.id = hospital_stay.patient
        WHERE hospital_stay.startdate >= ? AND hospital_stay.startdate <= ?
        """
        result = self.cursor.execute(query, (startdate1, startdate2))

        for row in result:
            print(row['p'])

    def list_patients_between_dates(self):
        print("Enter dates between which patients have entered the hospital:")
        print("First date: (format: yyyy-mm-dd)")
        date1 = input()
        print("Second date:")
        date2 = input()

        self.__patients_between_dates(date1, date2)


def main():
    hospital = HospitalAPI('hospital.db')
    # hospital.add_patient("Pesho", "Peshov", 12, 'M', 1)
    # hospital.add_doctor("Courtney", "Cake")
    # hospital.delete_patient()
    # hospital.update_doctor_information()
    # hospital.update_patient_information()
    # hospital.list_all_patients()
    # hospital.list_all_doctors()
    # hospital.all_doctor_patients()
    # hospital.list_sick_patients_by_injury()
    # hospital.list_patients_between_dates()


if __name__ == '__main__':
    main()
