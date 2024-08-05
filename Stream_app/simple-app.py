import streamlit as st
import time 
import numpy as np
import pandas as pd

st.write("streamlit version = {}".format(st.__version__))

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

last_rows = np.random.randn(1,1)
chart = st.line_chart(last_rows)