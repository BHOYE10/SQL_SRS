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


answer_str= exercise.loc[0, "exercise_name"]
with open(f"answers/{answer_str}.sql" , "r") as f:
    answer=f.read()
    solution_df=con.execute(answer).df()
st.header("enter your code ")
query = st.text_area(label="enter your request", key="user_input")

if query:
    result=con.execute(query).df()
    st.dataframe(result)
    try:
        result=result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except:
        st.write("some culombs are missing")
    n_line=solution_df.shape[0]-result.shape[0]
    if n_line!=0:
        st.write(f"result has a {n_line} line different with a solution")



tab2, tab3 = st.tabs(["tables", "solution"])
with tab2:
    exercise_table=exercise.loc[0,"tables"]
    for table in exercise_table:
        st.write(f"table: {table}")
        df_table=con.execute(f"select* from {table}").df()
        st.dataframe(df_table)


with tab3:
        st.write(answer)

con.close()
