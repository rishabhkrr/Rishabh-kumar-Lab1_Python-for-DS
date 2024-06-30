use e_commerce;

SELECT CUS_GENDER, COUNT(*) AS num_customers
FROM customer c
JOIN orders o ON c.CUS_ID = o.CUS_ID
WHERE o.ORD_AMOUNT >= 3000
GROUP BY CUS_GENDER;

SELECT o.ORD_ID, p.PRO_NAME
FROM orders o
JOIN product_details pd ON o.PROD_ID = pd.PROD_ID
JOIN product p ON pd.PRO_ID = p.PRO_ID
WHERE o.CUS_ID = 2;

SELECT s.*
FROM supplier s
JOIN product_details pd ON s.SUPP_ID = pd.SUPP_ID
GROUP BY s.SUPP_ID
HAVING COUNT(pd.PROD_ID) > 1;

SELECT c.CAT_NAME
FROM category c
JOIN product p ON c.CAT_ID = p.CAT_ID
JOIN product_details pd ON p.PRO_ID = pd.PRO_ID
JOIN orders o ON pd.PROD_ID = o.PROD_ID
WHERE o.ORD_AMOUNT = (SELECT MIN(ORD_AMOUNT) FROM orders);

SELECT p.PRO_ID, p.PRO_NAME
FROM product p
JOIN product_details pd ON p.PRO_ID = pd.PRO_ID
JOIN orders o ON pd.PROD_ID = o.PROD_ID
WHERE o.ORD_DATE > '2021-10-05';



