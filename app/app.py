<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Sistema de Predição de Churn",
    page_icon="📉",
    layout="wide"
)

# ==========================================
# CARREGAR MODELO
# ==========================================

model = joblib.load('models/model_lr.pkl')
scaler = joblib.load('models/scaler.pkl')
feature_names = joblib.load('models/feature_names.pkl')

# ==========================================
# HEADER
# ==========================================

st.title("📉 Sistema de Predição de Churn")

st.markdown("""
Este sistema utiliza **Machine Learning** para prever a chance de um cliente cancelar o serviço (**Churn**).

Preencha as informações abaixo para obter uma previsão.
""")

st.divider()

# ==========================================
# INPUTS
# ==========================================

st.subheader("🧾 Informações do Cliente")

col1, col2 = st.columns(2)

with col1:

    tenure = st.slider(
        "Tempo como cliente (meses)",
        0,
        72,
        12
    )

    monthly_charges = st.slider(
        "Valor mensal da assinatura (R$)",
        0.0,
        150.0,
        70.0
    )

    contract = st.selectbox(
        "Tipo de contrato",
        [
            "Mensal",
            "1 Ano",
            "2 Anos"
        ]
    )

    internet_service = st.selectbox(
        "Serviço de internet",
        [
            "DSL",
            "Fibra Óptica",
            "Sem Internet"
        ]
    )

    senior = st.selectbox(
        "Cliente idoso (+65 anos)",
        [
            "Não",
            "Sim"
        ]
    )

    partner = st.selectbox(
        "Possui parceiro(a)?",
        [
            "Sim",
            "Não"
        ]
    )

with col2:

    payment_method = st.selectbox(
        "Método de pagamento",
        [
            "Cheque eletrônico",
            "Cheque enviado",
            "Transferência bancária automática",
            "Cartão de crédito automático"
        ]
    )

    tech_support = st.selectbox(
        "Possui suporte técnico?",
        [
            "Sim",
            "Não"
        ]
    )

    online_security = st.selectbox(
        "Possui segurança online?",
        [
            "Sim",
            "Não"
        ]
    )

    streaming_tv = st.selectbox(
        "Possui Streaming TV?",
        [
            "Sim",
            "Não"
        ]
    )

    streaming_movies = st.selectbox(
        "Possui Streaming Movies?",
        [
            "Sim",
            "Não"
        ]
    )

    dependents = st.selectbox(
        "Possui dependentes?",
        [
            "Sim",
            "Não"
        ]
    )

    paperless = st.selectbox(
        "Fatura digital?",
        [
            "Sim",
            "Não"
        ]
    )

st.divider()

# ==========================================
# BOTÃO
# ==========================================

if st.button("🔍 Prever Churn", use_container_width=True):

    # ======================================
    # BASE INICIAL
    # ======================================

    customer_data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': tenure * monthly_charges,
        'SeniorCitizen': 1 if senior == 'Sim' else 0
    }

    input_df = pd.DataFrame([customer_data])

    # Criar TODAS as colunas do treino
    for feature in feature_names:

        if feature not in input_df.columns:
            input_df[feature] = 0

    # ======================================
    # CONTRACT
    # ======================================

    if contract == "1 Ano":
        if 'Contract_One year' in input_df.columns:
            input_df['Contract_One year'] = 1

    elif contract == "2 Anos":
        if 'Contract_Two year' in input_df.columns:
            input_df['Contract_Two year'] = 1

    # ======================================
    # INTERNET
    # ======================================

    if internet_service == "Fibra Óptica":
        if 'InternetService_Fiber optic' in input_df.columns:
            input_df['InternetService_Fiber optic'] = 1

    elif internet_service == "Sem Internet":
        if 'InternetService_No' in input_df.columns:
            input_df['InternetService_No'] = 1

    # ======================================
    # PAYMENT METHOD
    # ======================================

    payment_mapping = {
        "Cheque eletrônico":
            "PaymentMethod_Electronic check",

        "Cheque enviado":
            "PaymentMethod_Mailed check",

        "Transferência bancária automática":
            "PaymentMethod_Bank transfer (automatic)",

        "Cartão de crédito automático":
            "PaymentMethod_Credit card (automatic)"
    }

    payment_col = payment_mapping[payment_method]

    if payment_col in input_df.columns:
        input_df[payment_col] = 1

    # ======================================
    # TECH SUPPORT
    # ======================================

    if tech_support == "Sim":
        if 'TechSupport_Yes' in input_df.columns:
            input_df['TechSupport_Yes'] = 1

    # ======================================
    # ONLINE SECURITY
    # ======================================

    if online_security == "Sim":
        if 'OnlineSecurity_Yes' in input_df.columns:
            input_df['OnlineSecurity_Yes'] = 1

    # ======================================
    # STREAMING TV
    # ======================================

    if streaming_tv == "Sim":
        if 'StreamingTV_Yes' in input_df.columns:
            input_df['StreamingTV_Yes'] = 1

    # ======================================
    # STREAMING MOVIES
    # ======================================

    if streaming_movies == "Sim":
        if 'StreamingMovies_Yes' in input_df.columns:
            input_df['StreamingMovies_Yes'] = 1

    # ======================================
    # DEPENDENTS
    # ======================================

    if dependents == "Sim":
        if 'Dependents_Yes' in input_df.columns:
            input_df['Dependents_Yes'] = 1

    # ======================================
    # PARTNER
    # ======================================

    if partner == "Sim":
        if 'Partner_Yes' in input_df.columns:
            input_df['Partner_Yes'] = 1

    # ======================================
    # PAPERLESS BILLING
    # ======================================

    if paperless == "Sim":
        if 'PaperlessBilling_Yes' in input_df.columns:
            input_df['PaperlessBilling_Yes'] = 1

    # ======================================
    # REORDENAR COLUNAS
    # ======================================

    input_df = input_df[feature_names]

    # DEBUG (TEMPORÁRIO)
    with st.expander("🔧 Debug das Features"):

        st.write("Quantidade de features:")
        st.write(len(input_df.columns))

        st.write("Features usadas:")
        st.dataframe(input_df.T)

    # ======================================
    # SCALER
    # ======================================

    input_scaled = scaler.transform(input_df)

    # ======================================
    # PREDIÇÃO
    # ======================================

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    threshold = 0.40

    prediction = int(
        probability >= threshold
    )

    # ======================================
    # RESULTADO
    # ======================================

    st.subheader("📊 Resultado da Predição")

    st.metric(
        "Probabilidade de Cancelamento",
        f"{probability:.2%}"
    )

    if prediction == 1:

        st.error(
            "⚠️ Alto Risco de Cancelamento"
        )

        st.markdown(f"""
### Motivo da Classificação

O cliente apresentou uma probabilidade de **{probability:.2%}**
de cancelar o serviço.

### Recomendações Estratégicas

✅ Oferecer desconto de retenção  
✅ Priorizar atendimento técnico  
✅ Incentivar contrato anual  
✅ Oferecer benefícios exclusivos
        """)

    else:

        st.success(
            "✅ Baixo Risco de Cancelamento"
        )

        st.markdown(f"""
### Motivo da Classificação

O cliente apresentou uma probabilidade de apenas **{probability:.2%}**
de cancelar o serviço.

### Situação do Cliente

✅ Tendência de permanência  
✅ Não necessita ação imediata  
✅ Cliente com menor propensão ao churn
        """)

st.divider()

st.caption(
    "Projeto de Machine Learning para Predição de Churn | Desenvolvido por Luiz P. Hatem"
)
=======
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Sistema de Predição de Churn",
    page_icon="📉",
    layout="wide"
)

# ==========================================
# CARREGAR MODELO
# ==========================================

model = joblib.load('models/model_lr.pkl')
scaler = joblib.load('models/scaler.pkl')
feature_names = joblib.load('models/feature_names.pkl')

# ==========================================
# HEADER
# ==========================================

st.title("📉 Sistema de Predição de Churn")

st.markdown("""
Este sistema utiliza **Machine Learning** para prever a chance de um cliente cancelar o serviço (**Churn**).

Preencha as informações abaixo para obter uma previsão.
""")

st.divider()

# ==========================================
# INPUTS
# ==========================================

st.subheader("🧾 Informações do Cliente")

col1, col2 = st.columns(2)

with col1:

    tenure = st.slider(
        "Tempo como cliente (meses)",
        0,
        72,
        12
    )

    monthly_charges = st.slider(
        "Valor mensal da assinatura (R$)",
        0.0,
        150.0,
        70.0
    )

    contract = st.selectbox(
        "Tipo de contrato",
        [
            "Mensal",
            "1 Ano",
            "2 Anos"
        ]
    )

    internet_service = st.selectbox(
        "Serviço de internet",
        [
            "DSL",
            "Fibra Óptica",
            "Sem Internet"
        ]
    )

    senior = st.selectbox(
        "Cliente idoso (+65 anos)",
        [
            "Não",
            "Sim"
        ]
    )

    partner = st.selectbox(
        "Possui parceiro(a)?",
        [
            "Sim",
            "Não"
        ]
    )

with col2:

    payment_method = st.selectbox(
        "Método de pagamento",
        [
            "Cheque eletrônico",
            "Cheque enviado",
            "Transferência bancária automática",
            "Cartão de crédito automático"
        ]
    )

    tech_support = st.selectbox(
        "Possui suporte técnico?",
        [
            "Sim",
            "Não"
        ]
    )

    online_security = st.selectbox(
        "Possui segurança online?",
        [
            "Sim",
            "Não"
        ]
    )

    streaming_tv = st.selectbox(
        "Possui Streaming TV?",
        [
            "Sim",
            "Não"
        ]
    )

    streaming_movies = st.selectbox(
        "Possui Streaming Movies?",
        [
            "Sim",
            "Não"
        ]
    )

    dependents = st.selectbox(
        "Possui dependentes?",
        [
            "Sim",
            "Não"
        ]
    )

    paperless = st.selectbox(
        "Fatura digital?",
        [
            "Sim",
            "Não"
        ]
    )

st.divider()

# ==========================================
# BOTÃO
# ==========================================

if st.button("🔍 Prever Churn", use_container_width=True):

    # ======================================
    # BASE INICIAL
    # ======================================

    customer_data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': tenure * monthly_charges,
        'SeniorCitizen': 1 if senior == 'Sim' else 0
    }

    input_df = pd.DataFrame([customer_data])

    # Criar TODAS as colunas do treino
    for feature in feature_names:

        if feature not in input_df.columns:
            input_df[feature] = 0

    # ======================================
    # CONTRACT
    # ======================================

    if contract == "1 Ano":
        if 'Contract_One year' in input_df.columns:
            input_df['Contract_One year'] = 1

    elif contract == "2 Anos":
        if 'Contract_Two year' in input_df.columns:
            input_df['Contract_Two year'] = 1

    # ======================================
    # INTERNET
    # ======================================

    if internet_service == "Fibra Óptica":
        if 'InternetService_Fiber optic' in input_df.columns:
            input_df['InternetService_Fiber optic'] = 1

    elif internet_service == "Sem Internet":
        if 'InternetService_No' in input_df.columns:
            input_df['InternetService_No'] = 1

    # ======================================
    # PAYMENT METHOD
    # ======================================

    payment_mapping = {
        "Cheque eletrônico":
            "PaymentMethod_Electronic check",

        "Cheque enviado":
            "PaymentMethod_Mailed check",

        "Transferência bancária automática":
            "PaymentMethod_Bank transfer (automatic)",

        "Cartão de crédito automático":
            "PaymentMethod_Credit card (automatic)"
    }

    payment_col = payment_mapping[payment_method]

    if payment_col in input_df.columns:
        input_df[payment_col] = 1

    # ======================================
    # TECH SUPPORT
    # ======================================

    if tech_support == "Sim":
        if 'TechSupport_Yes' in input_df.columns:
            input_df['TechSupport_Yes'] = 1

    # ======================================
    # ONLINE SECURITY
    # ======================================

    if online_security == "Sim":
        if 'OnlineSecurity_Yes' in input_df.columns:
            input_df['OnlineSecurity_Yes'] = 1

    # ======================================
    # STREAMING TV
    # ======================================

    if streaming_tv == "Sim":
        if 'StreamingTV_Yes' in input_df.columns:
            input_df['StreamingTV_Yes'] = 1

    # ======================================
    # STREAMING MOVIES
    # ======================================

    if streaming_movies == "Sim":
        if 'StreamingMovies_Yes' in input_df.columns:
            input_df['StreamingMovies_Yes'] = 1

    # ======================================
    # DEPENDENTS
    # ======================================

    if dependents == "Sim":
        if 'Dependents_Yes' in input_df.columns:
            input_df['Dependents_Yes'] = 1

    # ======================================
    # PARTNER
    # ======================================

    if partner == "Sim":
        if 'Partner_Yes' in input_df.columns:
            input_df['Partner_Yes'] = 1

    # ======================================
    # PAPERLESS BILLING
    # ======================================

    if paperless == "Sim":
        if 'PaperlessBilling_Yes' in input_df.columns:
            input_df['PaperlessBilling_Yes'] = 1

    # ======================================
    # REORDENAR COLUNAS
    # ======================================

    input_df = input_df[feature_names]

    # DEBUG (TEMPORÁRIO)
    with st.expander("🔧 Debug das Features"):

        st.write("Quantidade de features:")
        st.write(len(input_df.columns))

        st.write("Features usadas:")
        st.dataframe(input_df.T)

    # ======================================
    # SCALER
    # ======================================

    input_scaled = scaler.transform(input_df)

    # ======================================
    # PREDIÇÃO
    # ======================================

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    threshold = 0.40

    prediction = int(
        probability >= threshold
    )

    # ======================================
    # RESULTADO
    # ======================================

    st.subheader("📊 Resultado da Predição")

    st.metric(
        "Probabilidade de Cancelamento",
        f"{probability:.2%}"
    )

    if prediction == 1:

        st.error(
            "⚠️ Alto Risco de Cancelamento"
        )

        st.markdown(f"""
### Motivo da Classificação

O cliente apresentou uma probabilidade de **{probability:.2%}**
de cancelar o serviço.

### Recomendações Estratégicas

✅ Oferecer desconto de retenção  
✅ Priorizar atendimento técnico  
✅ Incentivar contrato anual  
✅ Oferecer benefícios exclusivos
        """)

    else:

        st.success(
            "✅ Baixo Risco de Cancelamento"
        )

        st.markdown(f"""
### Motivo da Classificação

O cliente apresentou uma probabilidade de apenas **{probability:.2%}**
de cancelar o serviço.

### Situação do Cliente

✅ Tendência de permanência  
✅ Não necessita ação imediata  
✅ Cliente com menor propensão ao churn
        """)

st.divider()

st.caption(
    "Projeto de Machine Learning para Predição de Churn | Desenvolvido por Luiz P. Hatem"
)
>>>>>>> 5da02ff8080a5a479ceb14dadc1faada33eb39c8
