import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load Data
@st.cache_data
def loadData():
    return pd.read_csv('data/df_cleaned.csv')


# Load Data
@st.cache_data
def engagementData():
    return pd.read_csv('data/engagement_metrics.csv')


# Load Data
@st.cache_data
def experienceData():
    return pd.read_csv('data/experience_metrics.csv')

# Load Data
@st.cache_data
def satisfactiontData():
    return pd.read_csv('data/satisfaction_metrics.csv')





# Missing values 
def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Get the count of non-null values for each column
    non_null_counts = df.notnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes
    
    # missing values unique number
    unique_counts = df.nunique()
    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype, non_null_counts, unique_counts], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Dtype',3: 'Values', 4: 'Unique Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
          "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")
    

    # Return the dataframe with missing information
    return mis_val_table_ren_columns



def top_handset(df):
    # Exclude "undefined" from the DataFrame
    filtered_df = df[df['Handset Type'] != 'undefined']
    # Count occurrences of each handset
    handset_counts = filtered_df['Handset Type'].value_counts()

    # Get the top 10 handsets
    top_10_handsets = handset_counts.head(10)

    # Display the results
    st.header("Top 10 handsets")
    # st.write(top_10_handsets.columns)
    st.write(top_10_handsets)

    

def handset_plot(df):
    # Exclude "undefined" from the DataFrame
    filtered_df = df[df['Handset Type'] != 'undefined']
    # Count occurrences of each handset
    handset_counts = filtered_df['Handset Type'].value_counts()
    top_10_handsets = handset_counts.head(10)
    handset = top_10_handsets.reset_index()
    handset.columns = ['Handset Type', 'Count'] 

    fig = px.bar(handset, x='Handset Type', y='Count', title='Top Ten Handset Types',
             labels={'Handset Type': 'Handset Type', 'Count': 'Count'},
             color='Count',  # Optional: color bars based on count
             template='plotly_white') 
    
    st.plotly_chart(fig)



def top_handset_manufacturer(df):
    # Count occurrences of each handset
    handset_manuf_counts = df['Handset Manufacturer'].value_counts()

    # Get the top 3 handsets manufacturer
    top_3_manufacturer = handset_manuf_counts.head(3)

    # Display the results
    st.header("Top 3 handsets manufacturer")
    # st.write(top_10_handsets.columns)
    st.write(top_3_manufacturer)

    

def manufacturer_plot(df):
    # Count occurrences of each handset
    handset_manuf_counts = df['Handset Manufacturer'].value_counts()

    # Get the top 3 handsets manufacturer
    top_3_manufacturer = handset_manuf_counts.head(3)
    manuf = top_3_manufacturer.reset_index()
    manuf.columns = ['Handset Manufacturer', 'Count'] 

    fig = px.bar(manuf, x='Handset Manufacturer', y='Count', title='Top three Handset Manufacturer',
             labels={'Handset Manufacturer': 'Handset Manufacturer', 'Count': 'Count'},
             color='Count',  # Optional: color bars based on count
             template='plotly_white') 
    
    st.plotly_chart(fig)





def engagement(data):
    # For Engagement Clusters
    engagement_summary = data.groupby('engagement_cluster')[['total_duration', 'total_traffic', 'sessions_frequency']].mean()

    # Create a color mapping for each trace
    session_color = 'lightgreen'
    duration_color = 'purple'
    traffic_color = 'blue'

    fig = make_subplots(rows=3, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.1,
                        subplot_titles=("Sessions Frequency", "Total Duration", "Total Traffic"))

    # Convert cluster indices to strings for x-axis labels
    cluster_labels = engagement_summary.index.astype(str)

    # Add traces with cluster colors
    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=engagement_summary['sessions_frequency'],
                         marker=dict(color=session_color),
                         name="Sessions Frequency"),
                  row=1, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=engagement_summary['total_duration'],
                         marker=dict(color=duration_color),
                          name="Total Duration"),
                  row=2, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=engagement_summary['total_traffic'],
                         marker=dict(color=traffic_color),
                          name="Total Traffic"),
                  row=3, col=1)

    # Update layout and axes titles
    fig.update_layout(height=720, width=1000, 
                      title_text="Engagement Metrics for Each Cluster", showlegend=True)
    
   

    st.plotly_chart(fig)





def experience(data):
    # For Engagement Clusters
    experience_summary = data.groupby('experience_cluster')[['avg_tcp_retransmission_bytes', 'avg_rtt_ms', 'avg_throughput_kbps']].mean()

    # Create a color mapping for each trace
    session_color = 'lightgreen'
    duration_color = 'purple'
    traffic_color = 'blue'

    fig = make_subplots(rows=3, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.1,
                        subplot_titles=("Average TCP Retransmission Bytes", "Average RTT (ms)", "Average Throughput (kbps)"))

    # Convert cluster indices to strings for x-axis labels
    cluster_labels = experience_summary.index.astype(str)

    # Add traces with cluster colors
    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=experience_summary['avg_tcp_retransmission_bytes'],
                         marker=dict(color=session_color),
                         name="avg_tcp_retransmission_bytes"),
                  row=1, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=experience_summary['avg_rtt_ms'],
                         marker=dict(color=duration_color),
                          name="avg_rtt_ms"),
                  row=2, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=experience_summary['avg_throughput_kbps'],
                         marker=dict(color=traffic_color),
                          name="avg_throughput_kbps"),
                  row=3, col=1)

    # Update layout and axes titles
    fig.update_layout(height=720, width=1200, 
                      title_text="Experience Metrics for Each Cluster", showlegend=True)
    
   

    st.plotly_chart(fig)



def satisfaction(data):
    
    #  Aggregate average satisfaction & experience scores per cluster
    avg_scores_per_cluster = data.groupby('eng_exp_cluster').agg(
        users=('MSISDN/Number', 'nunique'),
        avg_satisfaction=('satisfaction_score', 'mean'),
        avg_experience=('experience_score', 'mean')
        ).reset_index()
    
    # Create a color mapping for each trace
    session_color = 'lightgreen'
    duration_color = 'purple'
    traffic_color = 'blue'

    fig = make_subplots(rows=3, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.1,
                        subplot_titles=("Average Experience", "Average Satisfaction", " Number of Users"))

    # Convert cluster indices to strings for x-axis labels
    cluster_labels = avg_scores_per_cluster.index.astype(str)

    # Add traces with cluster colors
    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=avg_scores_per_cluster['avg_experience'],
                         marker=dict(color=session_color),
                         name="avg_experience"),
                  row=1, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=avg_scores_per_cluster['avg_satisfaction'],
                         marker=dict(color=duration_color),
                          name="avg_satisfaction"),
                  row=2, col=1)

    fig.add_trace(go.Bar(x=cluster_labels, 
                         y=avg_scores_per_cluster['users'],
                         marker=dict(color=traffic_color),
                          name="users"),
                  row=3, col=1)

    # Update layout and axes titles
    fig.update_layout(height=720, width=1000, 
                      title_text="Satisfaction Metrics for Each Cluster", showlegend=True)
    
   

    st.plotly_chart(fig)

# def exper(data):
#     # For Engagement Clusters
#     experience_summary = data.groupby('experience_cluster')[['avg_tcp_retransmission_bytes', 'avg_rtt_ms', 'avg_throughput_kbps']].mean()

#     # Define colors for each cluster
#     colors = {
#         0: 'lightgreen',
#         1: 'purple',
#         2: 'blue'
#     }

#     fig = make_subplots(rows=3, cols=1,
#                         shared_xaxes=True,
#                         vertical_spacing=0.1,
#                         subplot_titles=("Average TCP Retransmission Bytes", "Average RTT (ms)", "Average Throughput (kbps)"))

#     # Convert cluster indices to strings for x-axis labels
#     #cluster_labels = experience_summary.index.astype(str)

#     # Add traces for each metric with colors based on clusters
#     for cluster in experience_summary.index:
#         fig.add_trace(go.Bar(
#             x=[cluster], 
#             y=[experience_summary.loc[cluster, 'avg_tcp_retransmission_bytes']],
#             marker=dict(color=colors[cluster]),
#             name="avg_tcp_retransmission_bytes" if cluster == 0 else "",  # Show name only for the first trace
#         ), row=3, col=1)

#         fig.add_trace(go.Bar(
#             x=[cluster], 
#             y=[experience_summary.loc[cluster, 'avg_rtt_ms']],
#             marker=dict(color=colors[cluster]),
#             name="avg_rtt_ms" if cluster == 1 else "",  # Show name only for the first trace
#         ), row=2, col=1)

#         fig.add_trace(go.Bar(
#             x=[cluster], 
#             y=[experience_summary.loc[cluster, 'avg_throughput_kbps']],
#             marker=dict(color=colors[cluster]),
#             name="avg_throughput_kbps" if cluster == 2 else "",  # Show name only for the first trace
#         ), row=1, col=1)

#     # Update layout
#     fig.update_layout(height=720, width=600, 
#                     title_text="Experience Metrics Based on Clusters",
#                     showlegend=True)


#     st.plotly_chart(fig)