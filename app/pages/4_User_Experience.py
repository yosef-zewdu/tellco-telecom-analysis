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
data = experienceData()


def user_experience(data):
    analysis_options = {
        "Experience Cluster Figure": experience
        #"Exp": exper
    }
    selected_analyses = st.multiselect("Select List or Figure to explore users Experience", list(analysis_options.keys()))

    for analysis in selected_analyses:
        analysis_options[analysis](data)

    
def main():
    """
    The main function.
    """
    st.title("User Experience")
    st.markdown("""- The Experience data has three clusters:
            
            :      
            -Cluster 0
            -Cluster 1
            -Cluster 2 """)
    st.write('Experience Data head')
    st.write(data.head())

    user_experience(data)
    
if __name__ == "__main__":
    main()