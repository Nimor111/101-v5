-- QUERY 2--
SELECT products.productname , products.unitprice
FROM products
ORDER BY products.unitprice DESC
LIMIT 10;

-- QUERY 3 --
SELECT products.categoryid, COUNT (products.categoryid)
FROM products
GROUP BY products.categoryid;

--QUERY 4--
SELECT DISTINCT shippers.companyname
FROM orders, shippers
WHERE orders.shippeddate > 9/26/1996;