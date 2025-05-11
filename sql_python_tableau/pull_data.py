import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect("charterup_analytics_project.db")

# Pull data from Bookings joined with Operators (for cancellation analysis)
query1 = """
SELECT o.name AS operator, b.status
FROM Bookings b
JOIN Buses bu ON b.bus_id = bu.bus_id
JOIN Operators o ON bu.operator_id = o.operator_id;
"""
df1 = pd.read_sql_query(query1, conn)
df1.to_csv("cancellations_by_operator.csv", index=False)

# Pull data for customer segments
query2 = """
SELECT c.customer_id,
       COUNT(b.booking_id) AS num_bookings,
       SUM(b.price) AS total_spent,
       AVG(t.distance) AS avg_distance
FROM Customers c
JOIN Bookings b ON c.customer_id = b.customer_id
JOIN Trips t ON b.booking_id = t.booking_id
WHERE b.status = 'Completed'
GROUP BY c.customer_id;
"""
df2 = pd.read_sql_query(query2, conn)
df2.to_csv("customer_metrics.csv", index=False)

conn.close()
