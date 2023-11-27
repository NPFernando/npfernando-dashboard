import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="IT Performance Dashboard",
    layout="wide",
)

# Function to generate dummy data for live RAM and CPU usage
def generate_dummy_performance_data(metric, minutes=60):
    current_time = datetime.now()
    time_range = [current_time - timedelta(minutes=i) for i in range(minutes)]
    data = {'Timestamp': time_range, f'{metric} Usage (%)': [random.uniform(30, 70) for _ in range(minutes)]}
    return pd.DataFrame(data)

# Function to display live performance chart
def display_live_performance_chart(metric, df):
    st.subheader(f"Live {metric} Usage")
    chart = px.line(df, x='Timestamp', y=f'{metric} Usage (%)', title=f'Live {metric} Usage Over Time')
    st.plotly_chart(chart)

# Function to generate dummy virus detail report
def generate_dummy_virus_report(month):
    devices = ['Device A', 'Device B', 'Device C']
    virus_data = {
        'Device': random.choices(devices, k=20),
        'Virus Name': [f'Virus_{i}' for i in range(20)],
        'Detection Time': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(20)]
    }
    return pd.DataFrame(virus_data)

# Function to display virus detail report
def display_virus_detail_report(month, df):
    st.title("Monthly Virus Detail Report")
    st.subheader(f"Virus Detail Report for {month}")
    st.table(df)

# Main Streamlit app
if __name__ == '__main__':
    # Display live RAM and CPU usage
    st.title("Live IT Performance Dashboard")
    ram_df = generate_dummy_performance_data('RAM')
    cpu_df = generate_dummy_performance_data('CPU')

    display_live_performance_chart('RAM', ram_df)
    display_live_performance_chart('CPU', cpu_df)

    # Display monthly virus detail report
    selected_month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

    if selected_month:
        virus_df = generate_dummy_virus_report(selected_month)
        display_virus_detail_report(selected_month, virus_df)
    else:
        st.warning("Please select a month to view the virus detail report.")
