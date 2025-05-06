import pandas as pd
from datetime import datetime

# Sample data for customer feedback
data = [
    {'CustomerID': '001', 'Feedback': 'Great service, very helpful!', 'Timestamp': '2025-05-06T10:05:00', 'AgentID': '101'},
    {'CustomerID': '002', 'Feedback': 'The wait was too long, not happy.', 'Timestamp': '2025-05-06T10:15:00', 'AgentID': '102'},
    {'CustomerID': '003', 'Feedback': 'Good experience overall, would recommend.', 'Timestamp': '2025-05-06T10:20:00', 'AgentID': '101'},
    {'CustomerID': '004', 'Feedback': 'I had trouble with the product, not satisfied.', 'Timestamp': '2025-05-06T10:30:00', 'AgentID': '103'},
    {'CustomerID': '005', 'Feedback': 'The service was excellent, very fast.', 'Timestamp': '2025-05-06T10:35:00', 'AgentID': '101'}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv('customer_feedback.csv', index=False)

print("CSV file created successfully.")