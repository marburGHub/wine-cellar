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

# Sezione per aggiungere un vino
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

# Visualizzazione della lista di vini
st.header("Lista dei Vini in Cantina")
st.dataframe(wine_data)

# Sezione per eliminare un vino
st.header("Rimuovi un vino")
wine_to_remove = st.selectbox("Seleziona un vino da rimuovere", wine_data["Nome"].unique() if not wine_data.empty else [])
if st.button("Rimuovi Vino") and not wine_data.empty:
    wine_data = wine_data[wine_data["Nome"] != wine_to_remove]
    save_data()
    st.success("Vino rimosso con successo!")
    st.experimental_rerun()
