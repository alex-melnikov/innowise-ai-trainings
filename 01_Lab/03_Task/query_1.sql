SELECT SUM(amount) as total_sales
FROM orders
WHERE order_date >= '2024-03-01' AND order_date <= '2024-03-31'; 