SELECT address
FROM studio
WHERE name = "MGM";

SELECT birthdate
FROM moviestar 
WHERE name = "Sandra Bullock";

SELECT name
FROM movieexec
WHERE networth > 1000000;

SELECT name
FROM moviestar
WHERE gender = "M" OR address = "Prefect Rd.";

INSERT INTO moviestar
VALUES("Zahari Baharov", "Pesho street", "M", "1978-10-11");

DELETE FROM studio
WHERE address LIKE "%5%";

UPDATE movie
SET studioname = "Fox"
WHERE title LIKE "%star%";

SELECT movie.title, studio.name
FROM movie,studio
WHERE movie.studioname = studio.name
ORDER BY movie.title;

SELECT moviestar.name
FROM moviestar, starsin
WHERE starsin.starname=moviestar.name
AND moviestar.gender = "M"
AND starsin.movietitle="Terms of Endearment";

SELECT moviestar.name
FROM starsin, moviestar, movie
WHERE starsin.movieyear = 1995 AND movie.title = starsin.movietitle
AND moviestar.name = starsin.starname AND movie.studioname = "MGM";

SELECT DISTINCT movieexec.name
FROM movieexec, movie
WHERE movieexec.cert = movie.producer AND movie.studioname="MGM";

SELECT movie.title
FROM movie
WHERE movie.length > ( SELECT movie.title
					   FROM movie
					   WHERE movie.title = "Gone with the wind" );

SELECT movie.title
FROM movieexec, movie
WHERE movie.producer = movieexec.CERT AND movieexec.networth > ( SELECT movieexec.networth
															   FROM movieexec
															   WHERE movieexec.name = "Merv Griffin")



