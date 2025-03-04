import streamlit as st
import time
import numpy as np
import pandas as pd
import random
import altair as alt

st.set_page_config(page_title="Warp Data", page_icon="🔮")

st.markdown("# Warp Data: ")

st.image("images/warp.webp", caption="Picture of the Warp outside of a Gellar Field ", use_container_width=True)

st.subheader("Real Time Analysis")
st.sidebar.header("Data Collection")
progress_text = st.sidebar.empty()
st.write(
    """This is quite impossible, The Warp, chaotic as it is, still follows patterns—hidden, but there.
    And yet, these readings… mere stochastic gibberish? No. There is a structure I am not yet perceiving. 
    Either the machine is flawed—unlikely, as I designed it—or the Warp is deliberately obfuscating its nature.
    Bah! This is akin to divining the Emperor’s will from the flight of carrion birds! The Omnissiah did not bless me 
    with ten millennia of intellect to be defeated by mere statistical noise! Activate the Noosphere’s deep-logic 
    analysis and keep running it till we find something—there must be a pattern. There is **always** a pattern."""
)

st.button("Update Data to Most Recent")


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

num_seconds = 20  # Adjust for longer data collection
values = [9, 8, 7, 6] * (num_seconds // 4)  # Ensure equal distribution
random.shuffle(values)  # Shuffle to make random order

df = pd.DataFrame({"Second": range(1, num_seconds + 1), "Average Value": [None] * num_seconds})

for i in range(num_seconds):
    df.loc[i, "Average Value"] = values[i]
    progress = int(((i + 1) / num_seconds) * 100)
    status_text.text("%i%% Complete" % progress)
    progress_bar.progress(progress)
    time.sleep(0.2)

status_text.text("100% Complete")
progress_bar.progress(100)

st.subheader("Noospheric Sensor Data:")
line_chart = (
    alt.Chart(df)
    .mark_line()
    .encode(
        x=alt.X("Second:Q", title="Time (seconds)"),
        y=alt.Y("Average Value:Q", title="Warp Flux"),
    )
)
st.altair_chart(line_chart, use_container_width=True)


st.subheader("Warp Flux Averages Per Second:")
bar_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Second:Q", title="Time (seconds)"),
        y=alt.Y("Average Value:Q", title="Warp Flux Average"),
    )
)
st.altair_chart(bar_chart, use_container_width=True)
