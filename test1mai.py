import streamlit as st
import pandas as pd
from io import BytesIO
import openpyxl

# Colonnes à supprimer du fichier Excel
columns_to_drop = [
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

st.title("Importer et Transformer un Fichier Excel")

# Permettre à l'utilisateur de télécharger un fichier Excel
uploaded_file = st.file_uploader("Téléchargez un fichier Excel", type=["xlsx"])

if uploaded_file:
    # Lire le fichier Excel avec pandas
    df = pd.read_excel(uploaded_file)

    # Supprimer les colonnes spécifiées
    df_cleaned = df.drop(columns=columns_to_drop, errors='ignore')

    # Convertir le DataFrame en Excel avec le nouveau nom de feuille
    excel_buffer = BytesIO()  # Créer un buffer en mémoire pour le fichier Excel
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        # Écrire le DataFrame dans une feuille nommée "Export MF"
        df_cleaned.to_excel(writer, sheet_name="Export MF", index=False)
    
    # Revenir au début du buffer
    excel_buffer.seek(0)

    # Créer un lien de téléchargement pour le fichier Excel
    st.download_button(
        label="Télécharger le fichier Excel transformé",
        data=excel_buffer,
        file_name="transformed_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Afficher un aperçu du DataFrame transformé
    st.write("Aperçu des données transformées :")
    st.dataframe(df_cleaned.head(10))  # Afficher les 10 premières lignes
