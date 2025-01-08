import streamlit as st


st.title("Prediction temperature 🌦️")

with st.container():
    st.subheader("Statistiques Rapides :", divider="blue")
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        {"title": "Années de Données", "value": "10+", "icon": "📊"},
        {"title": "Précision", "value": "95%", "icon": "🎯"},
        {"title": "Modèles machine learining", "value": "2", "icon": "🤖"},
        {"title": "Mise à jour", "value": "24/7", "icon": "🔄"}
    ]
    for col, metric in zip([col1, col2, col3, col4], metrics):
        with col:
            st.container(border=True,height=200).markdown(f"""
                <div style='text-align: center;'>
                    <h2 style='font-size: 2.5em; margin: 0;'>{metric['icon']}</h2>
                    <p class='medium-font gradient-text' style='margin: 0;'>{metric['value']}</p>
                    <p style='font-size: 1.1em; opacity: 0.8;'>{metric['title']}</p>
                </div>
            """, unsafe_allow_html=True)
    st.subheader("Fonctionnalités Principales :", divider="blue")
    tab1,tab2,tab3 =st.tabs(["🌍 Collecte", "📊 Analyse", "🤖 Prédiction"])
    with tab1:
        with st.container(border=True, height=220):
            st.header("Collecte de données")
            st.markdown("""
                <div class='medium-font'>
                    • Sélection interactive sur carte mondiale<br>
                    • Données météorologiques sur 10 ans<br>
                    • Mise à jour automatique quotidienne<br>
                    • Validation et nettoyage automatique
                </div>
            """, unsafe_allow_html=True)
    with tab2:
        with st.container(border=True, height=220):
            st.header("Analyse de données")
            st.markdown("""
            <div class='medium-font'>
                • Visualisations interactives<br>
                • Corrélations avancées<br>
                • Tendances temporelles<br>
                • Rapports détaillés
            </div>
            """, unsafe_allow_html=True)
    with tab3:
        with st.container(border=True, height=220):
            st.header("Prédiction de température")
            st.markdown("""
            <div class='medium-font'>
                • Régression linéaire optimisée<br>
                • Random Forest adaptatif<br>
                • Métriques de performance<br>
                • Ajustement automatique
            </div>
            """, unsafe_allow_html=True)
    st.subheader("Guide Détaillé du Processus :", divider="blue")
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 1: Sélection de Location 🎯</h3>
            </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Comment faire:")
            st.write("• Accédez à l'onglet 'Location'")
            st.write('• Utilisez la carte interactive mondiale')
            st.write('• Cliquez sur votre emplacement désiré')
            st.write('• Confirmez les coordonnées GPS')

        with col2:
            st.write("### Détails techniques :")
            st.write("• Utilisation de Folium pour la cartographie interactive")
            st.write("• Géocodage inverse pour identifier la ville/pays")
            st.write("• Précision des coordonnées à 0.01 degré")
            st.write("• Validation automatique des coordonnées")
    
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 2: Collecte des Données 📥</h3>
            </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Sources de données:")
            st.write("• API Open-Meteo pour données historiques")
            st.write("• 10 ans d'historique (2014-2024)")
            st.write('• Données météorologiques quotidiennes')
            st.write('• Mise à jour automatique')

        with col2:
            st.write("### Paramètres collectés:")
            st.write("• Température moyenne journalière (°C)")
            st.write("• Précipitations quotidiennes (mm)")
            st.write("• Humidité relative moyenne (%)")
            st.write("• Autres indicateurs météorologiques")
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 style='font-size: 2em;'>Étape 3: Analyse IA 🔍</h3>
            </div>
        """, unsafe_allow_html=True)
        col1,col2,col3=st.columns(3)
        with col1:
            st.write("### Prétraitement:")
            st.write("• Nettoyage des données")
            st.write("• Normalisation")
            st.write('• Calcul des moyennes mobiles')
            st.write('• Gestion des valeurs manquantes')
        with col2:
            st.write("### Visualisation:")
            st.write("• Graphiques temporels")
            st.write("• Matrices de corrélation")
            st.write('• Analyses statistiques')
            st.write('• Détection des tendances')
        with col3:
            st.write("### Modélisation:")
            st.write("• Sélection des caractéristiques")
            st.write("• Validation croisée")
            st.write('• Optimisation des paramètres')
            st.write('• Évaluation des modèles')
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Comparaison des Modèles 📊</h3>
            </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Avantages Régression Linéaire:")
            st.write("• Simplicité d'interprétation")
            st.write("• Rapidité d'exécution")
            st.write('• Performance stable')
            st.write('• Idéal pour les tendances linéaires')

        with col2:
            st.write("### Avantages Random Forest:")
            st.write("• Meilleure précision générale")
            st.write("• Gestion des relations complexes")
            st.write("• Robustesse au bruit")
            st.write("• Pas de problème de surapprentissage")
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Commencez Votre Prédiction</h3>
            </div>
        """, unsafe_allow_html=True)
        st.write("##### Suivez ces étapes simples pour obtenir des prédictions précises:")
        st.write("• Sélectionnez votre emplacement sur la carte")
        st.write("• Attendez la collecte et l'analyse des données")
        st.write("• Choisissez votre modèle de prédiction préféré")
        st.write("• Obtenez vos prédictions de température")
        st.warning("La partie de comparaison ne fonctionne qu'apres l'access au deux modeles",icon="⚠️")
        col1,col2,col3=st.columns(3)
        with col2:
            if st.button("Démarrer l'Analyse", type="primary"):
                st.switch_page("pages/02) Location.py")
