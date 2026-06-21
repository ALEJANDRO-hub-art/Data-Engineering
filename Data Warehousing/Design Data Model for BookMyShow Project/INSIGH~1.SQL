-- 1. Most popular movie genres in specific locations
SELECT l.city, g.genre_name, COUNT(bi.booking_item_id) AS tickets_sold
FROM booking_items bi
JOIN bookings b ON bi.booking_id = b.booking_id
JOIN shows s ON bi.show_id = s.show_id
JOIN events e ON s.event_id = e.event_id
JOIN movies m ON e.movie_id = m.movie_id
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genres g ON mg.genre_id = g.genre_id
JOIN screens sc ON s.screen_id = sc.screen_id
JOIN theatres t ON sc.theatre_id = t.theatre_id
JOIN locations l ON t.location_id = l.location_id
WHERE e.event_type = 'Movie' AND b.booking_status = 'Confirmed'
GROUP BY l.city, g.genre_name
ORDER BY l.city, tickets_sold DESC;

-- 2. Busiest time of day/week for movie bookings
SELECT EXTRACT(DOW FROM booking_ts) AS day_of_week,
       EXTRACT(HOUR FROM booking_ts) AS booking_hour,
       COUNT(*) AS booking_count
FROM bookings
GROUP BY EXTRACT(DOW FROM booking_ts), EXTRACT(HOUR FROM booking_ts)
ORDER BY booking_count DESC;

-- 3. Percentage of movie customers who later book other events
WITH movie_users AS (
    SELECT DISTINCT b.user_id, MIN(b.booking_ts) AS first_movie_booking_ts
    FROM bookings b
    JOIN booking_items bi ON b.booking_id = bi.booking_id
    JOIN shows s ON bi.show_id = s.show_id
    JOIN events e ON s.event_id = e.event_id
    WHERE e.event_type = 'Movie' AND b.booking_status = 'Confirmed'
    GROUP BY b.user_id
), later_event_users AS (
    SELECT DISTINCT mu.user_id
    FROM movie_users mu
    JOIN bookings b ON mu.user_id = b.user_id AND b.booking_ts > mu.first_movie_booking_ts
    JOIN booking_items bi ON b.booking_id = bi.booking_id
    JOIN shows s ON bi.show_id = s.show_id
    JOIN events e ON s.event_id = e.event_id
    WHERE e.event_type <> 'Movie' AND b.booking_status = 'Confirmed'
)
SELECT ROUND(100.0 * COUNT(leu.user_id) / COUNT(mu.user_id), 2) AS pct_movie_users_booking_other_events
FROM movie_users mu
LEFT JOIN later_event_users leu ON mu.user_id = leu.user_id;

-- 4. Average number of tickets booked per transaction
SELECT AVG(ticket_count) AS avg_tickets_per_transaction
FROM (
    SELECT booking_id, COUNT(*) AS ticket_count
    FROM booking_items
    GROUP BY booking_id
) x;

-- 5. Rate of booking cancellations
SELECT ROUND(100.0 * SUM(CASE WHEN booking_status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancellation_rate_pct
FROM bookings;

-- 6. Impact of pricing on booking volume
SELECT CASE
         WHEN ticket_price < 200 THEN 'Low'
         WHEN ticket_price BETWEEN 200 AND 500 THEN 'Medium'
         ELSE 'High'
       END AS price_band,
       COUNT(*) AS tickets_sold
FROM booking_items bi
JOIN bookings b ON bi.booking_id = b.booking_id
WHERE b.booking_status = 'Confirmed'
GROUP BY price_band
ORDER BY tickets_sold DESC;

-- 7. Correlation between star cast and movie bookings
SELECT cm.cast_name, COUNT(bi.booking_item_id) AS tickets_sold
FROM cast_members cm
JOIN movie_cast mc ON cm.cast_id = mc.cast_id
JOIN movies m ON mc.movie_id = m.movie_id
JOIN events e ON m.movie_id = e.movie_id
JOIN shows s ON e.event_id = s.event_id
JOIN booking_items bi ON s.show_id = bi.show_id
JOIN bookings b ON bi.booking_id = b.booking_id
WHERE b.booking_status = 'Confirmed'
GROUP BY cm.cast_name
ORDER BY tickets_sold DESC;

-- 8. New users acquired each month
SELECT DATE_TRUNC('month', signup_date) AS signup_month, COUNT(*) AS new_users
FROM users
GROUP BY DATE_TRUNC('month', signup_date)
ORDER BY signup_month;

-- 9. Most effective marketing campaigns by acquisition and revenue
SELECT mc.campaign_name,
       COUNT(DISTINCT u.user_id) AS acquired_users,
       SUM(b.total_amount) AS revenue
FROM marketing_campaigns mc
LEFT JOIN bookings b ON mc.campaign_id = b.campaign_id
LEFT JOIN users u ON b.user_id = u.user_id
GROUP BY mc.campaign_name
ORDER BY revenue DESC NULLS LAST;

-- 10. Revenue generated from each movie theatre
SELECT t.theatre_name, l.city, SUM(bi.ticket_price) AS theatre_revenue
FROM booking_items bi
JOIN bookings b ON bi.booking_id = b.booking_id
JOIN shows s ON bi.show_id = s.show_id
JOIN screens sc ON s.screen_id = sc.screen_id
JOIN theatres t ON sc.theatre_id = t.theatre_id
JOIN locations l ON t.location_id = l.location_id
WHERE b.booking_status = 'Confirmed'
GROUP BY t.theatre_name, l.city
ORDER BY theatre_revenue DESC;
