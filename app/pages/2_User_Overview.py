import streamlit as st
import pandas as pd 
import sys
import os
sys.path.append(os.path.abspath('..'))
from utils import * 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px



# Use the function
data = loadData()


def top_handset_types(data):
    analysis_options = {
        "Top 10 Handset Types List": top_handset,
        "Top 10 Handset Types Figure": handset_plot,
        "Top 3 Handset Manufacturer List": top_handset_manufacturer,
        "Top 3 Handset Manufacturer Figure": manufacturer_plot
    }
    selected_analyses = st.multiselect("Select List or Figure to explore the Top Handset types and Manufacturers", list(analysis_options.keys()))

    for analysis in selected_analyses:
        analysis_options[analysis](data)

    
def main():
    """
    The main function.
    """
    st.title("User Overview")
    st.write(data.head())

    top_handset_types(data)
    
if __name__ == "__main__":
    main()