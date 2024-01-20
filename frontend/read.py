import pandas as pd
import streamlit as st
from database import view_all_data,getcolumns

def read():
    list_of_tables=['Employee','Department','Dept_Locations','Project','Works_on','Dependents','Pay_Roll','Pay_Grade']
    choice=st.selectbox("Select Table to View Data", list_of_tables)
    result = view_all_data(choice)
    cols = [i[0] for i in getcolumns(choice)]
    df = pd.DataFrame(result,columns=cols)
    if st.button("View"):
        st.table(df)