
-- 1. Most booked doctor specialties by location
SELECT l.city, l.area, s.specialty_name, COUNT(a.appointment_id) AS appointments
FROM appointments a
JOIN doctors d ON a.doctor_id = d.doctor_id
JOIN specialties s ON d.specialty_id = s.specialty_id
JOIN clinics c ON a.clinic_id = c.clinic_id
JOIN locations l ON c.location_id = l.location_id
GROUP BY l.city, l.area, s.specialty_name
ORDER BY appointments DESC;

-- 2. Doctor utilization / appointment volume
SELECT d.full_name, COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a
    ON d.doctor_id = a.doctor_id
    AND a.appointment_status = 'Completed'
GROUP BY d.full_name
ORDER BY total_appointments DESC;

-- 3. Average consultation fee by specialty
SELECT s.specialty_name, AVG(d.consultation_fee) AS avg_consultation_fee
FROM doctors d
JOIN specialties s ON d.specialty_id = s.specialty_id
GROUP BY s.specialty_name;

-- 4. Appointment cancellation rate
SELECT ROUND(
    100.0 * SUM(CASE WHEN appointment_status = 'Cancelled' THEN 1 ELSE 0 END)
    / COUNT(*),
    2
) AS cancellation_rate_pct
FROM appointments;

-- 5. Average patient wait time
SELECT d.full_name,
       AVG(EXTRACT(EPOCH FROM (c.consultation_start_ts - a.appointment_ts))/60)
       AS avg_wait_minutes
FROM consultations c
JOIN appointments a ON c.appointment_id = a.appointment_id
JOIN doctors d ON a.doctor_id = d.doctor_id
GROUP BY d.full_name
ORDER BY avg_wait_minutes DESC;

-- 6. Revenue by doctor and clinic
SELECT d.full_name AS doctor,
       cl.clinic_name,
       SUM(p.paid_amount) AS revenue
FROM payments p
JOIN appointments a ON p.appointment_id = a.appointment_id
JOIN doctors d ON a.doctor_id = d.doctor_id
JOIN clinics cl ON a.clinic_id = cl.clinic_id
WHERE p.payment_status = 'Success'
GROUP BY d.full_name, cl.clinic_name
ORDER BY revenue DESC;

-- 7. Monthly new patient acquisition
SELECT DATE_TRUNC('month', signup_date) AS signup_month,
       COUNT(*) AS new_patients
FROM patients
GROUP BY DATE_TRUNC('month', signup_date)
ORDER BY signup_month;

-- 8. Campaign effectiveness by patients and revenue
SELECT mc.campaign_name,
       COUNT(DISTINCT a.patient_id) AS acquired_or_engaged_patients,
       SUM(p.paid_amount) AS revenue
FROM marketing_campaigns mc
LEFT JOIN appointments a
    ON mc.campaign_id = a.campaign_id
LEFT JOIN payments p
    ON a.appointment_id = p.appointment_id
    AND p.payment_status = 'Success'
GROUP BY mc.campaign_name
ORDER BY revenue DESC NULLS LAST;

-- 9. Doctor ratings
SELECT d.full_name,
       AVG(r.rating) AS avg_rating,
       COUNT(r.review_id) AS review_count
FROM doctors d
LEFT JOIN reviews r
    ON d.doctor_id = r.doctor_id
GROUP BY d.full_name
ORDER BY avg_rating DESC NULLS LAST;

-- 10. Follow-up requirement rate by specialty
SELECT s.specialty_name,
       ROUND(
           100.0 * SUM(
               CASE
                   WHEN c.follow_up_required THEN 1
                   ELSE 0
               END
           ) / COUNT(*),
           2
       ) AS follow_up_rate_pct
FROM consultations c
JOIN appointments a ON c.appointment_id = a.appointment_id
JOIN doctors d ON a.doctor_id = d.doctor_id
JOIN specialties s ON d.specialty_id = s.specialty_id
GROUP BY s.specialty_name
ORDER BY follow_up_rate_pct DESC;
