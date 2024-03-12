import streamlit as st
import pandas as pd

# Définition de la fonction de transformation
def supprimer_colonnes_et_modifier_feuille(df):
    colonnes_a_supprimer = [
        "Nom", 
        "Nom_de_naissance", 
        "Prenom", 
        "Date_de_Naissance_Principal", 
        "Lieu_de_naissance", 
        "Pays_de_naissance",
        "Code_Postal_Patient_Principal",
        "Nom_Conjoint",
        "Nom_de_naissance_Conjoint",
        "Prenom_Conjoint",
        "Date_de_Naissance_Conjoint",
        "Lieu_de_naissance_de_conjoint",
        "Pays_de_naissance_de_conjoint",
        "Nb_emb_type_C"
    ]

    # Supprimer les colonnes spécifiées
    df.drop(columns=colonnes_a_supprimer, inplace=True, errors='ignore')

    # Modifier le nom de la feuille
    writer = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name="Export MF")
    writer.save()

# Interface Streamlit
st.title("Transformation de fichier Excel")

# Uploader de fichier Excel
uploaded_file = st.file_uploader("Uploader un fichier Excel", type=["xlsx"])

if uploaded_file is not None:
    # Lecture du fichier Excel
    df = pd.read_excel(uploaded_file)

    # Bouton pour déclencher la transformation et le téléchargement
    if st.button("Transformer et télécharger"):
        supprimer_colonnes_et_modifier_feuille(df)
        st.success("La transformation est terminée. Téléchargez le fichier transformé ci-dessous.")
        
        # Bouton pour télécharger le fichier transformé
        with open("output.xlsx", "rb") as file:
            st.download_button(label="Télécharger le fichier transformé", data=file, file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
