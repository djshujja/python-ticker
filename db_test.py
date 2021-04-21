import sqlite3
import time

conn = sqlite3.connect('test_db.db')

c = conn.cursor()

# c.execute("""CREATE TABLE tickers (
#     symbol text,
#     watchlist_count integer,
#     timestamp real
# )""")

# 
# c.execute("INSERT INTO tickers VALUES('FB','12345')")
# # ticker="FB"
# # watchlist_count = 1234.567
# # query = f"INSERT INTO tickers VALUES('{ticker}', '{watchlist_count}', '{time.time()}')"

# # c.execute(query)
# conn.commit()

# c.execute("SELECT * FROM tickers")
c.execute("DELETE FROM tickers")

# print(c.fetchall())

conn.commit()

conn.close()
