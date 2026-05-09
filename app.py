import streamlit as st
import plotly.graph_objects as go
from solver import simular_seir

# Configuração inicial da página
st.set_page_config(page_title="Simulador SEIR", layout="wide")

# ==========================================
# BARRA LATERAL (SIDEBAR) - Entradas do Usuário
# ==========================================
st.sidebar.title("Parâmetros da Simulação")
st.sidebar.markdown("Ajuste as variáveis abaixo para simular diferentes cenários.")

# Sliders interativos para coletar dados do usuário
N = st.sidebar.slider("População Total", min_value=1000, max_value=1000000, value=100000, step=1000)
dias = st.sidebar.slider("Dias de Simulação", min_value=30, max_value=365, value=150, step=5)
t_incubacao = st.sidebar.slider("Tempo de Incubação (dias)", min_value=1.0, max_value=20.0, value=5.2, step=0.1)
t_infeccao = st.sidebar.slider("Duração da Infecção (dias)", min_value=1.0, max_value=20.0, value=2.9, step=0.1)
R0 = st.sidebar.slider("R0 (Ritmo Básico de Reprodução)", min_value=0.5, max_value=10.0, value=2.5, step=0.1)

# ==========================================
# CORPO PRINCIPAL - Explicação e Gráficos
# ==========================================
st.title("🦠 Simulador Epidemiológico SEIR")

# Explicação teórica didática para os usuários
st.markdown("""
Este aplicativo simula a propagação de uma doença infecciosa usando o **Modelo SEIR**. 
A população é dividida em quatro compartimentos ao longo do tempo:
* **(S) Suscetíveis:** Pessoas que podem contrair a doença.
* **(E) Expostos:** Pessoas infectadas, mas ainda no período de incubação (não transmitem).
* **(I) Infectados:** Pessoas que estão doentes e podem transmitir o vírus.
* **(R) Recuperados:** Pessoas que se curaram (ou faleceram) e adquiriram imunidade.
""")

try:
    # Chama a função do solver.py para gerar os dados
    df_resultado = simular_seir(N, dias, t_incubacao, t_infeccao, R0)
    
    # Criação do gráfico interativo usando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_resultado['Dia'], y=df_resultado['Suscetíveis'], mode='lines', name='Suscetíveis', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df_resultado['Dia'], y=df_resultado['Expostos'], mode='lines', name='Expostos', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=df_resultado['Dia'], y=df_resultado['Infectados'], mode='lines', name='Infectados', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df_resultado['Dia'], y=df_resultado['Recuperados'], mode='lines', name='Recuperados', line=dict(color='green')))
    
    fig.update_layout(
        title="Curvas do Modelo SEIR ao longo do Tempo",
        xaxis_title="Dias",
        yaxis_title="Número de Indivíduos",
        hovermode="x unified", # Facilita a leitura mostrando todos os valores de um dia específico
        legend_title="Estados"
    )
    
    # Renderiza o gráfico na interface
    st.plotly_chart(fig, use_container_width=True)
    
    # ==========================================
    # FUNCIONALIDADE SECUNDÁRIA - Tabela Expansível
    # ==========================================
    with st.expander("📊 Ver Tabela de Dados Diários Brutos"):
        st.markdown("Consulte os números exatos calculados pelo modelo para cada dia da simulação.")
        # Exibe o dataframe arredondando os valores para não mostrar "frações de pessoas"
        st.dataframe(df_resultado.round(0).astype(int), use_container_width=True)

except Exception as e:
    # Tratamento de erro elegante na interface
    st.error(f"Erro ao processar a simulação: {e}")
