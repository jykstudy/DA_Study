SELECT D.DEPT_ID AS DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT D JOIN HR_EMPLOYEES E USING (DEPT_ID)
GROUP BY 1,2 ORDER BY 3 DESC