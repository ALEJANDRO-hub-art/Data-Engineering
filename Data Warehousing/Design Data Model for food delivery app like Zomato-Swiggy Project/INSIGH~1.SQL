-- 1. Most popular restaurants in specific locations
SELECT l.city, l.area, r.restaurant_name, COUNT(o.order_id) AS order_count
FROM orders o JOIN restaurants r ON o.restaurant_id = r.restaurant_id JOIN locations l ON r.location_id = l.location_id
WHERE o.order_status = 'Delivered'
GROUP BY l.city, l.area, r.restaurant_name
ORDER BY l.city, l.area, order_count DESC;

-- 2. Busiest times of day/week for food orders
SELECT EXTRACT(DOW FROM order_ts) AS day_of_week, EXTRACT(HOUR FROM order_ts) AS order_hour, COUNT(*) AS orders
FROM orders GROUP BY EXTRACT(DOW FROM order_ts), EXTRACT(HOUR FROM order_ts) ORDER BY orders DESC;

-- 3. Average order value for each customer
SELECT c.customer_id, c.full_name, AVG(o.total_amount) AS avg_order_value
FROM customers c JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.customer_id, c.full_name;

-- 4. Average delivery time for each restaurant and delivery person
SELECT r.restaurant_name, dp.full_name AS delivery_person, AVG(EXTRACT(EPOCH FROM (d.delivered_ts - d.assigned_ts))/60) AS avg_delivery_minutes
FROM deliveries d JOIN orders o ON d.order_id = o.order_id JOIN restaurants r ON o.restaurant_id = r.restaurant_id JOIN delivery_personnel dp ON d.delivery_person_id = dp.delivery_person_id
WHERE d.delivery_status = 'Delivered'
GROUP BY r.restaurant_name, dp.full_name;

-- 5. Most commonly ordered cuisines
SELECT c.cuisine_name, SUM(oi.quantity) AS items_ordered
FROM order_items oi JOIN menu_items mi ON oi.menu_item_id = mi.menu_item_id JOIN cuisines c ON mi.cuisine_id = c.cuisine_id JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'Delivered'
GROUP BY c.cuisine_name ORDER BY items_ordered DESC;

-- 6. Rate of order cancellations
SELECT ROUND(100.0 * SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancellation_rate_pct FROM orders;

-- 7. Impact of pricing and discounts on order volume
SELECT CASE WHEN subtotal < 300 THEN 'Low' WHEN subtotal BETWEEN 300 AND 800 THEN 'Medium' ELSE 'High' END AS price_band,
       CASE WHEN discount_amount > 0 THEN 'Discounted' ELSE 'No Discount' END AS discount_flag,
       COUNT(*) AS order_volume
FROM orders GROUP BY price_band, discount_flag ORDER BY order_volume DESC;

-- 8. Revenue generated from each restaurant
SELECT r.restaurant_name, SUM(o.total_amount) AS revenue
FROM restaurants r JOIN orders o ON r.restaurant_id = o.restaurant_id
WHERE o.order_status = 'Delivered'
GROUP BY r.restaurant_name ORDER BY revenue DESC;

-- 9. Number of new customers acquired each month
SELECT DATE_TRUNC('month', signup_date) AS signup_month, COUNT(*) AS new_customers FROM customers GROUP BY DATE_TRUNC('month', signup_date) ORDER BY signup_month;

-- 10. Most effective marketing campaigns by acquisition/revenue
SELECT mc.campaign_name, COUNT(DISTINCT o.customer_id) AS customers, SUM(o.total_amount) AS revenue
FROM marketing_campaigns mc LEFT JOIN orders o ON mc.campaign_id = o.campaign_id
GROUP BY mc.campaign_name ORDER BY revenue DESC NULLS LAST;
