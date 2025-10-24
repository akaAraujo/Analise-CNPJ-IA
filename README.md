# API - CRUD

## 🎯 Objetivo

O projeto tem como objetivo automatizar a análise de CNPJs de Instituições de Ensino, avaliando suas informações cadastrais e financeiras para identificar se estão qualificadas a atuar em operações de gestão de recebíveis e financiamento estudantil.

## ⚖️ Critérios de Avaliação

| Categoria       | Condição                                  | Descrição                                                       | Classificação |
| --------------- | ----------------------------------------- | --------------------------------------------------------------- | ------------- |
| 🟢 **Positivo** | Empresa ativa há 2 anos ou mais           | Demonstra estabilidade e histórico operacional                  | Apta          |
| 🟢 **Positivo** | Capital social acima de R$ 100.000        | Indica estrutura financeira adequada ao setor educacional       | Apta          |
| 🟢 **Positivo** | CNAE principal relacionado à Educação     | Garante que a atividade principal é compatível com o serviço    | Apta          |
| 🟡 **Atenção**  | Empresa com menos de 2 anos de atividade  | Indica empresa nova, com histórico limitado                     | Em atenção    |
| 🟡 **Atenção**  | Capital social abaixo de R$ 100.000       | Pode indicar estrutura financeira inadequada                    | Em atenção    |
| 🟠 **Negativo** | Empresa inapta, suspensa ou baixada       | Não atende aos requisitos mínimos legais                        | Não apta      |
| 🟠 **Negativo** | CNAE principal não relacionado a Educação | Indica que a atividade principal não é compatível com o serviço | Não apta      |

## 🧠 Lógica e Tomada de Decisão

A análise considera **critérios positivos**, **critérios de atenção** e **critérios negativos**, atribuindo uma classificação final conforme a combinação dos fatores encontrados.

✅ **Apta**: Caso a empresa atenda todos os requisitos positivos ela será aprovada de imediato.

⚠️ **Em Atenção**: Caso a empresa possui algum critério de atenção os dados serão submetidos a análise da IA, utilizando dados já obtidos, análise semântica e dados pertinentes da empresa.

❌ **Não Apta**: Caso o CNPJ analisado possua um dos critérios negativos ele será reprovado imediatamente.

## ⚙️ Como Executar o Projeto

### 🧩 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- [Python 3.13.1](https://www.python.org/)
- [Git](https://git-scm.com/)
- (Opcional) [Visual Studio Code](https://code.visualstudio.com/) para editar e executar o código

### 📦 Clonar o Repositório

```bash
git clone https://github.com/akaAraujo/Analise-CNPJ-IA.git
cd Analise-CNPJ-IA
```

### 🔧 Configurar o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 🔐 Configurar Variáveis de Ambiente

O projeto utiliza a API **Gemini** para análises baseadas em IA.  
Para isso, é necessário definir a variável de ambiente `GEMINI_API_KEY`.

1. **Fora da pasta do projeto**, crie um arquivo chamado **`.env`**

   > ⚠️ **Importante:** o arquivo `.env` **não deve ficar dentro da pasta `venv/`**.

2. Adicione a seguinte linha ao arquivo `.env`:

   ```bash
   GEMINI_API_KEY="sua_chave_aqui"
   ```

### 📩 Instalando as dependências

```bash
pip install -r requirements.txt
```

### 🚩 Executando o projeto

```bash
python src/main.py
```

## 📂 Estrutura de Pastas

```text
Analise-CNPJ-IA/
├── data/                       # Dados brutos
│   └── cnae_permitidos.json    # Listagem dos CNAEs aceitos pela análise
│
├── src/                        # Código-fonte principal
│   ├── analise.py              # Arquivo destinado a lógica e testes para a tomada de decisões
│   ├── connections_ia.py       # Arquivo destinado a conexão com a Gemini
│   ├── connections.py          # Arquivo destinado a conexão a API do OpenCNPJ
│   ├── empresa.py              # Classe e lógica principal da entidade Empresa
│   ├── main.py                 # Script raiz do projeto
│   └── utils.py                # Arquivo destinado a funções utilitárias (formatação, leitura de arquivos)
│
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação do projeto
└── .gitignore                  # Arquivos/pastas a ignorar no repositório
```
