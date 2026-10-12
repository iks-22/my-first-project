import os

import psycopg2
from flask import Flask

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppass"),
    )


@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits (id INT PRIMARY KEY, count INT NOT NULL)"
    )
    cur.execute(
        "INSERT INTO visits (id, count) VALUES (1, 1) "
        "ON CONFLICT (id) DO UPDATE SET count = visits.count + 1 "
        "RETURNING count"
    )
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return f"Hello DevOps. Visits: {count}"


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)