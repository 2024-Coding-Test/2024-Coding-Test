-- 특정 형질을 가지는 대장균 찾기
SELECT
    COUNT(ID) COUNT
FROM
    ECOLI_DATA
WHERE
    GENOTYPE & 5         -- 0101
    AND NOT GENOTYPE & 2 -- 0010