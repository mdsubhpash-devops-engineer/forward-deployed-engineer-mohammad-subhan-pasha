# © 2026 Mohammad Subhan Pasha. All Rights Reserved.
# ™ SubhanOps™ - Author: Mohammad Subhan Pasha
from fastapi import FastAPI
app = FastAPI(title="Recovery Tracker API - Mohammad Subhan Pasha")

customers = [
    {"id": 1, "name": "Kavitha", "village": "Chittoor", "due": 0, "score": 92},
    {"id": 2, "name": "Ramesh", "village": "Tirupati", "due": 4500, "score": 45},
    {"id": 3, "name": "Venkat", "village": "Renigunta", "due": 8000, "score": 35},
]

@app.get("/")
def home():
    return {"message": "Recovery Tracker API by Mohammad Subhan Pasha", "copyright": "© 2026 Mohammad Subhan Pasha"}

@app.get("/customers")
def get_all():
    return customers

@app.get("/pending")
def get_pending():
    return [c for c in customers if c["due"] > 0]

@app.get("/customer/{id}")
def get_one(id: int):
    for c in customers:
        if c["id"] == id:
            return c
    return {"error": "Not found"}
