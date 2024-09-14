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
data = engagementData()


def user_engagement(data):
    analysis_options = {
        "Engagement Cluster Figure": engagement
    }
    selected_analyses = st.multiselect("Select List or Figure to explore users engagement", list(analysis_options.keys()))

    for analysis in selected_analyses:
        analysis_options[analysis](data)

    
def main():
    """
    The main function.
    """
    st.title("User Engagement")
    st.markdown("""- The engagement data has three clusters:
            
            :      
            -Cluster 0
            -Cluster 1
            -Cluster 2 """)
    st.write('Engagement Data head')
    st.write(data.head())

    user_engagement(data)
    
if __name__ == "__main__":
    main()