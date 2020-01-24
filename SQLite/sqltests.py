import sqlite3
from sqlite3 import Error
from data import User
 
conn = sqlite3.connect('./db/test-table.db')

c = conn.cursor()

# c.execute("""CREATE TABLE user_mood (
#     happy integer,
#     sad integer,
#     tired integer,
#     alert integer,
#     timestamp text
# )""")

hour_1 = User(15, 5, 10, 15, '12:28:32')
hour_2 = User(10, 5, 15, 10, '12:33:32')
hour_3 = User(5, 10, 15, 5, '12:38:32')

# c.execute("INSERT INTO user_mood VALUES (?, ?, ?, ?, ?)", (hour_1.happy, hour_1.sad, hour_1.tired, hour_1.alert, hour_1.timestamp))

# conn.commit()

# c.execute("INSERT INTO user_mood VALUES (:happy, :sad, :tired, :alert, :timestamp)", 
# {'happy': hour_2.happy, 'sad': hour_2.sad, 'tired': hour_2.tired, 'alert': hour_2.alert, 'timestamp': hour_2.timestamp})

# conn.commit()

# c.execute("INSERT INTO user_mood VALUES (?, ?, ?, ?, ?)", (hour_3.happy, hour_3.sad, hour_3.tired, hour_3.alert, hour_3.timestamp))

# conn.commit()

#when using the question mark notion, comma is necessary even with only one value
c.execute("SELECT * FROM user_mood WHERE happy=?", (15,))

print(c.fetchall())

c.execute("SELECT * FROM user_mood WHERE happy=:happy", {'happy': 10})

print(c.fetchall())

conn.commit()

conn.close()