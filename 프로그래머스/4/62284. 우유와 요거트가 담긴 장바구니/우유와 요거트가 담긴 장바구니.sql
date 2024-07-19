SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY 1 HAVING COUNT(DISTINCT NAME)>=2
ORDER BY 1