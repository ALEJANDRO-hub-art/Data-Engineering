-- 1. Top revenue-generating routes
SELECT oa.airport_code AS origin, da.airport_code AS destination, SUM(t.ticket_price) AS route_revenue
FROM tickets t JOIN flight_instances fi ON t.flight_instance_id = fi.flight_instance_id JOIN flights f ON fi.flight_id = f.flight_id JOIN routes r ON f.route_id = r.route_id JOIN airports oa ON r.origin_airport_id = oa.airport_id JOIN airports da ON r.destination_airport_id = da.airport_id
WHERE t.ticket_status = 'Confirmed'
GROUP BY oa.airport_code, da.airport_code ORDER BY route_revenue DESC;

-- 2. Flight occupancy/load factor
SELECT fi.flight_instance_id, f.flight_number, COUNT(t.ticket_id) AS seats_booked, a.total_seats, ROUND(100.0 * COUNT(t.ticket_id) / a.total_seats, 2) AS load_factor_pct
FROM flight_instances fi JOIN flights f ON fi.flight_id = f.flight_id JOIN aircraft a ON f.aircraft_id = a.aircraft_id LEFT JOIN tickets t ON fi.flight_instance_id = t.flight_instance_id AND t.ticket_status = 'Confirmed'
GROUP BY fi.flight_instance_id, f.flight_number, a.total_seats ORDER BY load_factor_pct DESC;

-- 3. Busiest booking time by day/hour
SELECT EXTRACT(DOW FROM booking_ts) AS day_of_week, EXTRACT(HOUR FROM booking_ts) AS booking_hour, COUNT(*) AS reservations
FROM reservations GROUP BY EXTRACT(DOW FROM booking_ts), EXTRACT(HOUR FROM booking_ts) ORDER BY reservations DESC;

-- 4. Cancellation rate by route
SELECT oa.airport_code AS origin, da.airport_code AS destination, ROUND(100.0 * SUM(CASE WHEN t.ticket_status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancellation_rate_pct
FROM tickets t JOIN flight_instances fi ON t.flight_instance_id = fi.flight_instance_id JOIN flights f ON fi.flight_id = f.flight_id JOIN routes r ON f.route_id = r.route_id JOIN airports oa ON r.origin_airport_id = oa.airport_id JOIN airports da ON r.destination_airport_id = da.airport_id
GROUP BY oa.airport_code, da.airport_code ORDER BY cancellation_rate_pct DESC;

-- 5. Average ticket price by fare class
SELECT fc.class_name, AVG(t.ticket_price) AS avg_ticket_price FROM tickets t JOIN fare_classes fc ON t.fare_class_id = fc.fare_class_id GROUP BY fc.class_name;

-- 6. Monthly new customers
SELECT DATE_TRUNC('month', signup_date) AS signup_month, COUNT(*) AS new_customers FROM customers GROUP BY DATE_TRUNC('month', signup_date) ORDER BY signup_month;

-- 7. Delay analysis by route
SELECT oa.airport_code AS origin, da.airport_code AS destination, AVG(EXTRACT(EPOCH FROM (fi.actual_arrival_ts - fi.scheduled_arrival_ts))/60) AS avg_arrival_delay_minutes
FROM flight_instances fi JOIN flights f ON fi.flight_id = f.flight_id JOIN routes r ON f.route_id = r.route_id JOIN airports oa ON r.origin_airport_id = oa.airport_id JOIN airports da ON r.destination_airport_id = da.airport_id
WHERE fi.actual_arrival_ts IS NOT NULL GROUP BY oa.airport_code, da.airport_code ORDER BY avg_arrival_delay_minutes DESC;

-- 8. Repeat booking customers
SELECT c.customer_id, c.full_name, COUNT(r.reservation_id) AS reservation_count
FROM customers c JOIN reservations r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.full_name HAVING COUNT(r.reservation_id) > 1 ORDER BY reservation_count DESC;

-- 9. Revenue by booking channel
SELECT channel, SUM(total_amount) AS revenue, COUNT(*) AS reservations FROM reservations WHERE reservation_status = 'Confirmed' GROUP BY channel ORDER BY revenue DESC;

-- 10. Loyalty points usage
SELECT c.loyalty_tier, SUM(lt.points_earned) AS total_points_earned, SUM(lt.points_redeemed) AS total_points_redeemed
FROM loyalty_transactions lt JOIN customers c ON lt.customer_id = c.customer_id GROUP BY c.loyalty_tier;
