import streamlit as st
import pandas as pd
import altair as alt

st.markdown("# Hello World")

"This also worksee"

# df_simple = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

df =  pd.read_csv('/Users/oo/kse-streamlit-2024-06/hromada_budget_2020_2022 (1).csv')

with st.expander("сирий датафрейм"):
    st.write("dataframe preview")
    df

ST_OBLAST = st.sidebar.selectbox("Оберіть Область", df['oblast_name'].unique())
ST_COLOR = st.sidebar.selectbox("Оберіть Розбивку", ['year', 'hromada_name'])
ST_METRIC = st.sidebar.selectbox("Оберіть метрику", [x for x in df.columns if "income" in x])
ST_METRIC_2 = st.sidebar.selectbox("Оберіть метрику 2", [x for x in df.columns if "income" in x])
ST_SPLIT_BY = st.sidebar.selectbox("Оберіть Розбивку", ['hromada_name', 'raion_name', 'oblast_name'])
df_to_plot = df[df["oblast_name"]==ST_OBLAST]

ST_TITLE = st.sidebar.text_input("Назва графіку", "Графік")

ST_WIDTH, ST_HEIGHT = st.sidebar.columns(2)
ST_WIDTH =  ST_WIDTH.slider("Ширина графіку", min_value=200, max_value=1000, value=700)
ST_HEIGHT =  ST_HEIGHT.slider("Висота графіку", min_value=200, max_value=1000, value=350)
tab1, tab2 = st.tabs(["Стовпчата Діаграма", "Scatter Plot"])

with tab1:
    chart_income_by_oblast = alt.Chart(df_to_plot).mark_bar().encode(
        x=f'sum({ST_METRIC})',
        y='raion_name',
        color=ST_COLOR
    ).properties(width=ST_WIDTH, height=ST_HEIGHT, title=ST_TITLE).interactive()

    st.altair_chart(chart_income_by_oblast)

with tab2:
    chart_scatter_plot = alt.Chart(df_to_plot).mark_point().encode(
        x=f'sum({ST_METRIC})',
        y=f'sum({ST_METRIC_2})',
        color=ST_SPLIT_BY
    ).properties(width=ST_WIDTH, height=ST_HEIGHT, title=ST_TITLE).interactive()
    st.altair_chart(chart_scatter_plot)