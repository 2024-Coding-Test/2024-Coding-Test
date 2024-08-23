-- 이번에 푼거
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE ISNULL(NAME)
ORDER BY ANIMAL_ID ASC;

-- 옛날에 푼거
SELECT animal_id from animal_ins where name is null
