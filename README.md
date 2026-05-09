# Simulador Epidemiológico Interativo: Modelo SEIR

## 1. Título e Descrição
O **Simulador Epidemiológico SEIR** é um projeto de caráter acadêmico desenvolvido com o Gemini Pro para  ilustrar a ' INsustentabilidade da mera prática de desenvolvimento de código, per si , como uma atividade da chamada "escola de cursos superiores" ' e que um estudante, mesmo de 1º semestre, assumido sem conhecimento prévio algum, é capaz de construir e hospedar um código minimamente complexo e que funcione a contento e que ele não entende nem a complexidade do problema, nem tampouco a do código escrito.

O aplicativo simula o espalhamento de doenças infecciosas modelando a transição da população através de quatro estados: Suscetíveis, Expostos, Infectados e Recuperados.
**Funcionalidades:**
* Configuração interativa de parâmetros epidemiológicos (R0, Tempo de incubação, etc).
* Gráficos dinâmicos com *hover* para análise de curvas de contágio.
* Tabela expansível de dados determinísticos diários.

## 2. Tecnologias Utilizadas
O projeto foi inteiramente concebido em **Python** e se apoia nas seguintes bibliotecas:
* **Streamlit:** Construção rápida e reativa da interface web (frontend).
* **Numpy:** Operações matemáticas vetorizadas e manipulação de arrays.
* **Scipy:** Resolução do sistema de Equações Diferenciais Ordinárias (ODE) com a função `odeint`.
* **Pandas:** Armazenamento, formatação e manipulação dos resultados estruturados em DataFrames.
* **Plotly:** Construção das renderizações gráficas interativas em formato de linhas.

## 3. Passo a Passo para Execução

Siga os passos abaixo para rodar o simulador localmente na sua máquina:

1. **Clone o repositório:**
   
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio
   

2. Crie e ative um ambiente virtual (Recomendado):

No Windows:
  python -m venv venv
  venv\Scripts\activate

No Linux/Mac:
  python3 -m venv venv
  source venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt
Rode a aplicação:

streamlit run app.py

## 4. Como Funciona (Lógica Principal)

  O coração do simulador repousa no Scipy. O modelo SEIR não se baseia em sorteio estatístico (estocástico), mas em equações de mudança baseadas no tempo (derivadas).
Definimos um sistema de equações onde a variação (crescimento ou decrescimento) de Suscetíveis, Expostos, Infectados e Recuperados depende de taxas fixas
interconectadas (R0, tempo de infecção, etc.). A função scipy.integrate.odeint recebe essas equações, as condições iniciais (Dia 0) e um vetor de tempo, 
calculando os passinhos (integração numérica) dia após dia para descobrir quantos indivíduos estão em cada grupo ao longo do tempo.

## 5. Estrutura do Repositório

• solver.py: Arquivo lógico que processa os cálculos puramente matemáticos sem saber da existência da interface. Abstrai e resolve as equações.
• app.py: Arquivo "front-end" e de roteamento. Capta as interações no painel do usuário, envia para o solver.py calcular, e empacota os resultados em gráficos usando Streamlit e Plotly.

• requirements.txt: Inventário de pacotes.

• README.md: Este documento de instrução e apresentação.

## 6. Limitações do Projeto

  Por se tratar de um modelo SEIR em sua forma clássica básica, o simulador apresenta algumas premissas irrealistas se aplicado diretamente sem ajustes ao mundo real:

• População Fechada e Homogênea: Assume-se que ninguém nasce ou morre (por causas naturais) e que o contato social é idêntico para todos.
• Falta de Intervenções: O modelo não computa vacinações, lockdowns dinâmicos, quarentenas estritas ou uso de máscaras (o R0 se mantém estático durante toda simulação).
• Ausência de Reinfecção: Parte-se do pressuposto que todo indivíduo Recuperado adquire imunidade vitalícia e não volta para o grupo de Suscetíveis (o que seria um modelo SEIRS).

## 7. Visão Crítica e Realidade Epidemiológica

Existe um abismo considerável entre um simulador didático determinístico e o mundo real da modelagem em saúde pública.

Ferramentas como esta são maravilhosas do ponto de vista pedagógico por isolarem os efeitos de variáveis cruciais (como provar matematicamente o "achatamento da curva" ao se reduzir o R0). No entanto, o mundo real é caótico e inerentemente estocástico (baseado em
probabilidades variáveis e imprevistos). Modeladores epidemiológicos profissionais usam modelos baseados em agentes (onde cada pessoa tem rotinas simuladas) ou modelos em rede (considerando aglomerados populacionais, mobilidade urbana e matrizes de contato por idade). 
Utilizar este modelo puro e isolado para tomada de decisão em políticas públicas sem calibrá-lo massivamente aos dados empíricos diários levaria a previsões imprecisas e decisões falhas.

## 8. Prompts utilizados

Prompt 1: Atue como um Cientista de Dados e Desenvolvedor Python. Preciso de um projeto completo  com intuito educacional de um simulador interativo de propagação de doenças usando o modelo epidemiológico SEIR, focado em demonstrar a viabilidade de criar aplicações complexas de forma simplificada com IA. O projeto será publicado no GitHub e deve ser modularizado em quatro arquivos: a lógica matemática (solver.py), a interface (app.py), as dependências (requirements.txt) e a documentação (README.md).

Parte 1: A Lógica Matemática (solver.py)
* Use numpy e scipy para as equações diferenciais.
* Crie a função do modelo SEIR e uma função para resolver as equações usando o Scipy. 
* Adicione validações lógicas na função principal para garantir que os parâmetros de entrada sejam válidos (ex: população > 0, tempo de simulação > 0). O resultado deve ser retornado em um DataFrame do Pandas.

Parte 2: A Interface Python (app.py)
* Importe a lógica do solver.py.
* Use plotly para um gráfico interativo e streamlit para a interface.
* Barra lateral (sidebar): Crie sliders para População Total, Número de dias da simulação, Tempo de Incubação, Duração da Infecção e R0. A simulação deve sempre iniciar com 1 pessoa infectada.
* Corpo principal: Título da aplicação, uma breve explicação teórica das fases do modelo SEIR.
* Visualização: Exiba o gráfico interativo do Plotly com as curvas. 
* Funcionalidade Secundária: Logo abaixo do gráfico, adicione um 'expander' (seção expansível) ou uma aba contendo a tabela de dados diários brutos gerada pelo modelo, para que o usuário possa consultar os números exatos de cada dia.
* Comentários: Comente os blocos principais do código de forma didática, para que eu possa explicar a lógica facilmente se for questionado.

Parte 3: Dependências (requirements.txt)
* Liste as bibliotecas necessárias para rodar o projeto: streamlit, numpy, scipy, pandas, plotly.

Parte 4: A Documentação (README.md)
Crie um arquivo README.md profissional e bem formatado, contendo obrigatoriamente as seguintes seções:
1. Título e Descrição: O nome do projeto, seu objetivo acadêmico, o que ele faz e as funcionalidades presentes (gráficos e tabela diária).
2. Tecnologias Utilizadas: Uma lista detalhada das bibliotecas e ferramentas usadas no desenvolvimento (Python, Streamlit, Scipy, Numpy, Pandas e Plotly).
3. Passo a Passo para Execução: Um guia detalhado de como clonar o repositório, criar um ambiente virtual (opcional mas recomendado), instalar as dependências através do arquivo requirements.txt e o comando exato para iniciar a aplicação com o streamlit.
4. Como Funciona (Lógica Principal): Explicação didática sobre como o Scipy resolve as equações diferenciais do modelo SEIR.
5. Estrutura do Repositório: Explicação de como os arquivos estão organizados e a função de cada um (app.py, solver.py, etc).
6. Limitações do Projeto: Análise das limitações matemáticas do modelo SEIR básico (assumir população fechada, não considerar vacinação, etc).
7. Visão Crítica: Reflexão acadêmica sobre o abismo entre um simulador didático determinístico e a complexidade da modelagem epidemiológica no mundo real.

Gere a resposta entregando o conteúdo de cada um dos quatro arquivos em blocos de código separados e claramente identificados.

Prompt 2: Atue como um pesquisador acadêmico e cientista da computação. Preciso que você escreva um texto em formato de artigo científico documentando e explicando o código do simulador SEIR interativo e o README que você acabou de gerar nesta nossa conversa.

A estrutura do artigo deve conter:
1. Resumo e Palavras-chave: Uma breve visão geral do projeto e das tecnologias, seguida de 3 a 5 palavras-chave.
2. Introdução: O contexto do modelo epidemiológico SEIR e o objetivo educacional de criar esse simulador.
3. Metodologia Computacional: Esta é a parte principal. Explique detalhadamente como o código foi arquitetado. Explique a modularização do projeto, como o arquivo solver.py utiliza o Scipy para resolver as Equações Diferenciais Ordinárias (EDOs) e como o arquivo app.py utiliza o Streamlit e o Plotly para a interface de usuário e renderização dos gráficos interativos.
4. Discussões e Resultados: Exponha os resultados obtidos e principais pontos de discussão.
5. Conclusão: Um fechamento sobre a viabilidade de construir ferramentas de simulação complexas com o auxílio de inteligência artificial.
6. Referências: Liste as referências bibliográficas. Cite estritamente as documentações oficiais das bibliotecas utilizadas (Python, Streamlit, SciPy, Pandas, Plotly) e a literatura clássica fundamental do modelo SEIR (como Kermack e McKendrick).

Gere o texto com linguagem acadêmica, formal e clara. O formato, a estrutura e as citações devem seguir rigorosamente as normas da ABNT. As argumentações devem ser claras, coerentes e objetivas, sem afirmar coisas sem embasamento técnico ou teórico. Baseie todo o artigo estritamente no código e nos arquivos da nossa conversa atual, sem adicionar funcionalidades, variáveis ou metodologias que não estejam presentes na aplicação. Atenção: sob nenhuma hipótese invente referências bibliográficas falsas (alucinações), não distorça informações e garanta que as conclusões sejam derivadas unicamente da realidade do projeto entregue.
