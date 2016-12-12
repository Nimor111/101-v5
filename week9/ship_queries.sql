SELECT sh.name, sh.launched, cl.numguns, cl.country
FROM ships AS sh
JOIN classes AS cl ON sh.class = cl.class;

SELECT sh.name, sh.launched, cl.numguns, cl.country
FROM classes AS cl
LEFT JOIN ships AS sh ON sh.class = cl.class
WHERE sh.name = cl.class;

SELECT DISTINCT sh.name
FROM ships AS sh
JOIN outcomes AS o ON o.ship = sh.name
JOIN battles AS b ON o.battle = b.name;
WHERE b.date LIKE "%1942%";

SELECT sh.name, cl.country
FROM classes AS cl
JOIN ( SELECT sh.name
	    FROM ships AS sh
	    JOIN outcomes as o ON o.ship = sh.name
	    JOIN battles as b ON b.name = o.battle
	    WHERE b.name = NULL )
ON sh.name = cl.country;


SELECT DISTINCT classes.country, ships.name
FROM classes
LEFT JOIN ships ON ships.class = classes.class
LEFT JOIN outcomes ON outcomes.ship = ships.name
WHERE outcomes.battle IS NULL;