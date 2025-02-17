import streamlit as st
from logic.linear_regression import preparer
import plotly.express as px
from logic.random_forest import train_model,predict
import numpy as np

st.set_page_config(
    page_title="Prediction temperature",
    page_icon="🌦️",
)

st.title("Random forest")
if "data_preparer" in st.session_state:
    tab1, tab2= st.tabs(["Modele", "Prediction"])
    with tab1:
        with st.spinner("Calculation en cours"):
            trained=train_model(st.session_state.data_preparer)
            st.session_state.rf_metrics={
            "MSE": trained[0],
            "MAE": trained[2],
            "R²": trained[1]
            }
            st.session_state.rf_accuracy=trained[4]
            st.session_state.rf_pred=trained[5]
            st.session_state.rf_train_time=trained[6]
            st.session_state.rf_pred_time=trained[7]
            c1,c2,c3=st.columns(3)
            with c1:
                with st.container(border=True,height=150):
                    st.write("Erreur Quadratique Moyenne (MSE) :")
                    st.write(f"##### :blue[{trained[0]}]")
            with c2:
                with st.container(border=True,height=150):
                    st.write("Coefficient de Détermination (R²) :")
                    st.write(f"##### :blue[{trained[1]}]")
            with c3:
                with st.container(border=True,height=150):
                    st.write("Erreur Absolue Moyenne (MAE) :")
                    st.write(f"##### :blue[{trained[2]}]")
    with tab2:
        jour = st.selectbox("Jour (Day of the Month)", range(1,32))
        mois = st.selectbox("Mois (Month)", range(1,13))
        precipitation = st.slider("Précipitation (mm)", max_value=100.0, value=0.0)
        humidite = st.slider("Humidité (%)", min_value=0.0, max_value=100.0, value=50.0)
        temp_moyenne_mobile = st.slider("Température Moyenne Mobile (°C)",min_value=0.0, max_value=80.0,value=20.0)
        hum_moyenne_mobile = st.slider("Humidité Moyenne Mobile (%)", min_value=0.0, max_value=100.0, value=50.0)
        st.subheader("Prédiction de la température pour le jour", divider="blue")
        if st.button("Predict"):
            with st.spinner("Prediction en cours"):
                prediction=predict(trained[3],jour,mois,precipitation,humidite,temp_moyenne_mobile,hum_moyenne_mobile)
                with st.container(border=True):
                    st.write(f"### Prédiction de la température pour le jour {jour}/{mois} est : :blue[{prediction[0]:.2f}°C] ")

else:
    if st.button("Collecter des donnees"):
        st.switch_page("pages/1 Collecte.py")