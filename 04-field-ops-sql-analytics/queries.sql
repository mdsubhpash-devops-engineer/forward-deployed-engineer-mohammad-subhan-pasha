-- © 2026 Mohammad Subhan Pasha. All Rights Reserved.
-- ™ Field Ops SQL Analytics™ - Author: Mohammad Subhan Pasha
SELECT * FROM customers;
SELECT name FROM customers WHERE score > 80;
SELECT name, due FROM customers ORDER BY due DESC;
SELECT village, COUNT(*) as total_customers FROM customers GROUP BY village;
SELECT c.name, l.amount FROM customers c JOIN loans l ON c.id = l.customer_id;
