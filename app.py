import streamlit as st
import streamlit.components.v1 as components
import time

# 1. Configuração da página
st.set_page_config(page_title="Janox BI - Performance", layout="wide")

# 2. CSS Ajustado (Garante cliques na sidebar e remove espaços brancos)
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

# 3. Lista de Vendedores
telas = {
    "📊 Visão Geral": "ReportSection",
    "👤 Vendedor 1": "ReportSection1",
    "👤 Vendedor 2": "ReportSection2",
    "👤 Vendedor 3": "ReportSection3",
}
nomes_vendedores = list(telas.keys())

# 4. Estado da Sessão
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'auto_loop' not in st.session_state:
    st.session_state.auto_loop = True

# 5. Sidebar com Navegação e Rodapé
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
    
    # Rodapé com link para o GitHub
    st.markdown("---")
    st.markdown(
        'Desenvolvido por [Fox Development](https://github.com/Fox-System-Development)', 
        unsafe_allow_html=True
    )

# Sincronização manual
novo_indice = nomes_vendedores.index(escolha)
if novo_indice != st.session_state.indice:
    st.session_state.indice = novo_indice
    st.rerun()

# 6. Exibição do Power BI
url_base = "https://playground.powerbi.com/sampleReportEmbed"
id_pagina = telas[nomes_vendedores[st.session_state.indice]]
url_final = f"{url_base}?pageName={id_pagina}&navContentPaneEnabled=false"

components.iframe(url_final, height=920)

# 7. Lógica do Temporizador
if st.session_state.auto_loop:
    time.sleep(30)
    st.session_state.indice = (st.session_state.indice + 1) % len(nomes_vendedores)
    st.rerun()