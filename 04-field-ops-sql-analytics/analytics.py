# © 2026 Mohammad Subhan Pasha. All Rights Reserved.
# ™ Field Ops SQL Analytics™ - Author: Mohammad Subhan Pasha
customers = [
    {"name": "Kavitha", "village": "Chittoor", "due": 0, "score": 92},
    {"name": "Ramesh", "village": "Tirupati", "due": 4500, "score": 45},
    {"name": "Venkat", "village": "Renigunta", "due": 8000, "score": 35},
]
print("© 2026 Mohammad Subhan Pasha - Field Ops Analytics")
for c in customers:
    print(c["village"], "-", c["name"], "- Due:", c["due"], "- Score:", c["score"])
print("Highest Pending:", max(customers, key=lambda x: x["due"])["name"])
