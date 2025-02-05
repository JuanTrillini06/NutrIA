import streamlit as st
import openai

# Configurar la clave de API de OpenAI
openai.api_key = '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'

def generar_plan_alimentacion(objetivo, tipo_dieta, calorias, restricciones):
    prompt = f"Genera un plan de alimentación para alguien cuyo objetivo es {objetivo}, sigue una dieta {tipo_dieta}, consume {calorias} calorías al día y tiene las siguientes restricciones alimenticias: {restricciones}."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    
    return response.choices[0].text.strip()

# Configuración de la app
st.title('Generador de Plan de Alimentación con IA')

# Entrada del usuario
objetivo = st.selectbox('¿Cuál es tu objetivo?', ['Perder peso', 'Mantener peso', 'Ganar músculo'])
tipo_dieta = st.selectbox('¿Qué tipo de dieta prefieres?', ['Omnívora', 'Vegetariana', 'Vegana', 'Keto', 'Paleo'])
calorias = st.slider('Calorías diarias consumidas', 1000, 4000, 2000)
restricciones = st.text_area('¿Tienes alguna restricción alimenticia?', 'Ninguna')

# Generar plan de alimentación
if st.button('Generar Plan'):
    plan = generar_plan_alimentacion(objetivo, tipo_dieta, calorias, restricciones)
    st.write('### Tu plan de alimentación:')
    st.write(plan)

