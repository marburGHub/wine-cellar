import streamlit as st
import pandas as pd
import os

# File CSV per i dati
DATA_FILE = "wine_cellar.csv"
PRODUCERS_FILE = "producers.csv"
WINE_TYPES_FILE = "wine_types.csv"

# Carica i dati esistenti o crea file vuoti
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Nome", "Anno", "Tipologia", "Cantina", "Quantità", "Note"]).to_csv(DATA_FILE, index=False)
if not os.path.exists(PRODUCERS_FILE):
    pd.DataFrame(columns=["Produttore"]).to_csv(PRODUCERS_FILE, index=False)
if not os.path.exists(WINE_TYPES_FILE):
    pd.DataFrame(columns=["Tipologia"]).to_csv(WINE_TYPES_FILE, index=False)

wine_data = pd.read_csv(DATA_FILE)
producers_data = pd.read_csv(PRODUCERS_FILE)
wine_types_data = pd.read_csv(WINE_TYPES_FILE)

# Funzione per salvare i dati
def save_data():
    wine_data.to_csv(DATA_FILE, index=False)

def save_producer(producer):
    global producers_data
    new_entry = pd.DataFrame([[producer]], columns=["Produttore"])
    producers_data = pd.concat([producers_data, new_entry], ignore_index=True)
    producers_data.to_csv(PRODUCERS_FILE, index=False)

def save_wine_type(wine_type):
    global wine_types_data
    new_entry = pd.DataFrame([[wine_type]], columns=["Tipologia"])
    wine_types_data = pd.concat([wine_types_data, new_entry], ignore_index=True)
    wine_types_data.to_csv(WINE_TYPES_FILE, index=False)

# Stile personalizzato
st.markdown("""
    <style>
        .big-title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #7b1fa2;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }
        .stButton > button {
            background-color: #7b1fa2;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Interfaccia Streamlit
st.markdown("<p class='big-title'>🍷 Gestione Cantina di Vini 🍷</p>", unsafe_allow_html=True)

# Menu principale con pulsanti
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, _ = st.columns(2)

if col1.button("Aggiungi un vino"):
    st.session_state.page = "add_wine"
if col2.button("Aggiungi un movimento"):
    st.session_state.page = "add_movement"
if col3.button("Controlla lo stock"):
    st.session_state.page = "check_stock"
if col4.button("Vedi statistiche"):
    st.session_state.page = "view_stats"
if col5.button("Gestisci produttori e tipologie"):
    st.session_state.page = "manage_data"

st.markdown("</div>", unsafe_allow_html=True)

# Gestione della navigazione tra le pagine
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "add_wine":
    st.header("🍇 Aggiungi un nuovo vino")
    name = st.text_input("Nome del vino")
    year = st.number_input("Anno", min_value=1900, max_value=2100, step=1)
    type = st.selectbox("Tipologia", wine_types_data["Tipologia"].dropna().unique())
    winery = st.selectbox("Cantina produttrice", producers_data["Produttore"].dropna().unique())
    quantity = st.number_input("Quantità", min_value=0, step=1)
    notes = st.text_area("Note personali")

    if st.button("Aggiungi Vino"):
        new_entry = pd.DataFrame([[name, year, type, winery, quantity, notes]],
                                  columns=wine_data.columns)
        wine_data = pd.concat([wine_data, new_entry], ignore_index=True)
        save_data()
        st.success("Vino aggiunto con successo!")
        st.rerun()

elif st.session_state.page == "add_movement":
    st.header("📦 Aggiungi un movimento")
    st.write("Funzione in sviluppo...")

elif st.session_state.page == "check_stock":
    st.header("📋 Lista dei Vini in Cantina")
    st.dataframe(wine_data)

elif st.session_state.page == "view_stats":
    st.header("📊 Statistiche sui vini")
    st.write("Funzione in sviluppo...")

elif st.session_state.page == "manage_data":
    st.header("🛠️ Gestisci Produttori e Tipologie")
    st.subheader("Aggiungi un nuovo produttore")
    new_producer = st.text_input("Nome del produttore")
    if st.button("Aggiungi Produttore"):
        save_producer(new_producer)
        st.success("Produttore aggiunto con successo!")
        st.rerun()
    
    st.subheader("Aggiungi una nuova tipologia di vino")
    new_wine_type = st.text_input("Nome della tipologia")
    if st.button("Aggiungi Tipologia"):
        save_wine_type(new_wine_type)
        st.success("Tipologia aggiunta con successo!")
        st.rerun()
    
    st.subheader("Lista Produttori")
    st.dataframe(producers_data)
    
    st.subheader("Lista Tipologie di Vino")
    st.dataframe(wine_types_data)
