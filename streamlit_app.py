import streamlit as st
import pandas as pd

# Définition de la fonction de transformation
def supprimer_colonnes_et_modifier_feuille(df):
    # Liste des colonnes à supprimer
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

    return df

# Interface Streamlit
st.title("Transformation de fichier CSV en Excel")

# Uploader de fichier CSV
uploaded_file = st.file_uploader("Uploader un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lecture du fichier CSV
    df = pd.read_csv(uploaded_file)

    # Bouton pour déclencher la transformation et le téléchargement
    if st.button("Transformer et télécharger"):
        df_transforme = supprimer_colonnes_et_modifier_feuille(df)
        st.success("La transformation est terminée. Téléchargez le fichier transformé ci-dessous.")
        
        # Sauvegarder le DataFrame transformé dans un fichier Excel temporaire
        with st.spinner("Enregistrement du fichier Excel..."):
            temp_file_path = "temp.xlsx"
            writer = pd.ExcelWriter(temp_file_path, engine='xlsxwriter')
            df_transforme.to_excel(writer, index=False, sheet_name="Export MF")
            writer.save()
        
        # Bouton pour télécharger le fichier transformé
        with open(temp_file_path, "rb") as file:
            st.download_button(label="Télécharger le fichier transformé", data=file, file_name="fichier_transforme.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
