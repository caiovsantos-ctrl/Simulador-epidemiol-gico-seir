import numpy as np
from scipy.integrate import odeint
import pandas as pd

def equacoes_seir(y, t, N, beta, sigma, gamma):
    """
    Define as equações diferenciais do modelo SEIR.
    """
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

def simular_seir(N, dias, t_incubacao, t_infeccao, R0):
    """
    Resolve o modelo SEIR e retorna um DataFrame do Pandas.
    
    Parâmetros:
    N: População total
    dias: Tempo de simulação em dias
    t_incubacao: Tempo médio de incubação da doença (dias)
    t_infeccao: Tempo médio de duração da infecção (dias)
    R0: Número básico de reprodução
    """
    
    # 1. Validações lógicas de entrada
    if N <= 0:
        raise ValueError("A população total deve ser maior que zero.")
    if dias <= 0:
        raise ValueError("O número de dias de simulação deve ser maior que zero.")
    if t_incubacao <= 0 or t_infeccao <= 0:
        raise ValueError("Os tempos de incubação e infecção devem ser maiores que zero.")
    
    # 2. Derivação dos parâmetros das taxas
    sigma = 1.0 / t_incubacao
    gamma = 1.0 / t_infeccao
    beta = R0 * gamma 
    
    # 3. Condições Iniciais
    I0 = 1 # Começamos sempre com 1 pessoa infectada
    E0 = 0 # Sem expostos inicialmente
    R0_estado = 0 # Sem recuperados inicialmente
    S0 = N - I0 - E0 - R0_estado # O resto da população é suscetível
    
    y0 = S0, E0, I0, R0_estado
    
    # 4. Vetor de tempo (dias)
    t = np.linspace(0, dias, dias)
    
    # 5. Resolução das equações diferenciais usando o Scipy
    solucao = odeint(equacoes_seir, y0, t, args=(N, beta, sigma, gamma))
    S, E, I, R = solucao.T
    
    # 6. Formatação e retorno dos resultados em DataFrame
    df = pd.DataFrame({
        'Dia': np.arange(dias),
        'Suscetíveis': S,
        'Expostos': E,
        'Infectados': I,
        'Recuperados': R
    })
    
    return df
