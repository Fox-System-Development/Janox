import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="Janox BI - Performance", layout="wide")

st.markdown("""
    <style>
        /* Remove o padding do container de visualização principal */
        [data-testid="stAppViewContainer"] {
            padding: 0rem !important;
        }

        /* Ajusta a área principal para não sobrepor a sidebar */
        [data-testid="stMainViewContainer"] {
            padding: 0rem !important;
        }

        /* Zera as margens do bloco de conteúdo onde fica o BI */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* Esconde o cabeçalho mas mantém a funcionalidade da sidebar */
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
            border: none;
        }

        /* Garante que o iframe ocupe a largura total disponível */
        iframe {
            border: none !important;
            width: 100% !important;
        }

        /* Estilização básica para o rodapé da sidebar */
        .footer-fox {
            position: fixed;
            bottom: 20px;
            left: 20px;
            font-size: 12px;
            color: #6c757d;
        }
        .footer-fox a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True)

#Vendedores
telas = {
    "📊 Visão Geral": "9646ffcb14e85fa2adf4",
    "👤 Arthur": "068bfb5551b049c00271",
    "👤 Júlio Cesar": "ba7466568c206d700536",
    "👤 Livian": "0a0db2b850767d5f3f9b",
    "👤 Marcio": "d1c3c0c7e74bb1e5719b",
    "👤 Miguel": "7fce0ef3ee0964b7ab6b",
    "👤 Thais": "654e7dc6f349ae3dec5c",
}
nomes_vendedores = list(telas.keys())

if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'auto_loop' not in st.session_state:
    st.session_state.auto_loop = True

with st.sidebar:
    st.title("Fox System")
    st.subheader("Projeto Janox")
    
    escolha = st.radio(
        "Selecione o Relatório:",
        nomes_vendedores,
        index=st.session_state.indice
    )
    
    st.divider()
    st.session_state.auto_loop = st.toggle("Giro Automático (30s)", value=st.session_state.auto_loop)
    
    st.markdown("---")
    st.markdown(
        'Desenvolvido por [Fox Development](https://github.com/Fox-System-Development)', 
        unsafe_allow_html=True
    )

novo_indice = nomes_vendedores.index(escolha)
if novo_indice != st.session_state.indice:
    st.session_state.indice = novo_indice
    st.rerun()

url_base = "https://app.powerbi.com/reportEmbed?reportId=fc3f2b99-27c1-4737-8b5a-4a056d928ea1&autoAuth=true&ctid=07bd24b4-6a91-4018-a004-47134c9ac99f"
id_pagina = telas[nomes_vendedores[st.session_state.indice]]

url_final = f"{url_base}&pageName={id_pagina}&navContentPaneEnabled=false"

components.iframe(url_final, height=830)

if st.session_state.auto_loop:
    time.sleep(30)
    st.session_state.indice = (st.session_state.indice + 1) % len(nomes_vendedores)
    st.rerun()