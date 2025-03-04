import streamlit as st

st.set_page_config(page_title="Home Page:", page_icon="💫",)

st.write("# Grant St.Onge Lab 2")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    In this CS 1301 lab, we were told to build a web app using the streamlit Python library. In Phase I, we  were to create an online portfolio by following the steps outlined in a video tutorial. In Phase II, we had to create our own pages where we utilized new streamlit functions and display data using interactive charts.

    ### Page 1: 🤖
    - This page is the portfolio from Phase I of the lab, it is a satirical, grandiose self-introduction styled after Belisarius Cawl, a figure from Warhammer 40K. It humorously presents the author as a supreme technologist and visionary, blending exaggerated self-praise with sci-fi lore.
    
    - The overall tone is tongue-in-cheek arrogance, celebrating Cawl's boundless intellect and relentless innovation while mocking the dogmatic stagnation of the Imperium.
    
    ### Page 2: 🔮
    - This page creates a sci-fi-inspired "real-time" data analysis dashboard, blending lore and analytics in an engaging way. It mimics a scientist or tech-priest attempting to decipher chaotic patterns in a turbulent system (i.e., the Warp).
    
    - Includes simulated Real-Time Data Collection, which is a dataset initialized with 20 seconds of measurements. The values (ranging from 6 to 9) are randomly shuffled to simulate unpredictable sensor readings. A line chart dynamically updates with new data points every 0.2 seconds with a sidebar progress bar that fills up in sync with data collection. Lastly, a bar chart shows the Warp Flux Averages Per Second, summarizing the collected data. This data collection can be reset by the press of a button.
    
    - Also it includes a dramatic lore-style text monologue about finding hidden patterns in chaotic data

    ### Page 3:  👽
    - This page serves as the Xenos Archive, an interactive data-driven compendium of the most infamous alien species in Warhammer 40K. Structured into four sections—Tyranids, Necrons, Orks, and Aeldari
   
    - Each tab unveils a trove of knowledge, with expandable lore entries, faction imagery, and interactive charts that track their conquests, awakenings, and battles across the galaxy.
   
    - The aesthetic channels the perspective of an Imperial archivist or Tech-Priest, painstakingly documenting alien threats with reverence, caution, and a touch of dread.
"""
)
