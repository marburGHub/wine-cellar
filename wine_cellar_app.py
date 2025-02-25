import streamlit as st
import pandas as pd
import os

# Nome del file CSV per salvare i dati
DATA_FILE = "wine_cellar.csv"

# Carica il database se esiste
if os.path.exists(DATA_FILE):
    wine_data = pd.read_csv(DATA_FILE)
else:
    wine_data = pd.DataFrame(columns=["Nome", "Anno", "Tipologia", "Cantina", "Quantità", "Note"])

# Funzione per salvare i dati
def save_data():
    wine_data.to_csv(DATA_FILE, index=False)

# Interfaccia Streamlit
st.title("Gestione Cantina di Vini")

# Menu principale
menu = st.selectbox("Seleziona un'operazione", ["Aggiungi un vino", "Aggiungi un movimento", "Controlla lo stock", "Vedi statistiche"])

if menu == "Aggiungi un vino":
    st.header("Aggiungi un nuovo vino")
    name = st.text_input("Nome del vino")
    year = st.number_input("Anno", min_value=1900, max_value=2100, step=1)
    type = st.selectbox("Tipologia", ["Rosso", "Bianco", "Spumante", "Altro"])
    winery = st.text_input("Cantina produttrice")
    quantity = st.number_input("Quantità", min_value=0, step=1)
    notes = st.text_area("Note personali")

    if st.button("Aggiungi Vino"):
        new_entry = pd.DataFrame([[name, year, type, winery, quantity, notes]],
                                  columns=wine_data.columns)
        wine_data = pd.concat([wine_data, new_entry], ignore_index=True)
        save_data()
        st.success("Vino aggiunto con successo!")
        st.rerun()

elif menu == "Aggiungi un movimento":
    st.header("Aggiungi un movimento")
    st.write("Funzione in sviluppo...")

elif menu == "Controlla lo stock":
    st.header("Lista dei Vini in Cantina")
    st.dataframe(wine_data)

elif menu == "Vedi statistiche":
    st.header("Statistiche sui vini")
    st.write("Funzione in sviluppo...")

