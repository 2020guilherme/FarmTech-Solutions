# FarmTech Solutions: Aplicação de Agricultura Digital em Python e R

Este projeto é uma aplicação desenvolvida como parte de uma atividade acadêmica, simulando uma solução para a Startup FarmTech Solutions. O objetivo foi criar uma ferramenta de agricultura digital para auxiliar produtores de soja e milho no gerenciamento de suas lavouras, utilizando a integração entre as linguagens de programação Python e R.

---

#### **Recursos e Tecnologias Utilizadas**

* **Python:** Linguagem principal para a interface e a lógica da aplicação.
* **R:** Utilizado para a análise estatística dos dados e para a funcionalidade bônus.
* **Git & GitHub:** Ferramentas de versionamento de código e colaboração.
* **Bibliotecas Python:** `csv`, `math`, `os`, `subprocess`.
* **Bibliotecas R:** `httr`, `jsonlite`.
* **API:** OpenWeatherMap, para a funcionalidade de previsão do tempo.

---

#### **Pré-requisitos e Configuração**

Para rodar a aplicação, você precisa ter o **Python 3** e o **R** instalados. Além disso, as seguintes bibliotecas são necessárias:

**1. Instalação de Bibliotecas**

* **Python:**
    ```bash
    pip install requests
    ```

* **R:**
    Abra o RStudio e rode os seguintes comandos no console:
    ```R
    install.packages("httr")
    install.packages("jsonlite")
    ```

**2. Configuração de Chaves (API Key)**

Para que a funcionalidade de previsão do tempo funcione, você precisa de uma chave de API gratuita da OpenWeatherMap. Para mantê-la segura, ela deve ser configurada como uma variável de ambiente.

* **Windows:**
    1.  Vá em **Menu Iniciar** > procure por "Editar as variáveis de ambiente do sistema".
    2.  Clique em **"Variáveis de Ambiente..."**.
    3.  Na seção "Variáveis de usuário", clique em **"Novo..."**.
          - Nome da variável: `OPENWEATHER_API_KEY`
          - Valor da variável: `SUA_CHAVE_DA_API_AQUI`
    4.  Reinicie o seu terminal para que as mudanças tenham efeito.

---

#### **Como Utilizar a Aplicação**

1.  **Inicie o Programa:** Abra um terminal na pasta do projeto e rode a aplicação com o seguinte comando:
    ```bash
    python app.py
    ```

2.  **Menu Principal:** A aplicação apresentará um menu interativo com as seguintes opções:

    * **[1] Gerenciar Plantios:** Acesse este menu para cadastrar, editar, visualizar ou excluir talhões.
    * **[2] Calcular Insumos:** Selecione um talhão para calcular a quantidade de insumos necessária.
    * **[3] Análise Estatística:** Esta opção gera um relatório estatístico de todos os talhões cadastrados usando um script em R.
    * **[4] Consultar Previsão do Tempo:** Esta opção executa um script em R que consulta o clima em cidades produtoras de soja e milho.
    * **[5] Sair:** Encerra o programa.

---

#### **O Fluxo de Trabalho Integrado**

O ponto central desta aplicação é a integração entre Python e R. O programa Python gerencia a interface, enquanto os scripts R realizam tarefas especializadas de análise e consulta de API. A comunicação entre as duas linguagens é feita via `subprocess`, garantindo um fluxo de trabalho unificado e eficiente.

Este projeto demonstra uma solução completa de ponta a ponta, desde o gerenciamento de dados até a análise e a apresentação de informações relevantes para o agronegócio.