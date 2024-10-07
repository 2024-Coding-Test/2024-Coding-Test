-- 현재 코드
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') as 'NAME' , SEX_UPON_INTAKE
FROM ANIMAL_INS;

-- 이전코드
SELECT animal_type, ifnull(name,"No name"), sex_upon_intake
from animal_ins