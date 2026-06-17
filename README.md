# Customer Churn Prediction System

Sistema de predição de cancelamento de clientes (Churn Prediction) desenvolvido utilizando Machine Learning, Power BI e Streamlit para auxiliar estratégias de retenção de clientes.

---

## Objetivo

O objetivo deste projeto é identificar clientes com maior propensão ao cancelamento de serviços, permitindo que empresas realizem ações preventivas de retenção, reduzindo perdas financeiras e aumentando a fidelização.

---

## Problema de Negócio

Empresas de telecomunicações frequentemente enfrentam altas taxas de cancelamento de clientes.

Antecipar quais clientes possuem maior risco de churn possibilita:

- Redução de perda de receita;
- Aumento da retenção;
- Campanhas de fidelização mais eficientes;
- Melhor alocação dos recursos comerciais.

---

## Arquitetura do Projeto

```text
Customer-Churn-Prediction-System/

├── app/
│   └── app.py
│
│
├── data/
│
├── raw/
│    └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── processed/
│    └── encoded_df.csv
│    └── dashboard_dataset.csv
│
├── models/
│   ├── final_model.pkl
│   ├── final_scaler.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_eda.ipynb
│   ├── 03_predicition_analyze.ipynb
│   ├── 04_data_cleaning_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_feature_importance_business_insights.ipynb
│   ├── 07_dashboard_dataset.ipynb
│   ├── 08_model_improvement(XGB).ipynb
│	├── 09_model_optimization.ipynb
│	└── 10_model_evaluation.ipynb
│
├── requirements.txt
├── README.md
├── churn_dashboard.pbix
└── .gitignore
```

---

# Exploratory Data Analysis (EDA)

Principais insights encontrados:

### Clientes com maior probabilidade de churn

✅ Internet Fiber Optic

✅ Contratos mensais

✅ Electronic Check

✅ Streaming TV

✅ Streaming Movies

✅ Clientes idosos (+65 anos)

---

### Clientes com menor probabilidade de churn

✅ Contratos anuais

✅ Tech Support

✅ Online Security

✅ Clientes com dependentes

✅ Clientes com maior tenure

---

# Modelagem

Modelos avaliados:

| Modelo | Accuracy | Precision | Recall | F1 |
|--------|----------|-----------|--------|----|
| Logistic Regression | 80% | 65% | 57% | 61% |
| Decision Tree | 78% | 58% | 60% | 59% |
| Random Forest | 79% | 64% | 48% | 55% |
| XGBoost | 78% | 59% | 55% | 57% |
| Logistic Balanced | 73% | 49% | **80%** | **61%** |

---

## Modelo Escolhido

### Logistic Regression (Balanced)

Justificativa:

Apesar do XGBoost apresentar maior Accuracy, a Regressão Logística Balanceada foi escolhida devido ao alto Recall.

O objetivo do projeto é identificar clientes em risco de cancelamento.

Nesse contexto, minimizar falsos negativos é mais importante do que reduzir falsos positivos.

---

# Avaliação do Modelo

## Métricas finais

Accuracy

```python
72.64%
```

Precision

```python
49.09%
```

Recall

```python
79.68%
```

F1 Score

```python
60.75%
```

ROC-AUC

```python
0.835
```

---

## ROC Curve

![Curva ROC](CurvaROC.png)

---

## Confusion Matrix

![Matriz de Confusão](Matriz-Confusao.png)

---

# Dashboard Power BI

O dashboard foi desenvolvido para acompanhamento das principais métricas relacionadas ao churn.

Indicadores disponíveis:

- Taxa de churn;
- Perfil dos clientes;
- Contratos;
- Internet Service;
- Payment Methods;
- Streaming Services;
- Tenure;
- Charges.

![Dashboard](dashboard.png)

---

# Aplicação Streamlit

A aplicação permite realizar predições individuais em tempo real.

Funcionalidades:

- Cadastro do cliente;
- Predição de churn;
- Score de risco;
- Explicação do resultado;
- Classificação automática.

---

## Executando localmente


Instalar dependências


```bash
pip install -r requirements.txt
```


Executar aplicação


```bash
streamlit run app/app.py
```


---

# Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib
- Power BI
- Streamlit
- Git
- GitHub

---

# Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- EDA;
- Feature Engineering;
- Model Selection;
- Threshold Tuning;
- ROC Curve;
- ROC-AUC;
- Model Persistence;
- Business Understanding;
- Dashboard Development;
- Streamlit Deployment.

---

# Autor

### Luiz Hatem

Estudante de Ciência da Computação | Analista de Dados | ML Enthusiast

LinkedIn:

www.linkedin.com/in/luiz-p-hatem/

GitHub:

github.com/LuizPH0


---

Caso tenha gostado do projeto, deixe uma estrela no repositório.