import streamlit as st
import duckdb
import os
import logging

if "data" not in os.listdir():
    print("creating folder data")
    logging.error(os.listdir())
    os.mkdir("data")
if "exercises_sql.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())



con=duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "what would you like to review ?",
        ["CROSS_JOIN", "GROUP_BY","WINDOWS_FUNCTION" ],
        index=None,
        placeholder="Select a theme ...",
    )
    st.write("you selected :", theme)

    exercise=con.execute(f"select* from memory_state where theme='{theme}'").df().sort_values("last_reviewed").reset_index()
    st.write(exercise)

st.header("enter your code ")

query = st.text_area(label="enter your request", key="user_input")

if query:
    result=con.execute(query).df()
    st.dataframe(result)


tab2, tab3 = st.tabs(["tables", "solution"])
with tab2:
    exercise_table=exercise.loc[0,"tables"]
    for table in exercise_table:
        st.write(f"table: {table}")
        df_table=con.execute(f"select* from {table}").df()
        st.dataframe(df_table)
        #st.write("table : beverages")
        #st.dataframe(beverages)
#st.write("table : food_items")
#st.dataframe(food_items)
#st.write("expected :")
#st.dataframe(solution)

with tab3:
    answer_str= exercise.loc[0, "exercise_name"]
    with open(f"answers/{answer_str}.sql" , "r") as f:
        answer=f.read()
        st.write(answer)

con.close()
