import pandas as pd
import duckdb
import io
con=duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

#.....................................................................
#EXERCISES_LIST
#.....................................................................
data = {
    "theme": ["CROSS_JOIN","CROSS_JOIN"],
    "exercise_name": ["beverages_and_food", "trademark_and_sizes"],
    "tables": [["beverages", "food_items"],["trademarks", "sizes"]],
    "last_reviewed": ["1980-01-01", "1970-01-01"],
}
memory_state_df=pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state as select* from memory_state_df")

#.......................................................................
#CROSS_JOIN_EXERCISES
#.......................................................................

csv = """beverage,price
orange juice,2.5
Espresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages as select* from beverages")

csv2 = """food_item,food_price
cookie juice,2.5
chocolate,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items as select* from beverages")


df_size = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(df_size))
con.execute("CREATE TABLE IF NOT EXISTS sizes as select* from sizes")

df_trademark  = """
trademark
Nike
Asphalte
Abercrombie
Levis
"""
trademarks = pd.read_csv(io.StringIO(df_trademark ))
con.execute("CREATE TABLE IF NOT EXISTS trademarks as select* from trademarks")