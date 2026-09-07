from app import create_app
from app.db import get_db

app = create_app()
with app.app_context():
    db = get_db()
    sample = [
        ("CSE001","Aarav Sharma","B.Tech CSE","A"),
        ("CSE002","Ananya Rao","B.Tech CSE","A"),
        ("CSE003","Kabir Kumar","B.Tech CSE","A"),
        ("CSE004","Diya Nair","B.Tech CSE","A"),
        ("CSE005","Rohan Das","B.Tech CSE","A"),
    ]
    db.executemany(
        "INSERT OR IGNORE INTO students(roll_number,name,class_name,section) VALUES(?,?,?,?)",
        sample
    )
    db.commit()
    print("Sample students added.")
