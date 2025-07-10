import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 

# Create / Connect to database file (create if not exists)
conn = sqlite3.connect("Week3/Students.db")
cur = conn.cursor()

# Drop old table (if exists)
cur.execute("DROP TABLE IF EXISTS Students")

# Create a Table
cur.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK(age >= 0),
    city TEXT DEFAULT 'Unknown'
)    
''')

# Insert some data
data = [
    (1, 'Satyam', 22, 'Lucknow'),
    (2, 'Neha', 20, 'Kanpur'),
    (3, 'Ravi', 19, 'Varanasi'),
    (4, 'Amit', 16, 'Delhi'),
    (5, 'Pooja', 26, 'Lucknow'),
    (6, 'Niharika', 12, 'Gorakhpur'),
    (7, 'Asish', 18, 'Lucknow'),
    (8, 'Arun', 23, 'Hata'),
    (9, 'Raj', 22, 'Hata'),
    (10, 'Saurabh', 21, 'Hata')
]
cur.executemany('INSERT INTO students VALUES (?, ?, ?, ?)', data)
conn.commit()

# All Students
df = pd.read_sql_query("SELECT * FROM Students", conn)
print(df)

# Adults only (Age >= 18)
adults = pd.read_sql_query("SELECT * FROM Students WHERE age >=18", conn)
print("\n Adults Only")
print(adults)

# Average age By City
avg_age = pd.read_sql_query("SELECT city, AVG(age) as avg_age FROM Students GROUP BY city", conn)

# Count by City
count_df = pd.read_sql_query("SELECT city, COUNT(*) as count FROM Students GROUP BY city", conn)

# Visualization 
# 1 Bar Chart - Students per City
count_df.plot(kind = 'bar', x = 'city', y = 'count', title = 'Number of Students per City')
plt.tight_layout()
plt.show

# 2 Pie Chart - City Distribution
count_df.set_index('city').plot.pie(y ='count', autopct='%1.1f%%', title = 'City-wise Student Share')
plt.ylabel("")
plt.tight_layout()
plt.show() 
