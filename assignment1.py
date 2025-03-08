import streamlit as st
import pandas as pd
import random
import time

conn = st.connection("gsheets", type="gsheets")
df = pd.DataFrame(conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1htXnIS8wTOsiSak3NhHYQR1tK-KPNLrW5xkkGrsyyI8/edit?usp=sharing"))

st.title("What is the relationship between mpg and horsepower?")

# Initialize session state variables
if 'startTime' not in st.session_state:
    st.session_state.startTime = 0
if 'endTime' not in st.session_state:
    st.session_state.endTime = None
if 'answeredQuestion' not in st.session_state:
    st.session_state.answeredQuestion = False
if 'displayGraph' not in st.session_state:
    st.session_state.displayGraph = False
if 'randomChoice' not in st.session_state:
    st.session_state.randomChoice = random.uniform(0,1)
if 'elapsedTime' not in st.session_state:
    st.session_state.elapsedTime = None

# Only show Display Graph button if not already displayed
if not st.session_state.displayGraph:
    display_button = st.button("Display Graph")
    if display_button:
        st.session_state.startTime = time.time()
        st.session_state.displayGraph = True
        st.rerun()

# Display the graph if button was clicked
if st.session_state.displayGraph:
    # Create a DataFrame with just the columns we need
    chart_data = df[['mpg', 'horsepower']]
    
    if st.session_state.randomChoice <= 0.5:
        st.line_chart(chart_data, x='mpg', y='horsepower')
    else:
        st.scatter_chart(chart_data, x='mpg', y='horsepower')
    
    # Show answer button if not already answered
    if not st.session_state.answeredQuestion:
        answer_button = st.button("I answered your question!")
        if answer_button:
            st.session_state.answeredQuestion = True
            st.session_state.endTime = time.time()
            st.session_state.elapsedTime = st.session_state.endTime - st.session_state.startTime
            st.rerun()

# Display the elapsed time if available
if st.session_state.elapsedTime is not None:
    st.balloons()
    st.write(f"It took you {st.session_state.elapsedTime:.2f} seconds to answer!")




















