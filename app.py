import streamlit as st
import duckdb

#answer = """select*
#          from beverages
 #         cross join food_items
  #         """
#solution = duckdb.query(answer).df()

con=duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "what would you like to review ?",
        ["CROSS JOIN", "GROUP BY", "WINDOW FUNCTION"],
        index=None,
        placeholder="Select a theme ...",
    )
    st.write("you selected :", theme)
    exercise=con.execute(f"select* from memory_state where theme='{theme}'").df()
    st.write(exercise)

st.header("enter your code ")

query = st.text_area(label="enter your request", key="user_input")

#if query:
#resultat = duckdb.query(query).df()
#st.dataframe(resultat)

#, tab3 = st.tabs(["tables", "solution"])

# tab2:
#st.write("table : beverages")
#st.dataframe(beverages)
#st.write("table : food_items")
#st.dataframe(food_items)
#st.write("expected :")
#st.dataframe(solution)

# tab3:
#st.write(answer)
