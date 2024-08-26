SELECT  ID
        ,EMAIL
        ,FIRST_NAME
        ,LAST_NAME
FROM DEVELOPERS D, SKILLCODES S
WHERE 1 = 1
    AND (SKILL_CODE & S.CODE) > 0
    AND NAME IN ('Python', 'C#')
ORDER BY ID;