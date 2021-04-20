import sqlite3


def create_db(name):
    conn = sqlite3.connect(f'{name}.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE tickers (
        symbol text,
        watchlist_count integer,
        timestamp real
    )""")
    conn.commit()
    conn.close()
    print(f"{name}.db has been created!")


create_db("test_db")