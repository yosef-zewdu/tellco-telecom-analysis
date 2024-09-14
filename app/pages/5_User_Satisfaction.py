import streamlit as st
import sys
import os
sys.path.append(os.path.abspath('..'))
from utils import * 



# Use the function
data = satisfactiontData()


def user_satisfaction(data):
    analysis_options = {
        "Satisfaction Cluster Figure": satisfaction
    }
    selected_analyses = st.multiselect("Select List or Figure to explore users engagement", list(analysis_options.keys()))

    for analysis in selected_analyses:
        analysis_options[analysis](data)

    
def main():
    """
    The main function.
    """
    st.title("User Satisfaction")
    st.markdown("""- The satisfaction data has two clusters:
            
            :      
            -Cluster 0
            -Cluster 1 """)
    st.write('Satisfaction Data head')
    st.write(data.head())

    user_satisfaction(data)
    
if __name__ == "__main__":
    main()