import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='gaurav', password='S@njose1990',
                              host='localhost',
                              database='sakila')

df = pd.read_sql_query("select distinct f.title, f.description, a.first_name, a.last_name "
                       "from sakila.actor a inner join sakila.film_actor fa on a.actor_id = fa.actor_id "
                       "join sakila.film as f on f.film_id = fa.film_id "
                       " where title LIKE 'zo%'", cnx)
print(df)
cnx.close()
