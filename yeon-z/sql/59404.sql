-- 여러 기준으로 정렬하기
-- 현재 코드
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;

-- 이전 코드
SELECT animal_id, name, datetime from animal_ins order by name asc, datetime desc