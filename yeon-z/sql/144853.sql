-- 최신 풀이
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE)=2021 AND CATEGORY='인문'

-- 이전 풀이
SELECT BOOK_ID, PUBLISHED_DATE
FROM (
    SELECT BOOK_ID, date_format(PUBLISHED_DATE, '20%y-%m-%d') as PUBLISHED_DATE
    FROM BOOK
    WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = '인문'
    ORDER BY PUBLISHED_DATE
) sub