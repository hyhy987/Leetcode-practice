-- Write your PostgreSQL query statement below
SELECT DISTINCT v.author_id as id
FROM Views v
WHERE author_id = viewer_id
ORDER BY id ASC