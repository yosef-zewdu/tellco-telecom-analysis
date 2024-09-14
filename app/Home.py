import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine





# ---------------------------------------------------------------------------
# Load data from PostgreSQL
# conn = st.connection("telecom")
# df = conn.query("SELECT * FROM xdr_data")

# # Set page title
# st.title("Telecom Data - Exploratory Data Analysis")

# # Show first few rows of the dataset
# st.subheader("Initial Data")
# st.write(df.head())



# # Option to drop or fill missing values
# st.subheader("Handle Missing Values")
# missing_column = st.selectbox("Choose a column to fill missing values", df.columns[df.isnull().any()])
# fill_method = st.radio("Fill method", ["Fill with Mean", "Fill with Median", "Drop Rows"])

# if st.button("Apply Fill"):
#     if fill_method == "Fill with Mean":
#         df[missing_column] = df[missing_column].fillna(df[missing_column].mean())
#     elif fill_method == "Fill with Median":
#         df[missing_column] = df[missing_column].fillna(df[missing_column].median())
#     else:
#         df = df.dropna(subset=[missing_column])
#     st.success(f"{missing_column} cleaned successfully")

# # ---- 2. Descriptive Statistics ----
# st.subheader("Descriptive Statistics")
# st.write(df.describe())

# # ---- 3. Visualizations ----

# # Handset Type Distribution
# st.subheader("Handset Type Distribution")
# handset_counts = df['Handset Type'].value_counts()
# st.bar_chart(handset_counts)

# # Comparing Handset Type with another feature, e.g., Total DL (Bytes)
# st.subheader("Comparison: Handset Type vs. Total DL (Bytes)")
# df_clean = df.dropna(subset=["Handset Type", "Total DL (Bytes)"])  # Clean data

# fig, ax = plt.subplots()
# sns.boxplot(x="Handset Type", y="Handset Manufacturer", data=df_clean, ax=ax)
# plt.xticks(rotation=90)
# stplot(fig)


# Load data from PostgreSQL
conn = st.connection("telecom")
df = conn.query("SELECT * FROM xdr_data")

# Streamlit app
# st.title("Telecom User Data Analysis")


# # User Engagement
# st.header("User Engagement")
# engagement_metrics = df[['Activity Duration DL (ms)', 'Activity Duration UL (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']].describe()
# st.write(engagement_metrics)

# # User Experience
# st.header("User Experience")
# experience_metrics = df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']].describe()
# st.write(experience_metrics)
 
# # User Satisfaction
# st.header("User Satisfaction")
# df['Satisfaction Score'] = (
#     (100 - df['Avg RTT DL (ms)']) * 0.3 +
#     (df['Avg Bearer TP DL (kbps)'] * 0.4) +
#     (100 - df['TCP DL Retrans. Vol (Bytes)']) * 0.3
# )
# st.write("Average Satisfaction Score:", df['Satisfaction Score'].mean())

# # Visualizations
# st.subheader("Data Usage Distribution")
# st.bar_chart(df[['Total DL (Bytes)', 'Total UL (Bytes)']])

# st.subheader("RTT Distribution")
# st.line_chart(df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)']])

# st.subheader("Throughput Distribution")
# st.line_chart(df[['Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']])

import streamlit as st

def main():
    st.title("Tellco Users Analytics Dashboard")
    st.header("Welcome to the User Analytics Dashboard!" )
    st.write("* This app provides findings, figures and insights into users engagement, experience and satisfaction.")

    # Features Section
    st.header("Features")
    
    
    st.subheader("EDA (Exploratory Data Analysis)")
    st.write("- Get statistical summaries to uncover hidden patterns.")
    
    st.subheader("User Overview")
    st.write("- Get a high-level view of users usage and behavior to understand the users better.")
    
    st.subheader("User Engagement")
    st.write("- Analyze how users engage by reviewing sesssions frequency, total duration and total data traffic.")
    
    st.subheader("User Experience")
    st.write("- Evaluate users Experience by analyzing the quality of the service using Throughput, Round trip time and TCP Retransmission.")
    
    st.subheader("User Satisfaction")
    st.write("- Measure user satisfaction through engagement and experience metrics.")
    
    st.subheader("Report")
    st.write("- Generate comprehensive reports that summarize key findings, insights and recommendations")

     # Navigation Links
    st.title("Navigation")
    st.markdown("[EDA](EDA)")
    st.markdown("[User Overview](User_Overview)")
    st.markdown("[User Engagement](User_Engagement)")
    st.markdown("[User Experience](User_Experience)")
    st.markdown("[User Satisfaction](User_Satisfaction)")
    st.markdown("[Report](Reports)")

    # Call to Action
    st.write("- Use the sidebar to navigate to different sections of the app and gain valuable insights!")

if __name__ == "__main__":
    main()