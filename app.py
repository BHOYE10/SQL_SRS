import streamlit as st
import pandas as pd
import duckdb

st.write("""#SQL_SRS
         space repetition systeme SQL practice """)

st.write("hello world")
option=st.selectbox("what would you like to review ?", ["JOIN","GROUP BY" ,"WINDOW FUNCTION"],
                     index=None ,
                     placeholder="Select a theme ...",)

st.write("you selected :" ,option)
data={"a" : [1 ,2 ,3], "b" : [3 ,4 ,5]}
df=pd.DataFrame(data)

tab1,tab2,tab3=st.tabs(["cat","dog","owl"])

with tab1:
    #st.header("a cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg" , width=200)
    request_sql=st.text_area(label="enter your input")
    request=duckdb.query(request_sql).df()
    st.write(f"this is your request : {request_sql}")
    st.dataframe(request)


with tab2:
    st.header("a lyon")
    st.image("https://static.streamlit.io/examples/dog.jpg" , width=200)
with tab3:
    st.header("a owl")
    st.image("https://static.streamlit.io/examples/owl.jpg" , width=200)
