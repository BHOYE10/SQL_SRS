import duckdb

con=duckdb.connect(database="data/exercises_sql.duckdb", read_only=True)
test=con.execute("select* from memory_state").df()
print(test)







