import streamlit as st
import pandas as pd

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


st.write("Hello First Page")

@st.cache_data
def get_html_data(url):
    return pd.read_html(url)

URL = st.text_input("URL with tables", value='https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country')

tables = get_html_data(URL)

for table in tables:
    with st.expander("table"):
        st.table(table)
