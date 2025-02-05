import streamlit as st
import openai

# Configura tu clave de API de OpenAI de manera segura
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title('🥗 Generador Inteligente de Planes de Nutrición')

# Solicitar el objetivo del plan
objetivo = st.selectbox(
    '¿Cuál es tu objetivo?',
    ['Perder peso', 'Mantener peso', 'Ganar volumen']
)

# Solicitar el tipo de plan
tipo_plan = st.selectbox(
    'Elige el tipo de plan que prefieres:',
    ['Económica', 'Equilibrada', 'Estricta']
)

# Solicitar el consumo calórico deseado
consumo_calorico = st.number_input(
    'Ingresa tu consumo calórico diario:',
    min_value=1000,
    max_value=5000,
    step=100,
    value=2000
)

# Solicitar restricciones alimenticias
restricciones = st.text_input(
    'Indica tus restricciones alimenticias (celiaquía, intolerancias, alergias, etc):',
    placeholder='Ejemplo: Sin gluten, sin lactosa'
)

# Función para generar el plan
def generar_plan():
    restricciones_texto = restricciones if restricciones else 'Ninguna'
    prompt = f"""
    Eres un nutricionista profesional. Crea un plan de alimentación semanal personalizado basado en las siguientes preferencias:
    - Objetivo: {objetivo}
    - Tipo de plan: {tipo_plan}
    - Consumo calórico diario: {consumo_calorico} calorías
    - Restricciones alimenticias: {restricciones_texto}
    
    El plan debe ser detallado, incluyendo desayuno, almuerzo, cena y snacks para cada día de la semana. Las comidas deben ser variadas y considerar alimentos accesibles. Presenta la información de manera clara y organizada.
    """
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2500,
        temperature=0.7
    )
    plan = respuesta.choices[0].text.strip()
    return plan

# Botón para generar el plan
if st.button('Generar Plan de Nutrición'):
    with st.spinner('Generando tu plan personalizado...'):
        plan_nutricional = generar_plan()
    st.success('¡Aquí está tu plan!')
    st.write(plan_nutricional)
