import streamlit as st
from logic.collecte import collecter,get_stats
import plotly.express as px
from logic.linear_regression import preparer
import numpy as np

st.set_page_config(
    page_title="Prediction temperature",
    page_icon="🌦️",
)


st.title("Collecte des donnees :")
if "longitude" in st.session_state:
    lat,long=st.columns(2)
    with lat:
        with st.container(border=True):
            st.write(f"Latitude : :blue[{st.session_state.latitude:.2f}]")
    with long:
        with st.container(border=True):
            st.write(f"Longitude : :blue[{st.session_state.longitude:.2f}]")
    with st.spinner("Entrain de collecter"):
        data=collecter(st.session_state.latitude,st.session_state.longitude)
    st.subheader("Data frame:", divider="blue")
    st.write(data)
    st.session_state.data=data
    st.subheader("Data frame description:", divider="blue")
    st.write(get_stats(data))
    st.subheader("Data frame visualisation:", divider="blue")
    tab1, tab2,tab3 = st.tabs(["Temperature par date", "Humidite par date","Precipitation par date"])
    with tab1:
        st.line_chart(data, x="Date", y="Temperature moyenne (°C)",height=600)
    with tab2:
        st.line_chart(data, x="Date", y="Humidite moyenne (%)",height=600)
    with tab3:
        st.line_chart(data, x="Date", y="Precipitation (mm)",height=600)
    st.subheader("Data frame correlation matrix:", divider="blue")
    fig = px.imshow(data.drop('Date',axis=1,inplace=False).corr(), text_auto=True, aspect="auto")
    st.plotly_chart(fig, theme="streamlit")
    st.subheader("Data frame preparee:", divider="blue")
    data_preparer=preparer(data)
    st.session_state.data_preparer=data_preparer
    st.write(data_preparer)
    st.subheader("Matrice de correlation:", divider="blue")
    fig = px.imshow(data_preparer.corr(), text_auto=True, aspect="auto")
    st.plotly_chart(fig, theme="streamlit")
    st.subheader("Tendances saisonnières :", divider="blue")
    t1,t2,t3 =st.tabs(['Temperature','Humidite','Precipitation'])
    with t1:
        monthly_temp = data_preparer.groupby('Mois')['Temperature moyenne (°C)'].mean().reset_index()
        fig = px.line(
        monthly_temp,
        x='Mois',
        y='Temperature moyenne (°C)',
        title='Tendances saisonnières de la température',
        markers=True
        )
        fig.update_traces(line=dict(dash="solid", width=2))
        fig.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=np.arange(1, 13),
                ticktext=['Janvier', 'Feverier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
            ),
            yaxis=dict(title='Température moyenne (°C)'),
            title_x=0.5
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        st.plotly_chart(fig)
    with t2:
        monthly_hum = data_preparer.groupby('Mois')['Humidite moyenne (%)'].mean().reset_index()
        fig = px.line(
        monthly_hum,
        x='Mois',
        y='Humidite moyenne (%)',
        title="Tendances saisonnières de l'humidite",
        markers=True
        )
        fig.update_traces(line=dict(dash="solid", width=2))
        fig.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=np.arange(1, 13),
                ticktext=['Janvier', 'Feverier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
            ),
            yaxis=dict(title='Humidite moyenne (%)'),
            title_x=0.5
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        st.plotly_chart(fig)
    with t3:
        monthly_hum = data_preparer.groupby('Mois')['Precipitation (mm)'].mean().reset_index()
        fig = px.line(
        monthly_hum,
        x='Mois',
        y='Precipitation (mm)',
        title="Tendances saisonnières des précipitations",
        markers=True
        )
        fig.update_traces(line=dict(dash="solid", width=2))
        fig.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=np.arange(1, 13),
                ticktext=['Janvier', 'Feverier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
            ),
            yaxis=dict(title='Precipitation (mm)'),
            title_x=0.5
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        st.plotly_chart(fig)
    st.subheader("Tester les modeles", divider="blue")
    col1,col2=st.columns(2)
    with col1:
        if st.button("Regression linéaire"):
            st.switch_page("pages/04) Regression lineaire.py")
    with col2:
        if st.button("Random forest"):
            st.switch_page("pages/03) Random forest.py")
else:
    if st.button("Choisir localisation"):
        st.switch_page("pages/02) Location.py")