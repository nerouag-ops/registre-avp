import streamlit as st
import datetime

st.set_page_config(page_title="Registre AVP - EHS Salim Zemirli", layout="wide")
st.title("Registre Hospitalier des Victimes d'AVP")
st.markdown("---")

onglet1, onglet2, onglet3 = st.tabs([
    "📝 1. État civil & Admission", 
    "🚗 2. Circonstances de l'accident", 
    "🚑 3. Bilan lésionnel interactif"
])

with onglet1:
    st.subheader("Identification de la victime")
    col1, col2 = st.columns(2)
    with col1:
        nom = st.text_input("Nom :")
        prenom = st.text_input("Prénom :")
        sexe = st.radio("Sexe :", options=["Masculin", "Féminin"], horizontal=True)
    with col2:
        age = st.number_input("Âge (en années) :", min_value=0, max_value=120, step=1)
        wilaya = st.text_input("Wilaya de résidence :")
        commune = st.text_input("Commune de résidence :")

    st.markdown("---")
    st.subheader("Détails de l'admission")
    col3, col4 = st.columns(2)
    with col3:
        date_admission = st.date_input("Date d'admission :", datetime.date.today())
        mode_admission = st.selectbox("Mode d'admission :", ["Directe", "Transfert externe", "Transfert interne"])
    with col4:
        service = st.selectbox("Service d'admission :", ["Orthopédie - traumatologie", "Anesthésie Réanimation", "Chirurgie Générale", "Neurochirurgie", "Autre"])
        if mode_admission == "Directe":
            moyen_arrivee = st.selectbox("Moyen d'arrivée :", ["Protection civile", "SAMU", "Moyens Propres", "Ambulance Privée", "Inconnu"])

with onglet2:
    st.subheader("Dynamique de l'accident")
    col_circ1, col_circ2 = st.columns(2)
    with col_circ1:
        date_avp = st.date_input("Date de l'accident :", datetime.date.today())
        victime_statut = st.selectbox("La victime occupait :", ["Piéton", "Motocycliste", "Automobile", "Cycliste", "Camionnette", "Poids lourd", "Autobus", "Autre"])
        if victime_statut not in ["Piéton", "Autre"]:
            role_victime = st.radio("Rôle de la victime :", ["Conducteur", "Passager", "Autre (à l'extérieur)"])
    with col_circ2:
        partie_adverse = st.selectbox("La partie adverse dans l'accident est :", ["Automobile ou Camionnette", "Poids lourd ou Autobus", "Motocycle", "Objet fixe ou stationnaire", "Piéton ou animal", "Accident sans collision (glissement)", "Inconnu"])

with onglet3:
    st.subheader("Cartographie anatomique")
    
    with st.expander("🧠 TÊTE (Crâne, cerveau)"):
        tc = st.radio("Notion de traumatisme crânien ?", ["Non", "Oui"], horizontal=True)
        if tc == "Oui":
            glasgow = st.slider("Score de Glasgow à l'admission :", 3, 15, 15)
            dpc = st.number_input("Durée de la perte de connaissance (Heures) :", min_value=0.0)
            deficit = st.text_input("Déficit neurologique associé :")

    with st.expander("🫀 THORAX (Organes, Vaisseaux)"):
        anatomie_thorax = st.selectbox("Structure atteinte :", ["Paroi thoracique (Os/Muscles)", "Cœur (Organes internes)", "Gros Vaisseaux sanguins"])
        if anatomie_thorax == "Cœur (Organes internes)":
            lesion_coeur = st.selectbox("Nature de la lésion cardiaque :", ["Contusion", "Déchirure", "Perforation", "Rupture", "Commotion"])
        elif anatomie_thorax == "Gros Vaisseaux sanguins":
            lesion_vaisseaux = st.selectbox("Nature de la lésion vasculaire :", ["Arrachement", "Lacération", "Rupture", "Section"])
            
    with st.expander("🦵 MEMBRES INFÉRIEURS & BASSIN"):
        os_touche = st.selectbox("Siège exact :", ["Fémur", "Tibia", "Fibula", "Bassin (Ceinture pelvienne)", "Articulations"])
        nature_lesion = st.selectbox("Nature de la lésion osseuse :", ["Fracture fermée simple", "Fracture fermée comminutive", "Fracture ouverte (exposée)", "Luxation", "Écrasement", "Amputation"])

    st.markdown("---")
    perte_sang = st.radio("Perte de sang en % de volume :", ["≤ 20%", "> 20%"], horizontal=True)

st.markdown("---")
if st.button("💾 Valider et enregistrer le dossier d'admission", use_container_width=True):
    st.success("Le dossier a été enregistré.")
