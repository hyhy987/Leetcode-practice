SELECT w_today.id
FROM Weather AS w_today
JOIN Weather AS w_yday
  ON w_today.recordDate = w_yday.recordDate + INTERVAL '1 day'
WHERE w_today.temperature > w_yday.temperature