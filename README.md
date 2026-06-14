# 📉 Customer Churn Prediction - Telecom

Projeto de Machine Learning para predição de **Churn (cancelamento de clientes)** em uma empresa de telecomunicações.

O objetivo do projeto é identificar clientes com maior risco de cancelamento, gerar insights estratégicos e propor ações de retenção com base em dados.

---

# 🚀 Objetivo do Projeto

O churn de clientes é um dos principais problemas enfrentados por empresas de telecomunicações.

Neste projeto foi desenvolvido um pipeline completo de análise de dados e Machine Learning para:

- Entender os fatores relacionados ao cancelamento de clientes;
- Identificar padrões comportamentais;
- Construir modelos preditivos de churn;
- Ajustar threshold de decisão visando maior retenção;
- Gerar insights de negócio para estratégias de fidelização.

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Joblib
- Jupyter Notebook
- Power BI

---

# 📂 Estrutura do Projeto

```txt
customer-churn-prediction/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── processed/
│       ├── encoded_df.csv
│       └── dashboard_dataset.csv
│
├── models/
│   ├── model_lr.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_eda.ipynb
│   ├── 03_predicition_analyze.ipynb
│   ├── 04_data_cleaning_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_feature_importance_business_insights.ipynb
│   └── 07_dashboard_dataset.ipynb
│
├── dashboard/
│   └── customer_churn_dashboard.pbix
│
├── requirements.txt
└── README.md
````

---

# 📊 Dataset

O dataset utilizado foi o **IBM Telco Customer Churn Dataset**, contendo informações demográficas, financeiras e contratuais de clientes de telecom.

Principais variáveis:

* Tipo de contrato
* Serviço de internet
* Tempo de permanência (tenure)
* Método de pagamento
* Serviços adicionais
* Custos mensais e totais

**Target:**

* `Churn`

  * Yes → Cliente cancelou
  * No → Cliente permaneceu

---

# 🔎 Etapas do Projeto

## 1. Business Understanding

Definição do problema de negócio:

> Como prever clientes com maior risco de churn e reduzir cancelamentos?

---

## 2. Exploratory Data Analysis (EDA)

Análises realizadas:

* Churn por tipo de contrato;
* Churn por método de pagamento;
* Churn por serviço de internet;
* Churn por tenure;
* Churn por senior citizens;
* Relação entre serviços adicionais e churn.

### Principais Insights

✅ Clientes **Month-to-Month** cancelam mais.

✅ Clientes com **Fiber Optic** apresentam maior taxa de churn.

✅ Clientes com maior **tenure** possuem menor chance de cancelamento.

✅ Contratos anuais e bianuais demonstram maior retenção.

✅ Clientes com **Tech Support** e **Online Security** tendem a permanecer.

---

## 3. Data Cleaning & Feature Engineering

Tratamentos realizados:

* Conversão da coluna `TotalCharges` para formato numérico;
* Tratamento de valores ausentes;
* Encoding de variáveis categóricas;
* Preparação para Machine Learning;
* Train/Test Split;
* Feature Scaling com `StandardScaler`.

---

## 4. Machine Learning

Modelos testados:

### Logistic Regression

* Accuracy: **80.38%**
* Precision: **0.65**
* Recall: **0.57**
* F1-score: **0.61**

### Decision Tree

* Accuracy: **78%**
* Precision: **0.58**
* Recall: **0.60**
* F1-score: **0.59**

### Random Forest

* Accuracy: **79%**
* Precision: **0.64**
* Recall: **0.48**
* F1-score: **0.55**

---

## 🎯 Threshold Tuning

Foi realizado ajuste do threshold da Regressão Logística visando otimização da identificação de churn.

### Resultado

Threshold padrão:

```txt
0.50
```

Threshold otimizado:

```txt
0.40
```

Resultados:

* Precision: **0.58**
* Recall: **0.68**
* F1-score: **0.63**

O threshold otimizado aumentou significativamente a capacidade do modelo em identificar clientes com risco de cancelamento.

---

## 📈 Business Insights

O modelo apontou os principais fatores relacionados ao churn:

### Fatores que aumentam churn

* Fiber Optic
* Electronic Check
* Streaming Services
* Paperless Billing
* Senior Citizen

### Fatores que reduzem churn

* Longo tempo de permanência (`tenure`)
* Contratos de longo prazo
* Tech Support
* Online Security
* Dependents

---

## 💡 Recomendações Estratégicas

Com base nos resultados, recomenda-se:

1. Criar campanhas para clientes **Month-to-Month**;
2. Revisar experiência do serviço **Fiber Optic**;
3. Incentivar migração para contratos anuais;
4. Priorizar retenção nos primeiros meses do cliente;
5. Aplicar campanhas preventivas usando o modelo preditivo.

---

# 📌 Próximos Passos

* [ ] Deploy do modelo com Streamlit
* [ ] Dashboard interativo no Power BI
* [ ] Hyperparameter Tuning
* [ ] Cross Validation
* [ ] Feature Importance avançada

---

# 👨‍💻 Autor

**Luiz P. Hatem**

* GitHub: https://github.com/LuizPH0
* LinkedIn: https://www.linkedin.com/in/luiz-p-hatem/
