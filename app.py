import io
import urllib.parse
from fpdf import FPDF
import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="YOUBRAND - Raccolta Ordini Salone", page_icon="🛍️", layout="centered"
)

# Stile CSS personalizzato
st.markdown(
    """
    <style>
    .main { background-color: #121212; }
    .stTextInput input, .stTextArea textarea { background-color: #ffffff; color: #333333; }
    div.stDownloadButton > button { background-color: #D4AF37; color: #111111; font-weight: bold; width: 100%; font-size: 18px; padding: 12px; border-radius: 6px; border: none; }
    div.stDownloadButton > button:hover { background-color: #f3e5ab; color: #111111; }
    </style>
""",
    unsafe_allow_html=True,
)

# BLOCCO LOGO YOUBRAND UFFICIALE
st.markdown(
    """
    <div style="text-align: center; background: #111111; padding: 30px 15px; border-radius: 12px; border: 3px solid #D4AF37; margin-bottom: 25px; box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.2);">
        <div style="color: #D4AF37; font-size: 26px; font-family: 'Times New Roman', serif; font-weight: bold; letter-spacing: 2px;">
            ≈ CREA LA TUA LINEA ≈
        </div>
        <div style="border-bottom: 2px solid #D4AF37; width: 70%; margin: 12px auto;"></div>
        <div style="color: #FCE288; font-size: 44px; font-family: 'Times New Roman', serif; font-weight: bold; letter-spacing: 4px; margin: 10px 0;">
            YOUBRAND
        </div>
        <div style="color: #D4AF37; font-size: 13px; font-family: Arial, sans-serif; font-weight: bold; letter-spacing: 2px; line-height: 1.6;">
            PRODOTTI PERSONALIZZATI<br>
            PER BARBER • PARRUCCHIERI • ED ESTETISTE
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.subheader("📍 Anagrafica Cliente / Salone")

ragione_sociale = st.text_input(
    "Ragione Sociale / Nome e Cognome *", placeholder="Es. Salone Bellessere"
)
indirizzo = st.text_input("Indirizzo", placeholder="Es. Via Roma, 15")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    cap = st.text_input("CAP", placeholder="CAP")
with col2:
    citta = st.text_input("Città", placeholder="Città")
with col3:
    provincia = st.text_input("Provincia", placeholder="Prov")

col4, col5 = st.columns(2)
with col4:
    piva = st.text_input("Partita IVA", placeholder="11 cifre", max_chars=11)
with col5:
    cf = st.text_input("Codice Fiscale", placeholder="C.F. o P.IVA")

telefono = st.text_input("Telefono", placeholder="Telefono")
codice_univoco = st.text_input("Cod. Univoco (SDI) / PEC", placeholder="SDI o PEC")
email = st.text_input("Email", placeholder="Email aziendale")

# BLOCCO NOTE E CONDIZIONI VISIBILE A SCHERMO
st.markdown("---")
with st.expander(
    "📌 **NOTE E CONDIZIONI GENERALI DI VENDITA (Leggi Prima di Ordinare)**",
    expanded=True,
):
    st.markdown(
        """
        * **Invio File e Logo:**Inviare l'ordine ed eventuali file grafici (possibilmente vettoriale) per email a : grafica@youbrand.info ,  con indicazione sui colori preferiti per l'etichetta.
        * **Ordine di Prova:** Nel caso di un ordine di prova, verrà prodotta una sola grafica (etichetta) su un prodotto a scelta da indicare nell'email.
        * **Minimi d'Ordine:** L'ordine minimo per la personalizzazione sarà di **12 pz per referenza**, per un **minimo di 6 referenze**.
        * **Studio Grafico:** Il costo dello studio grafico sarà di **EUR 100 una tantum** (comprensive tutte le grafiche), che verrà fatturato sull'ordine definitivo.  A meno che provvediate voi a fornirci le grafiche.
        * **Costo Etichette Aggiuntive:**
            * *Etichetta 2 Colori Semplice:* **EUR 0,12 CAD.**
            * *Etichetta 2 Colori con lavorazioni particolari (3D / Lucido / Opaco):* **EUR 0,22 CAD.**
            * *Etichetta Quadricromia con lavorazioni particolari (3D / Lucido / Opaco):* **EUR 0,32 CAD.**
        * **Servizi Extra:** Realizzazione foto prodotti e brochure PDF della linea per conto del cliente: **EUR 150,00**.
        """
    )

st.markdown("---")
st.subheader("📦 Listino Prodotti")

# Catalogo prodotti
catalogo = [
    {
        "cat": "LINEA SHAVING",
        "name": "GEL RASATURA 300 ML (Vaso Clear Dispenser)",
        "price": 4.48,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "GEL RASATURA 750 ML (Flacone Square Disp.)",
        "price": 7.68,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "PRE POST RASATURA 250 ML (Vasetto Bianco)",
        "price": 5.28,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "SPRAY RASATURA WATER ZERO 120ML",
        "price": 6.24,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE CREAM 250 ML (Terre Hermes)",
        "price": 5.44,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE CREAM KINGSTON 250 ML",
        "price": 7.84,
    },
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 420 ML VETRO", "price": 12.00},
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE TOP QUALITY ESSENZA PERSISTENTE",
        "price": 7.20,
    },
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Invictus)", "price": 7.20},
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 250 ML (Beach River)",
        "price": 7.20,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 480 ML (Beach River)",
        "price": 9.52,
    },
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Creed)", "price": 7.20},
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 250 ML (Dark Afgano)",
        "price": 7.20,
    },
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Megamare)", "price": 7.20},
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 250 ML (Silver Mountain)",
        "price": 7.20,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 250 ML (Terre d'Hermes)",
        "price": 7.20,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 480 ML (Terre d'Hermes)",
        "price": 9.52,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 250 ML (Intense Cafe')",
        "price": 7.20,
    },
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 480 ML (Intense Cafe')",
        "price": 9.52,
    },
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Gustavo)", "price": 7.20},
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Pablo)", "price": 7.20},
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (Moncada)", "price": 7.20},
    {"cat": "LINEA SHAVING", "name": "AFTER SHAVE 250 ML (El Chapo)", "price": 7.20},
    {
        "cat": "LINEA SHAVING",
        "name": "AFTER SHAVE 100 ML (Stesse profumazioni)",
        "price": 4.16,
    },
    {
        "cat": "LINEA FINISH",
        "name": "GEL CAPELLI 500 ML (One Million)",
        "price": 4.16,
    },
    {"cat": "LINEA FINISH", "name": "GEL CAPELLI 500 ML (Invictus)", "price": 4.16},
    {
        "cat": "LINEA FINISH",
        "name": "GEL CAPELLI 500 ML (Terre d'Hermes)",
        "price": 4.16,
    },
    {
        "cat": "LINEA FINISH",
        "name": "GEL CAPELLI 500 ML (Acqua di Gio)",
        "price": 4.16,
    },
    {
        "cat": "LINEA FINISH",
        "name": "GEL CERA 500 ML EXTRA STRONG (Terre d'Hermes)",
        "price": 4.64,
    },
    {"cat": "LINEA FINISH", "name": "WATER WAX 100 ML (Invictus)", "price": 3.60},
    {"cat": "LINEA FINISH", "name": "WATER WAX 100 ML (Cocco)", "price": 3.60},
    {"cat": "LINEA FINISH", "name": "WATER WAX 100 ML (Megamare)", "price": 3.60},
    {"cat": "LINEA FINISH", "name": "MATTE WAX 100 ML", "price": 4.16},
    {
        "cat": "LINEA FINISH",
        "name": "MATT WAX 100 ML ULTRAMATT (Mango)",
        "price": 5.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "MATT WAX CEMENT 100 ML (Argilla)",
        "price": 5.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA LUCIDA NERA 100ML (Black Water Wax)",
        "price": 5.52,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA MATTE MANGO CUBA NARCOS 120GR",
        "price": 7.84,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA MATTE ARGILLA JAMAICA NARCOS 120GR",
        "price": 7.84,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA MATTE MANGO CUBA NARCOS 260GR",
        "price": 13.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA MATTE ARGILLA JAMAICA NARCOS 260GR",
        "price": 13.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA ROSSA FORTE NARCOS 120GR",
        "price": 7.84,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA BLU MEDIA NARCOS 120GR",
        "price": 7.84,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA ROSSA FORTE NARCOS 260GR",
        "price": 13.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA BLU MEDIA NARCOS 260GR",
        "price": 13.60,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA CARAMEL POMADE NARCOS 120GR",
        "price": 7.84,
    },
    {
        "cat": "LINEA FINISH",
        "name": "CERA SEMILUCIDA CARAMEL POMADE NARCOS 260GR",
        "price": 13.60,
    },
    {"cat": "LINEA FINISH", "name": "CERA IN POLVERE 20GR NARCOS", "price": 5.12},
    {"cat": "LINEA FINISH", "name": "CERA IN POLVERE 30GR NARCOS", "price": 7.92},
    {"cat": "LINEA FINISH", "name": "CERA LIQUIDA 100ML", "price": 7.20},
    {"cat": "LINEA FINISH", "name": "CERA BARBA E BAFFI 50ML", "price": 4.72},
    {
        "cat": "LINEA FINISH",
        "name": "CREMA DEFINIZIONE RICCI 150 ML COCCO",
        "price": 7.84,
    },
    {"cat": "LINEA FINISH", "name": "SEA SALT SPRAY 150ML", "price": 5.52},
    {
        "cat": "LINEA FINISH",
        "name": "PROTETTORE TERMICO 150ML CON TRIGGER",
        "price": 5.52,
    },
    {"cat": "LINEA FINISH", "name": "PROFUMO CAPELLI 50ML BIANCO LATTE", "price": 5.92},
    {
        "cat": "LINEA FINISH",
        "name": "SPRAY BIFASICO 150ML CON TRIGGER",
        "price": 5.52,
    },
    {"cat": "LINEA FINISH", "name": "MOUSSE CAPELLI RICCI E VANIGLIA", "price": 6.72},
    {"cat": "LINEA FINISH", "name": "BLAST FOAM MOUSSE AD ACQUA RICCI", "price": 8.00},
    {"cat": "LINEA FINISH", "name": "LACCA FORTE O EXTRA FORTE 500ML", "price": 7.20},
    {
        "cat": "WHITE LABEL BEARD CARE",
        "name": "BALSAMO DA BARBA ANTICRESPO 100ML",
        "price": 7.42,
    },
    {"cat": "WHITE LABEL BEARD CARE", "name": "SHAMPOO DA BARBA 100ML", "price": 4.72},
    {
        "cat": "WHITE LABEL BEARD CARE",
        "name": "SHAMPOO DA BARBA 100ML EXTASY",
        "price": 5.20,
    },
    {
        "cat": "WHITE LABEL BEARD CARE",
        "name": "OLIO DA BARBA 50ML LEGNO E SPEZIE",
        "price": 7.20,
    },
    {
        "cat": "WHITE LABEL BEARD CARE",
        "name": "OLIO DA BARBA 50ML COCO GOLD OIL",
        "price": 7.20,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "TRATTAMENTO NANOPLASTIA SUD-AMERICA 1000ML",
        "price": 88.00,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "TRATTAMENTO NANOPLASTIA SUD-AMERICA 150ML",
        "price": 15.20,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "SHAMPOO POST TRATTAMENTO SENZA SALE 250ML",
        "price": 4.64,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "SHAMPOO POST TRATTAMENTO SENZA SALE 500ML",
        "price": 7.84,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "SHAMPOO POST TRATTAMENTO SENZA SALE 1000ML",
        "price": 15.20,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "MASCHERA MANTENIMENTO 250ML",
        "price": 7.12,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "MASCHERA MANTENIMENTO 500ML",
        "price": 10.32,
    },
    {
        "cat": "WHITE LABEL NANOPLASTIA",
        "name": "MASCHERA MANTENIMENTO 1000ML",
        "price": 17.44,
    },
    {
        "cat": "WHITE LABEL TECNICO",
        "name": "DECOLORANTE BLUE IN BUSTA 500GR",
        "price": 6.88,
    },
    {
        "cat": "WHITE LABEL TECNICO",
        "name": "DECOLORANTE BLUE IN VASO 500GR",
        "price": 9.28,
    },
    {
        "cat": "WHITE LABEL TECNICO",
        "name": "SMACCHIATORE IN CREMA 100ML",
        "price": 5.38,
    },
    {"cat": "WHITE LABEL TECNICO", "name": "BARRIERA IN CREMA 100ML", "price": 6.24},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO DUAL DRUG 2IN1 250ML",
        "price": 5.20,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO ANTI CADUTA 250ML",
        "price": 6.96,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO ANTI FORFORA E GRASSO 250ML",
        "price": 6.96,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MIRACLE SHAMPOO RISTRUTTURANTE 250ML",
        "price": 4.64,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MIRACLE SHAMPOO RISTRUTTURANTE 1000ML",
        "price": 12.00,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO CHERATINA 250ML",
        "price": 5.20,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA CHERATINA 250ML",
        "price": 6.32,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SPRAY ALLA CHERATINA 150ML",
        "price": 5.20,
    },
    {"cat": "WHITE LABEL HAIR CARE", "name": "SHAMPOO ARGAN 250ML", "price": 5.20},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO ANTIGIALLO 250ML",
        "price": 4.72,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO ANTICRESPO 250ML",
        "price": 4.72,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA ANTICRESPO 250ML",
        "price": 6.32,
    },
    {"cat": "WHITE LABEL HAIR CARE", "name": "SPRAY BIPHASICO 150ML", "price": 5.76},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SUPREMO 10 IN 1 150ML", "price": 6.08},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SPRAY NO FRIZZ 150ML", "price": 5.28},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SHAMPOO RICCI 250ML", "price": 4.72},
    {"cat": "WHITE LABEL HAIR CARE", "name": "MASCHERA RICCI 250ML", "price": 6.08},
    {"cat": "WHITE LABEL HAIR CARE", "name": "MOUSSE RICCI 200ML", "price": 6.24},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "LOZIONE URTO ANTICADUTA 100ML",
        "price": 12.16,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "LOZIONE URTO ANTIFORFORA E GRASSO 100ML",
        "price": 12.16,
    },
    {"cat": "WHITE LABEL HAIR CARE", "name": "SCRUB PEELING CUTE 100ML", "price": 4.72},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SHAMPOO BOTOX 250ML", "price": 5.20},
    {"cat": "WHITE LABEL HAIR CARE", "name": "MASCHERA BOTOX 250ML", "price": 6.08},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SPRAY BOTOX 150ML", "price": 5.44},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO LAVAGGI FREQUENTI 250ML",
        "price": 4.72,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA LAVAGGI FREQUENTI IDRA 250ML",
        "price": 6.08,
    },
    {"cat": "WHITE LABEL HAIR CARE", "name": "MOUSSE FIX ENERGY 200ML", "price": 6.32},
    {"cat": "WHITE LABEL HAIR CARE", "name": "MAGIC KERATIN OIL 100ML", "price": 6.88},
    {"cat": "WHITE LABEL HAIR CARE", "name": "SPRAY LUCIDANTE 150ML", "price": 8.22},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SHAMPOO ILLUMINANTE AL COCCO 250ML",
        "price": 5.84,
    },
    {"cat": "WHITE LABEL HAIR CARE", "name": "CREMA LISCIANTE 150ML", "price": 7.92},
    {"cat": "WHITE LABEL HAIR CARE", "name": "CERA STICK 75GR", "price": 7.68},
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA AL LATTE DA LAVAGGIO 1000ML",
        "price": 6.32,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "TANICA SHAMPOO AL CARAMELLO 10000ML",
        "price": 20.00,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "LACCA ECOLOGICA VOLUMIZZANTE 300ML",
        "price": 8.00,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "LACCA ECOLOGICA DIREZIONALE 300ML",
        "price": 8.00,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "BOOSTER TECNICO PURO 4 TIPOLOGIE 30ML",
        "price": 7.20,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA MIRACOLOSA FIALA 10PZ",
        "price": 15.68,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA COCCO FIALA 10PZ",
        "price": 15.68,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "MASCHERA ILLUMINANTE AL COCCO 250ML",
        "price": 12.00,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SPRAY LAMINAZIONE COCCO 12IN1 50ML",
        "price": 7.84,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SPRAY LAMINAZIONE COCCO 12IN1 100ML",
        "price": 11.04,
    },
    {
        "cat": "WHITE LABEL HAIR CARE",
        "name": "SPRAY LAMINAZIONE COCCO 12IN1 200ML",
        "price": 15.20,
    },
    {
        "cat": "WHITE LABEL FIBRE",
        "name": "FIBRE PER CAPELLI 3 COLORI",
        "price": 10.40,
    },
    {"cat": "BODY AND SKIN MAN", "name": "SCRUB VISO E BARBA 50ML", "price": 6.32},
    {
        "cat": "BODY AND SKIN MAN",
        "name": "CREMA IDRATANTE VISO LENITIVA POST RASATURA 50ML",
        "price": 6.32,
    },
    {"cat": "BODY AND SKIN MAN", "name": "MASCHERA ARGILLA 50ML", "price": 6.32},
    {"cat": "PRODOTTI VISO", "name": "SCRUB VISO 100 TUBO", "price": 4.72},
    {"cat": "PRODOTTI VISO", "name": "SCRUB VISO 250 VASO", "price": 7.34},
    {
        "cat": "PRODOTTI VISO",
        "name": "LATTE DETERGENTE PELLI MISTE 250 MANDORLE E ALOE",
        "price": 5.20,
    },
    {"cat": "PRODOTTI VISO", "name": "TONICO HYDRA VISAGE 250 ALLA ROSA", "price": 4.08},
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA IDRATANTE VISO 50 AIRLESS",
        "price": 6.16,
    },
    {"cat": "PRODOTTI VISO", "name": "CREMA IDRATANTE VISO 250 VASO", "price": 7.76},
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA BAVA DI LUMACA SUPERIDRATANTE 50 AIRLESS",
        "price": 12.00,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA IDRATANTE AL COENZIMA Q10 50 AIRLESS",
        "price": 6.72,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "SIERO IDRATANTE ACIDO JALURONICO 30 AIRLESS",
        "price": 12.48,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA ANTIRUGHE VISAGE C + RETINOLO 50 AIRLESS",
        "price": 6.72,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA ANTIRUGHE EFFETTO LIFTING 50 AIRLESS",
        "price": 6.72,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA ANTIRUGHE EFFETTO LIFTING 250 VASO",
        "price": 8.80,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MASCHERA ANTIRUGHE VISAGE C + RETINOLO 250 VASO",
        "price": 8.80,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "SIERO ANTIETA' BAVA DI LUMACA 30 AIRLESS",
        "price": 12.48,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "SIERO VISO/OCCHI SIERO DI VIPERA 30 AIRLESS",
        "price": 12.48,
    },
    {"cat": "PRODOTTI VISO", "name": "CREMA NUTRIENTE 50 AIRLESS", "price": 6.72},
    {"cat": "PRODOTTI VISO", "name": "CREMA NUTRIENTE 250 VASO", "price": 8.80},
    {
        "cat": "PRODOTTI VISO",
        "name": "SIERO NUTRIENTE CELLULE STAMINALI 30 AIRLESS",
        "price": 12.48,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "CREMA VISO COUPEROSE DERMO PROTETTIVA 50 AIRLESS",
        "price": 6.72,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MASCHERA CALMANTE ALLA CAROTA 250 VASO",
        "price": 8.80,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "GLYCO+ LATTE ACIDO GLICOLICO 8% 150ML",
        "price": 7.20,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "GLYCO+ TONICO ACIDO GLICOLICO 8% 150ML",
        "price": 7.04,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "GLYCO+ 20% ACTIVE SOLUTION 150",
        "price": 10.24,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "GLYCO+ 40% ACTIVE SOLUTION 150",
        "price": 16.64,
    },
    {"cat": "PRODOTTI VISO", "name": "GLYCO+ NEUTRALIZER 300", "price": 5.74},
    {"cat": "PRODOTTI VISO", "name": "ACIDO GLICOLICO 10% 50 AIRLESS", "price": 7.20},
    {
        "cat": "PRODOTTI VISO",
        "name": "MANDELYC+ LATTE ACIDO MANDELICO 150",
        "price": 7.20,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MANDELYC+ TONICO ACIDO MANDELICO 150",
        "price": 7.04,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MANDELYC+ CREMA ACIDO MANDELICO 3% 50 AIRLESS",
        "price": 7.68,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MANDELYC+ SIERO ACIDO MANDELICO 15% 30 AIRLESS",
        "price": 14.08,
    },
    {
        "cat": "PRODOTTI VISO",
        "name": "MANDELYC+ ACIDO MANDELICO SOLUTION 40% 150",
        "price": 20.00,
    },
    {"cat": "PRODOTTI VISO", "name": "COLLAGENE MARINO 10 CON PIPETTA", "price": 6.40},
    {"cat": "PRODOTTI VISO", "name": "ACIDO JALURONICO 10 CON PIPETTA", "price": 6.40},
    {"cat": "PRODOTTI VISO", "name": "VITAMINA E PURA 10 CON PIPETTA", "price": 6.40},
    {
        "cat": "PRODOTTI CORPO",
        "name": "TALASSO SCRUB MARINO SALI ESFOLIANTI 500",
        "price": 9.44,
    },
    {"cat": "PRODOTTI CORPO", "name": "CREMA SCRUB CORPO 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "CREMA IDRATANTE CORPO 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "CREMA RIDUCENTE SNELLENTE 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "CREMA ANTICELLULITE 500", "price": 9.44},
    {
        "cat": "PRODOTTI CORPO",
        "name": "CREMA ANTICELLULITE TERMOATTIVA 500",
        "price": 9.44,
    },
    {
        "cat": "PRODOTTI CORPO",
        "name": "SNELL+ GEL FREDDO ANTICELLULITE DRENANTE 500",
        "price": 9.44,
    },
    {"cat": "PRODOTTI CORPO", "name": "BENDAGGIO CALDO 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "FANGO ANTICELLULITE 700", "price": 10.40},
    {
        "cat": "PRODOTTI CORPO",
        "name": "CREMA RASSODANTE ALLA JALURAMINA 500",
        "price": 9.44,
    },
    {
        "cat": "PRODOTTI CORPO",
        "name": "CREMA ELASTICIZZANTE ANTISMAGLIATURE 500",
        "price": 9.44,
    },
    {"cat": "PRODOTTI CORPO", "name": "BENDAGGIO FREDDO 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "CREMA MASSAGGIO POLIVALENTE 500", "price": 9.44},
    {"cat": "PRODOTTI CORPO", "name": "OLIO CORPO LINFODREN 500", "price": 10.40},
    {"cat": "PRODOTTI CORPO", "name": "OLIO MASSAGGIO ANTICELLULITE 500", "price": 10.40},
    {"cat": "PRODOTTI CORPO", "name": "OLIO MASSAGGIO RASSODANTE 500", "price": 10.40},
    {"cat": "PRODOTTI CORPO", "name": "OLIO MASSAGGIO MANDORLE DOLCI 1000", "price": 11.12},
    {"cat": "PRODOTTI CORPO", "name": "CREMA MANI ALOE 100 TUBO", "price": 3.98},
    {"cat": "PRODOTTI CORPO", "name": "CREMA PIEDI DEFATICANTE 150 TUBO", "price": 6.24},
    {"cat": "PRODOTTI CORPO", "name": "GEL FREDDO GAMBE 150 TUBO", "price": 6.24},
    {"cat": "PRODOTTI CORPO", "name": "CREMA MANI/PIEDI AL LIMONE 250 VASO", "price": 7.20},
    {
        "cat": "PRODOTTI CORPO",
        "name": "PLAYA DEL SOL GEL BRONZE CAROTA E MIRTILLO 500",
        "price": 7.92,
    },
    {
        "cat": "PRODOTTI CORPO",
        "name": "PLAYA DEL SOL GEL BRONZE BERGAMOTTO SENZA PROT. 500",
        "price": 7.92,
    },
    {
        "cat": "PRODOTTI CORPO",
        "name": "PLAYA DEL SOL GEL BRONZE BERGAMOTTO MEDIA PROT. 500",
        "price": 7.92,
    },
    {
        "cat": "PRODOTTI CORPO",
        "name": "PLAYA DEL SOL GEL BRONZE BERGAMOTTO ALTA PROT. 500",
        "price": 7.92,
    },
    {"cat": "PRODOTTI CORPO", "name": "PLAYA DEL SOL LATTE DOPOSOLE 500", "price": 6.32},
    {"cat": "PRODOTTI NAILS", "name": "ULTRA BOND 15ML", "price": 4.72},
    {"cat": "PRODOTTI NAILS", "name": "TOP COAT NO WIPE 15ML", "price": 7.20},
    {"cat": "PRODOTTI NAILS", "name": "BASE COAT 15ML", "price": 7.20},
    {"cat": "PRODOTTI NAILS", "name": "NAIL PREP 15ML", "price": 4.00},
    {"cat": "PRODOTTI NAILS", "name": "BASE RUBBER 15ML", "price": 7.20},
    {"cat": "PRODOTTI NAILS", "name": "OVERGLOSS TOP NO WIPE 15ML", "price": 9.60},
    {"cat": "PRODOTTI NAILS", "name": "OLIO CUTICOLE 15ML", "price": 4.80},
    {"cat": "PRODOTTI NAILS", "name": "INDURENTE 15ML", "price": 4.80},
    {"cat": "PRODOTTI NAILS", "name": "REMOVER CUTICOLE 15ML", "price": 5.60},
    {"cat": "PRODOTTI NAILS", "name": "PRIMER 15ML", "price": 4.72},
    {"cat": "PRODOTTI NAILS", "name": "BASE/TOP 15ML", "price": 10.40},
    {"cat": "PRODOTTI NAILS", "name": "CLEANSER 250ML", "price": 3.92},
    {"cat": "PRODOTTI NAILS", "name": "CLEANSER 500ML", "price": 5.52},
    {"cat": "PRODOTTI NAILS", "name": "CLEANSER 1000ML", "price": 8.72},
    {"cat": "PRODOTTI NAILS", "name": "REMOVER SEMIPERMANENTE 250ML", "price": 3.92},
    {"cat": "PRODOTTI NAILS", "name": "REMOVER SEMIPERMANENTE 1000ML", "price": 8.72},
    {"cat": "PRODOTTI NAILS", "name": "ACETONE PURO 1000ML", "price": 6.88},
    {"cat": "PRODOTTI NAILS", "name": "ACRYGEL SOLUTION 100ML", "price": 4.72},
]

if "qtys" not in st.session_state:
    st.session_state.qtys = {i: 0 for i in range(len(catalogo))}

current_category = ""
subtotal = 0.0

for i, prod in enumerate(catalogo):
    if prod["cat"] != current_category:
        current_category = prod["cat"]
        st.markdown(f"**📂 {current_category}**")

    cols = st.columns([3, 1, 1])
    with cols[0]:
        st.write(f"{prod['name']} (€ {prod['price']:.2f})")
    with cols[1]:
        st.session_state.qtys[i] = st.number_input(
            "Q.tà",
            min_value=0,
            max_value=999,
            value=st.session_state.qtys[i],
            key=f"prod_{i}",
            label_visibility="collapsed",
        )
    with cols[2]:
        tot_item = prod["price"] * st.session_state.qtys[i]
        subtotal += tot_item
        st.write(f"€ {tot_item:.2f}")

shipping = 10.0 if subtotal > 0 else 0.0
vat = (subtotal + shipping) * 0.22
total = subtotal + shipping + vat

st.markdown("---")

# 🎨 BLOCCO SCELTA GRAFICHE (CHECKBOX)
st.subheader("🎨 Gestione Grafiche")
col_g1, col_g2 = st.columns(2)
with col_g1:
    grafica_cliente = st.checkbox("Grafiche fornite dal cliente")
with col_g2:
    grafica_reparto = st.checkbox(
        "Grafiche gestite dal nostro reparto grafico"
    )

st.markdown("---")

note_ordine = st.text_area(
    "📝 Note aggiuntive per questo ordine specifico (opzionale)",
    placeholder="Inserisci eventuali note extra...",
)

st.markdown("---")
st.markdown("### 📊 Riepilogo Totali")
st.write(f"**Imponibile:** € {subtotal:.2f}")
st.write(f"**Trasporto:** € {shipping:.2f}")
st.write(f"**IVA 22%:** € {vat:.2f}")
st.markdown(f"### **TOTALE IVATO: € {total:.2f}**")


# Funzione per generare il PDF dell'ordine pulito e valido al 100%
def genera_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    def clean_text(txt):
        if not txt:
            return ""
        replacements = {
            "à": "a'",
            "è": "e'",
            "é": "e'",
            "ì": "i'",
            "ò": "o'",
            "ù": "u'",
            "’": "'",
            "“": '"',
            "”": '"',
            "«": '"',
            "»": '"',
            "€": "EUR",
            "≈": "",
            "•": "-",
        }
        for orig, repl in replacements.items():
            txt = txt.replace(orig, repl)
        return txt.encode("latin-1", "replace").decode("latin-1")

    # Intestazione Brand Completa nel PDF
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 6, clean_text("CREA LA TUA LINEA"), 0, 1, "C")
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, clean_text("YOUBRAND"), 0, 1, "C")
    pdf.set_font("Arial", "B", 9)
    pdf.cell(
        0,
        5,
        clean_text(
            "PRODOTTI PERSONALIZZATI PER BARBER, PARRUCCHIERI ED ESTETISTE"
        ),
        0,
        1,
        "C",
    )
    pdf.ln(8)

    # Dati Anagrafici
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 7, clean_text("ANAGRAFICA CLIENTE / SALONE"), 0, 1, "L")
    pdf.set_font("Arial", "", 10)
    pdf.cell(
        0, 6, clean_text(f"Ragione Sociale: {ragione_sociale}"), 0, 1, "L"
    )
    pdf.cell(
        0,
        6,
        clean_text(
            f"Indirizzo: {indirizzo} - {cap} {citta} ({provincia})"
        ),
        0,
        1,
        "L",
    )
    pdf.cell(0, 6, clean_text(f"P.IVA: {piva} | C.F.: {cf}"), 0, 1, "L")
    pdf.cell(
        0, 6, clean_text(f"Telefono: {telefono} | Email: {email}"), 0, 1, "L"
    )
    pdf.cell(
        0, 6, clean_text(f"Codice Univoco / PEC: {codice_univoco}"), 0, 1, "L"
    )
    pdf.ln(8)

    # Tabella Prodotti
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 7, clean_text("PRODOTTI ORDINATI"), 0, 1, "L")
    pdf.set_font("Arial", "B", 10)
    pdf.cell(110, 7, clean_text("Prodotto"), 1)
    pdf.cell(20, 7, clean_text("Q.ta"), 1, 0, "C")
    pdf.cell(30, 7, clean_text("Prezzo U."), 1, 0, "R")
    pdf.cell(30, 7, clean_text("Totale"), 1, 1, "R")

    pdf.set_font("Arial", "", 9)
    for i, prod in enumerate(catalogo):
        qta = st.session_state.qtys[i]
        if qta > 0:
            tot_prod = prod["price"] * qta
            pdf.cell(110, 6, clean_text(str(prod["name"][:50])), 1)
            pdf.cell(20, 6, str(qta), 1, 0, "C")
            pdf.cell(30, 6, f"EUR {prod['price']:.2f}", 1, 0, "R")
            pdf.cell(30, 6, f"EUR {tot_prod:.2f}", 1, 1, "R")

    pdf.ln(5)

    # SEZIONE SCELTA GRAFICHE NEL PDF
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 6, clean_text("GESTIONE GRAFICHE:"), 0, 1, "L")
    pdf.set_font("Arial", "", 9)
    val_g1 = "[X] Grafiche fornite dal cliente" if grafica_cliente else "[ ] Grafiche fornite dal cliente"
    val_g2 = "[X] Grafiche gestite dal nostro reparto grafico" if grafica_reparto else "[ ] Grafiche gestite dal nostro reparto grafico"
    pdf.cell(0, 5, clean_text(val_g1), 0, 1, "L")
    pdf.cell(0, 5, clean_text(val_g2), 0, 1, "L")
    pdf.ln(5)

    # Totali
    pdf.set_font("Arial", "B", 10)
    pdf.cell(160, 6, clean_text("Imponibile:"), 0, 0, "R")
    pdf.cell(30, 6, f"EUR {subtotal:.2f}", 0, 1, "R")
    pdf.cell(160, 6, clean_text("Trasporto:"), 0, 0, "R")
    pdf.cell(30, 6, f"EUR {shipping:.2f}", 0, 1, "R")
    pdf.cell(160, 6, clean_text("IVA 22%:"), 0, 0, "R")
    pdf.cell(30, 6, f"EUR {vat:.2f}", 0, 1, "R")
    pdf.set_font("Arial", "B", 12)
    pdf.cell(160, 8, clean_text("TOTALE IVATO:"), 0, 0, "R")
    pdf.cell(30, 8, f"EUR {total:.2f}", 0, 1, "R")
    pdf.ln(8)

    # NOTE AGGIUNTIVE SPECIFICHE
    if note_ordine.strip():
        pdf.set_font("Arial", "B", 9)
        pdf.cell(0, 5, clean_text("NOTE AGGIUNTIVE:"), 0, 1, "L")
        pdf.set_font("Arial", "", 8)
        pdf.multi_cell(0, 4, clean_text(note_ordine.strip()), 1)
        pdf.ln(5)

    # NOTE E CONDIZIONI FISSE
    pdf.set_font("Arial", "B", 9)
    pdf.cell(0, 5, clean_text("NOTE E CONDIZIONI GENERALI:"), 0, 1, "L")
    pdf.set_font("Arial", "", 7)

    testo_note = (
        "- Inviare l'ordine ed eventuali file grafici (possibilmente vettoriale) per email a : grafica@youbrand.info ,  con indicazione sui colori preferiti per l'etichetta.\n"
        "- Nel caso di un ordine di prova, verra' prodotta una sola grafica (etichetta) su un prodotto a scelta da indicare nell'email.\n"
        "- L'ordine minimo per la personalizzazione sara' di 12 pz per referenza minimo 6 referenze.\n"
        "- Il costo dello studio grafico sara' di EUR 100 una tantum (comprensive tutte le grafiche), che verra' fatturato sull'ordine definitivo. A meno che provvediate voi a fornirci le grafiche.\n"
        "- Il costo di ogni etichetta da aggiungere al prodotto sara' cosi' determinato:\n"
        "  * COSTO ETICHETTA A 2 COLORI SEMPLICE EUR 0,12 CAD.\n"
        "  * COSTO ETICHETTA A 2 COLORI CON LAVORAZIONI PARTICOLARI ANCHE 3D E/O LUCIDO/OPACO EUR 0,22 CAD.\n"
        "  * COSTO ETICHETTA QUADRICROMIA CON LAVORAZIONI ANCHE PARTICOLARI 3D E/O LUCIDO/OPACO EUR 0,32 CAD.\n"
        "- Inoltre possiamo effettuare REALIZZAZIONE FOTO PRODOTTI E BROCHURE PDF DELLA LINEA PER CONTO DEL CLIENTE EUR 150,00"
    )

    pdf.multi_cell(0, 3.5, clean_text(testo_note), 1)

    # Output binario pulito per Streamlit
    pdf_output = pdf.output(dest="S")
    if isinstance(pdf_output, str):
        return pdf_output.encode("latin-1")
    return bytes(pdf_output)


# Generazione e pulsante di scaricamento PDF
if not ragione_sociale.strip() or subtotal == 0:
    st.info(
        "Compila la Ragione Sociale e seleziona almeno un prodotto per abilitare il download del PDF."
    )
else:
    pdf_data = genera_pdf()

    st.download_button(
        label="📄 Scarica Ordine in PDF",
        data=pdf_data,
        file_name=f"Ordine_{ragione_sociale.replace(' ', '_')}.pdf",
        mime="application/pdf",
    )
