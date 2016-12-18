--SELECT GROUP_CONCAT(patient.firstname || " " || patient.lastname)
--FROM patient
--JOIN hospital_stay ON patient.id = hospital_stay.patient
--WHERE hospital_stay.startdate >= "2016-10-10" AND hospital_stay.startdate <= "2016-10-12";

--SELECT GROUP_CONCAT(patient.firstname || " " || patient.lastname), hospital_stay.injury
--FROM patient
--LEFT JOIN hospital_stay ON patient.id = hospital_stay.patient
--GROUP BY hospital_stay.injury;

SELECT DISTINCT doctor.firstname, doctor.lastname, GROUP_CONCAT (hospital_stay.injury)
FROM doctor
JOIN patient ON doctor.id= patient.doctor
JOIN hospital_stay ON hospital_stay.patient = patient.id
GROUP BY doctor.id;

DELETE
FROM user
WHERE id > 7;

DELETE
FROM doctor
WHERE doctor.id =11;

SELECT user.username, doctor.academic_title
FROM doctor
LEFT JOIN user
ON doctor.id = user.id;

DELETE FROM user WHERE id = 14;
DELETE FROM sqlite_sequence WHERE name = 'user';

DELETE FROM patient WHERE id = 14;

SELECT doctor.id, user.username, doctor.academic_title
FROM doctor
JOIN user ON doctor.id = user.id
LIMIT 1 OFFSET 0;

UPDATE user
SET is_active = 0
WHERE id = 8;

SELECT id
FROM user
WHERE username="Pesho";

SELECT GROUP_CONCAT(user.username)
FROM user
JOIN patient on patient.id = user.id
WHERE patient.doctor_id = 3;

SELECT doctor.id
FROM doctor
JOIN user ON doctor.id = user.id
WHERE user.username = "Dr. Pavlina Zdravkova";

SELECT user.username, hospital_stay.room, hospital_stay.startdate, hospital_stay.enddate
FROM hospital_stay
JOIN patient ON patient.id = hospital_stay.patient_id
JOIN user ON patient.id = user.id
WHERE patient.doctor_id = 3;