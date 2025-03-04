import streamlit as st
import pandas as pd
import info
import json
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


def load_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

data = load_data("data.json")

def activities_section(Nid_data, Nec_data, Ork_data, eldar_data):
    st.header("Xenos Archive 👽")
    tab1, tab2, tab3, tab4 = st.tabs(["Tyranids", "Necrons", "Orks", "Aeldari"])
    
    with tab1:
        st.subheader("Tyranids 🪲")
        for title, (details, image) in Nid_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=500)
            st.image(info.swarm_pic)
            for bullet in details:
                expander.write(bullet)
        
        #New
        st.subheader("Tyranid Consumption of Planets Over Time")
        selected_year = st.slider("Select Year", int(data["year"].min()), int(data["year"].max()), int(data["year"].min()))
        filtered_data = data[data["year"] <= selected_year]
        filtered_data["cumulative_planets_eaten"] = filtered_data["percent_planets_eaten"].cumsum()
        
        chart = alt.Chart(filtered_data).mark_line(point=True).encode(
            x=alt.X("year:O", title="Year"),
            y=alt.Y("cumulative_planets_eaten:Q", title="Planets Eaten"),
            color=alt.value("violet")
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)
    
    with tab2:
        st.subheader("Necrons 💀")
        for title, (details, image) in Nec_data.items():
          expander = st.expander(f"{title}")
          expander.image(image, width=500)
          st.image(info.cron_pic)
          for bullet in details:
             expander.write(bullet)

        data1 = pd.DataFrame ({
             "year": ["Gheden", "Nagathar", "Pyrrhia", "Suranas", "Trakonn", "Zykorak"],
              "tomb_worlds_awakened": [30, 15, 25, 55, 40, 80]
        })
        
        #New
        st.subheader("Blackstone Collectioned from Tomb Worlds")
        bar_chart = alt.Chart(data1).mark_bar().encode(
           x=alt.X("year:O", title="Tomb Worlds"),
           y=alt.Y("tomb_worlds_awakened:Q", title="Blackstone Harvested (Tons)"),
           color=alt.value("green")
        ).properties(
           width=600,
           height=400
        )
        st.altair_chart(bar_chart, use_container_width=True)

    with tab3:
        st.subheader("Orks 🍄")
        for title, (details, image) in Ork_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=500)
            st.image(info.AWagh_pic)
            for bullet in details:
                expander.write(bullet)


            orkdata = load_data("orkdata.json")

           
            st.subheader("Ork Expansion Over Armageddon")
            selected_year = st.slider("Select Year", int(orkdata["year"].min()), int(orkdata["year"].max()), int(orkdata["year"].min()))
            filtered_data = orkdata[orkdata["year"] <= selected_year]
            filtered_data["cumulative_worlds_conquered"] = filtered_data["percent_worlds_conquered"].cumsum()

            chart = alt.Chart(filtered_data).mark_line(point=True).encode(
              x=alt.X("year:O", title="Year (M41)"),
              y=alt.Y("cumulative_worlds_conquered:Q", title="Precent Conquered"),
            color=alt.value("green")
            ).properties(
                 width=600,
                height=400
            )

        st.altair_chart(chart, use_container_width=True)
    
    
    with tab4:
        st.subheader("Aeldari 🧝‍♂️")
        for title, (details, image) in eldar_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=500)
            st.image(info.eldar_pic)
            for bullet in details:
                expander.write(bullet)

        eldar_factions = {
            "Craftworlds": {"Speed": 7, "Durability": 6, "Melee": 5, "Ranged": 9, "Psychic": 10},
            "Drukhari": {"Speed": 10, "Durability": 4, "Melee": 9, "Ranged": 7, "Psychic": 2},
            "Harlequins": {"Speed": 8, "Durability": 9, "Melee": 8, "Ranged": 6, "Psychic": 4},
            
        }

        df = pd.DataFrame(eldar_factions).T
        categories = df.columns.tolist()

        st.title("Eldar Factions Analysis")

        
        st.dataframe(df)

        #New
        fig = go.Figure()
        for faction in df.index:
         fig.add_trace(go.Scatterpolar(
                r=df.loc[faction].tolist() + [df.loc[faction].tolist()[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name=faction
            ))

        fig.update_layout(
         polar=dict(
                radialaxis=dict(visible=True, range=[0, 10])
            ),
            showlegend=True
        )

        st.plotly_chart(fig)


    
    st.write("---")

activities_section(info.Nid_data,info.Nec_data,info.Ork_data,info.eldar_data)