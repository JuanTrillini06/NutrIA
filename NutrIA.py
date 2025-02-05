import streamlit as st

def generar_plan_alimentacion(objetivo, tipo_dieta, calorias, restricciones):
    # Ejemplo de un plan de alimentación simple (puedes personalizarlo)
    plan = [
        {
            "comida": "Desayuno",
            "menu": "Avena con frutas y almendras",
            "calorias": 300
        },
        {
            "comida": "Almuerzo",
            "menu": "Ensalada de pollo con quinoa y vegetales",
            "calorias": 500
        },
        {
            "comida": "Cena",
            "menu": "Salmón a la parrilla con espárragos",
            "calorias": 400
        },
        {
            "comida": "Snack",
            "menu": "Yogur griego con miel y nueces",
            "calorias": 200
        }
    ]
    return plan

# Configuración de la app
st.title('Generador de Plan de Alimentación')

# Entrada del usuario
objetivo = st.selectbox('¿Cuál es tu objetivo?', ['Perder peso', 'Mantener peso', 'Ganar músculo'])
tipo_dieta = st.selectbox('¿Qué tipo de dieta prefieres?', ['Omnívora', 'Vegetariana', 'Vegana', 'Keto', 'Paleo'])
calorias = st.slider('Calorías diarias consumidas', 1000, 4000, 2000)
restricciones = st.text_area('¿Tienes alguna restricción alimenticia?', 'Ninguna')

# Generar plan de alimentación
if st.button('Generar Plan'):
    plan = generar_plan_alimentacion(objetivo, tipo_dieta, calorias, restricciones)
    st.write('### Tu plan de alimentación:')
    for comida in plan:
        st.write(f"**{comida['comida']}:** {comida['menu']} - {comida['calorias']} calorías")

# Run the app
if __name__ == "__main__":
    st.run()
