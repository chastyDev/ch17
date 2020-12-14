#modifying/adding to books database
import sqlite3
import pandas as pd
connection = sqlite3.connect('books.db')
pd.options.display.max_columns =10
pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
pd.read_sql('SELECT * From titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()
#A
pd.read_sql("""SELECT * FROM authors ORDER BY last DESC""", connection, index_col=['id'])
#B
pd.read_sql("""SELECT * FROM titles ORDER by title ASC FROM """, connection, index_col=['id'])
#C
pd.read_sql("""SELECT first, last, title, copyright, isbn FROM authors INNER JOIN author_titles ORDER BY title""", connection, index_col=['id'])
#D
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Chris','Hasty')""")
#E
cursor = cursor.execute("""INSERT INTO author_ISBN (title) VALUES ('Moby Dick')""")
cursor = cursor.execute(("""INSERT INTO titles (title) VALUES ('Moby Dick')"""))