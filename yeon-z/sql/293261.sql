-- 물고기 종류 별 대어 찾기
SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO I
JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
WHERE (I.FISH_TYPE, LENGTH) IN
    (SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE)
ORDER BY ID