import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sys
import os
sys.path.append(os.path.abspath('..'))
from utils import * 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # or 'TkAgg', 'Qt5Agg', etc.




# Load data from PostgreSQL
conn = st.connection("telecom")
data = conn.query("SELECT * FROM xdr_data")



def display_data_preview(data):
    """
    Display the first few rows of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Data Preview")
    st.write(data.head())

def display_data_types(data):
    """
    Display the data types of each column.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Data Types")
    st.write(data.dtypes)

def display_summary_statistics(data):
    """
    Display the summary statistics of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Summary Statistics")
    st.write(data.describe())


   
def display_missing_data(data):
    """
    Display the summary statistics of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Missing Values Table ")
    st.write(missing_values_table(data))
    


def eda_page(data):
    """
    Display the exploratory data analysis page.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.title("Exploratory Data Analysis")

    display_data_preview(data)

    analysis_options = {
        "Summary Statistics": display_summary_statistics,
        "Data Types": display_data_types,
        "Missing Data Table": display_missing_data
    }

    selected_analyses = st.multiselect("Select analyses to perform", list(analysis_options.keys()))

    for analysis in selected_analyses:
        analysis_options[analysis](data)

def main():
    """
    The main function. 
    """
    
    eda_page(data)
    
if __name__ == "__main__":
    main()