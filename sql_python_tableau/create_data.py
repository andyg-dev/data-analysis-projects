import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect("complete_analytics_project.db")
cursor = conn.cursor()

# Seed data
names = ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
cities = ['Atlanta', 'Austin', 'Dallas', 'Chicago', 'Denver', 'Miami', 'Seattle']
bus_types = ['Mini Bus', 'Coach Bus', 'School Bus']

# --- 1. Customers ---
customers = []
for i in range(1, 51):
    name = random.choice(names)
    email = f"user{i}@gmail.com"
    signup_date = datetime.now() - timedelta(days=random.randint(30, 1000))
    customers.append((i, name, email, signup_date.date()))

cursor.executemany("INSERT INTO Customers VALUES (?, ?, ?, ?)", customers)

# --- 2. Operators ---
operators = []
for i in range(1, 11):
    name = f"Operator {i}"
    city = random.choice(cities)
    operators.append((i, name, city))

cursor.executemany("INSERT INTO Operators VALUES (?, ?, ?)", operators)

# --- 3. Buses ---
buses = []
for i in range(1, 31):
    operator_id = random.randint(1, 10)
    capacity = random.choice([20, 30, 40, 50])
    bus_type = random.choice(bus_types)
    buses.append((i, operator_id, capacity, bus_type))

cursor.executemany("INSERT INTO Buses VALUES (?, ?, ?, ?)", buses)

# --- 4. Bookings & 5. Trips ---
bookings = []
trips = []

for i in range(1, 101):
    customer_id = random.randint(1, 50)
    bus_id = random.randint(1, 30)
    booking_date = datetime.now() - timedelta(days=random.randint(1, 365))
    trip_date = booking_date + timedelta(days=random.randint(1, 14))
    price = round(random.uniform(500, 3000), 2)
    status = random.choices(['Completed', 'Cancelled', 'Pending'], weights=[0.6, 0.2, 0.2])[0]

    bookings.append((i, customer_id, bus_id, booking_date.date(), trip_date.date(), price, status))

    origin = random.choice(cities)
    destination = random.choice([c for c in cities if c != origin])
    distance = round(random.uniform(100, 2000), 2)
    duration = round(distance / random.uniform(40, 90), 2)

    trips.append((i, i, origin, destination, distance, duration))

cursor.executemany("INSERT INTO Bookings VALUES (?, ?, ?, ?, ?, ?, ?)", bookings)
cursor.executemany("INSERT INTO Trips VALUES (?, ?, ?, ?, ?, ?)", trips)

# Commit and close
conn.commit()
conn.close()
print("✅ Database populated with sample data.")
