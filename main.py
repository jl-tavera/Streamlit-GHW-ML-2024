import streamlit as st
import numpy as np
import pandas as pd
import csv

st.title('Pokemon Data Visualization Tool')
st.divider()

# Load the data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

# create a dataframe with the pokemon data
df = pd.DataFrame(data)

# Display the data
st.dataframe(df)