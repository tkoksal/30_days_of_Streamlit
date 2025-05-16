import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# Example 4
st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

# Example 5

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c']
)

st.write(c)

st.header('Further reading')

st.write(
    'In addition to [st.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write), you can explore '
    'the other ways of displaying text:'
)
st.markdown(
    """
    - [st.markdown](https://docs.streamlit.io/library/api-reference/text/st.markdown)
    - [st.header](https://docs.streamlit.io/library/api-reference/text/st.header)
    - [st.subheader](https://docs.streamlit.io/library/api-reference/text/st.subheader)
    - [st.caption](https://docs.streamlit.io/library/api-reference/text/st.caption)
    - [st.text](https://docs.streamlit.io/library/api-reference/text/st.text)
    - [st.latex](https://docs.streamlit.io/library/api-reference/text/st.latex)
    - [st.code](https://docs.streamlit.io/library/api-reference/text/st.code)
    """
)