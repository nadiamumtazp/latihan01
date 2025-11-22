import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualizatin")

# Generate some data
x = np.linspace(0,10,100)
y = np.sin(x)
#Plot Data
fig, ax = plt.subplot()
ax.plot(x, y)
#display the plot
st.pyplot(fig)