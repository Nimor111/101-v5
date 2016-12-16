SELECT AVG(speed)
FROM pc;

SELECT AVG(laptop.screen), product.maker
FROM laptop
JOIN product ON product.model = laptop.model
GROUP BY product.maker;

SELECT AVG(laptop.speed)
FROM laptop
WHERE laptop.price > 1000;

SELECT AVG(price) 
FROM pc
GROUP BY hd;

SELECT AVG(pc.price)
FROM pc
GROUP BY pc.speed 
HAVING pc.speed > 500;

SELECT AVG(pc.price)
FROM pc
JOIN product ON product.model = pc.model
GROUP BY product.maker
HAVING product.maker = "A";

SELECT product.maker, (AVG(pc.price) + AVG(laptop.price)) / 2
FROM product
LEFT JOIN laptop ON laptop.model = product.model
LEFT JOIN pc ON pc.model = product.model
--WHERE product.maker = "B"
GROUP BY product.maker;

SELECT product.maker, product.model
FROM product
LEFT JOIN pc ON product.model = pc.model
GROUP BY product.maker
HAVING COUNT(pc.model) >= 3;

SELECT product.maker, MAX(pc.price)
FROM product
JOIN pc ON product.model = pc.model
GROUP BY product.maker
HAVING pc.price = (SELECT MAX(pc.price)
				   FROM pc);
				   
SELECT product.maker, AVG(pc.hd)
FROM pc
LEFT JOIN product ON product.model = pc.model
WHERE product.maker IN ( SELECT product.maker
			 FROM product
			 JOIN printer ON product.model = printer.model)
GROUP BY product.maker;

SELECT product.maker, AVG(pc.hd)
FROM pc
JOIN product ON product.model = pc.model
JOIN printer ON printer.model = product.model
WHERE printer.code IS NOT NULL
GROUP BY product.maker;

SELECT COUNT(type IS "laptop"), COUNT(type IS "printer"), maker
FROM product
GROUP BY maker;
