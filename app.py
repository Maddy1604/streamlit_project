import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Giving the document title
st.title("Simple Data Dashboard")

# File uploading area
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Condition to insure file upload is done or not
if uploaded_file is not None:
    st.write("File uploaded successfully......")
    df = pd.read_csv(uploaded_file)

    # Getting the data preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Filtering the data add drop-down menu to select
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select Value", unique_values)

    # Filtering the selected data
    filtered_data = df[df[selected_column] == selected_values]
    st.write(filtered_data)

    # Bar chart
    st.subheader("Bar Chart")
    # Select numeric columns for bar chart
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column (numeric)", numeric_columns)

    if st.button("Generate Bar Chart"):
        # Create figure and plot
        plt.figure(figsize=(10, 6))
        filtered_data.groupby(x_column)[y_column].sum().plot(kind='bar')
        plt.title(f'{y_column} by {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Display the plot
        st.pyplot(plt)
else:
    st.write("Waiting for file upload....")