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
WHERE id > 3;