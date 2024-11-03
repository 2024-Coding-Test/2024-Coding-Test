-- 현재 코드
SELECT COUNT(DISTINCT(NAME)) as count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;

-- 이전 코드
SELECT count(distinct NAME) from animal_ins where NAME is not null