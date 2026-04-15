-- Total revenue per customer
SELECT CustomerID,
       SUM(Quantity * UnitPrice) AS total_spent
FROM data
GROUP BY CustomerID;

-- Order frequency
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS total_orders
FROM data
GROUP BY CustomerID;

-- Average order value
SELECT CustomerID,
       SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo) AS avg_order_value
FROM data
GROUP BY CustomerID;