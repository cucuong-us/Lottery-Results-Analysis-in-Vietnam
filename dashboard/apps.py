import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Demo Streamlit")

# Tạo dữ liệu ngẫu nhiên
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.write("Dữ liệu mẫu:", df)

st.line_chart(df)  # Vẽ biểu đồ đường
