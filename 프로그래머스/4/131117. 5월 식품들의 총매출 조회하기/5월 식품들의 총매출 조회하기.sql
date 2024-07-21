SELECT P.PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT*PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O USING (PRODUCT_ID)
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY 1,2 ORDER BY 3 DESC, 1;