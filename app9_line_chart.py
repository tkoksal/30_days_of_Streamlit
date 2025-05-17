import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.header('Further reading')

st.write('Read more about the following related Streamlit command from which [st.line_chart](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) is based on:')

st.markdown('- [st.altair_chart](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)')
