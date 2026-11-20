# © 2026 Mohammad Subhan Pasha
def test_pending_logic():
    customers = [{"name": "Kavitha", "due": 0}, {"name": "Venkat", "due": 8000}]
    pending = [c for c in customers if c["due"] > 0]
    assert len(pending) == 1
    assert pending[0]["name"] == "Venkat"

def test_trust_score():
    score = 100 - (8000 // 500) + (2 * 3)
    assert score < 100
