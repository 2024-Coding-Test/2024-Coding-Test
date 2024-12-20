SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM REST_REVIEW R
JOIN MEMBER_PROFILE P
ON R.MEMBER_ID=P.MEMBER_ID
WHERE R.MEMBER_ID IN (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(*) = (
        SELECT COUNT(*) as REVIEW_COUNT
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY REVIEW_COUNT DESC
        LIMIT 1
    )
)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT;