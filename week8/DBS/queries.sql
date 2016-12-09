SELECT movie.title, movie.year, movie.studioname, studio.name
FROM movie, studio
WHERE movie.length > 120 AND movie.studioname = studio.name;

SELECT movie.studioname, starsin.starname
FROM starsin, movie
WHERE starsin.movietitle = movie.title
ORDER BY movie.studioname;

SELECT DISTINCT movieexec.name
FROM movieexec, movie, starsin
WHERE movie.producer = movieexec.CERT AND movie.title = starsin.movietitle
AND starsin.starname = "Harrison Ford";

SELECT moviestar.name
FROM moviestar, movie, starsin
WHERE moviestar.gender = "F"
AND movie.title = starsin.movietitle
AND moviestar.name = starsin.starname
AND movie.studioname = "MGM";

SELECT movieexec.name, movie.title
FROM movieexec, movie
WHERE movieexec.CERT = movie.producer
AND movieexec.name = (SELECT movieexec.name 
		       FROM movieexec, movie
		       WHERE movie.producer = movieexec.CERT
		       AND movie.title = "Star Wars");
SELECT moviestar.name
FROM moviestar
WHERE moviestar.name NOT IN (SELECT starsin.starname
			      FROM starsin);
