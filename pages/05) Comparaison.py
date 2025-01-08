import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Prediction temperature",
    page_icon="🌦️",
)


st.title("Comparaison entre les metriques des modeles :")

if "rf_metrics" in st.session_state and "lr_metrics" in st.session_state:
    with st.spinner("Attender un peu"):
        st.subheader("Comparaison graphique des modeles:", divider="blue")
        blue_colors = ["#1f77b4", "#a6cbe3"]
        metrics_df = pd.DataFrame([st.session_state.rf_metrics, st.session_state.lr_metrics], index=["Random Forest", "Linear Regression"]).reset_index()
        metrics_df = metrics_df.melt(id_vars="index", var_name="Metric", value_name="Value")
        fig = px.bar(
        metrics_df,
        x="Metric",
        y="Value",
        color="index",
        barmode="group",
        text="Value",
        color_discrete_sequence=blue_colors,
        title="Comparaison des performances des modèles"
        )
        fig.update_layout(
            xaxis_title="Métrique",
            yaxis_title="Valeur",
            legend_title="Modèle",
            template="plotly_white"
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig)
        st.subheader("Graphique de la precision:", divider="blue")
        accuracy_df = pd.DataFrame({
            "Modèle": ["Random Forest", "Régression Linéaire"],
            "Précision": [st.session_state.rf_accuracy, st.session_state.lr_accuracy]
        })
        fig = px.bar(accuracy_df, x="Modèle", y="Précision", color="Modèle", title="Comparaison de la Précision des Modèles", color_discrete_sequence=blue_colors)
        fig.update_layout(xaxis_title="Modèle", yaxis_title="Précision")
        st.plotly_chart(fig)
        st.subheader("La comparaison des predictions vs valeurs reelles:", divider="blue")
        prediction_df = pd.DataFrame({
            "Valeur réelle": st.session_state.y_test,
            "Prédiction RF": st.session_state.rf_pred,
            "Prédiction LR": st.session_state.lr_pred
        })
        fig = px.scatter(prediction_df, x="Valeur réelle", y="Prédiction RF", color_discrete_sequence=["#1f77b4"], title="Prédictions vs Valeurs réelles (Random Forest)")
        fig.add_trace(px.scatter(prediction_df, x="Valeur réelle", y="Prédiction LR", color_discrete_sequence=["#a6cbe3"]).data[0])
        fig.update_layout(
            xaxis_title="Valeur réelle",
            yaxis_title="Prédiction",
            template="plotly_white"
        )
        st.plotly_chart(fig)
        st.subheader("Comparaison de la vitesse des modeles:", divider="blue")
        speed_df = pd.DataFrame({
            "Model": ["Random Forest", "Linear Regression"],
            "Training Time (s)": [st.session_state.rf_train_time, st.session_state.lr_train_time],
            "Prediction Time (s)": [st.session_state.rf_pred_time, st.session_state.lr_pred_time]
        })
        speed_df_melted = speed_df.melt(id_vars="Model", var_name="Type of Time", value_name="Time (seconds)")
        fig = px.bar(speed_df_melted, x="Model", y="Time (seconds)", color="Type of Time", barmode="group",
                    title="Speed Comparison of Models (Training and Prediction Time)",
                    labels={"Time (seconds)": "Time (seconds)", "Type of Time": "Type of Time"})

        st.plotly_chart(fig)
elif "lr_metrics" in st.session_state and "rf_metrics" not in st.session_state:
    st.warning("Il faut entrainer le modele de Random Forest",icon="⚠️")
    if st.button("Entrainer le modele"):
        st.switch_page("pages/03) Random forest.py")
elif "rf_metrics" in st.session_state and "lr_metrics" not in st.session_state:
    st.warning("Il faut entrainer le modele de Lineaire regression",icon="⚠️")
    if st.button("Entrainer le modele"):
        st.switch_page("pages/04) Regression lineaire.py")
else:
    st.warning("Les modeles ne sont pas encore entraines",icon="⚠️")
    col1,col2=st.columns(2)
    with col1:
        if st.button("Regression linéaire"):
            st.switch_page("pages/04) Regression lineaire.py")
    with col2:
        if st.button("Random forest"):
            st.switch_page("pages/03) Random forest.py")