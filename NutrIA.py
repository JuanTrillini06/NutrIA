import streamlit as st

def main():
    # Define the title and subtitle of the app
    st.title("Plan de Alimentación")
    st.subheader("Crea un plan de alimentación personalizado")

    # Get user input for the objective, diet type, consumed calories, and dietary restrictions
    objective = st.selectbox("Objetivo:", ["Perder peso", "Ganar peso", "Mantener peso"])
    diet_type = st.selectbox("Tipo de dieta:", ["Vegetariana", "Vegana", "Omnívora"])
    consumed_calories = st.number_input("Calorías consumidas:", min_value=0, step=100)
    dietary_restrictions = st.multiselect("Restricciones alimenticias:", 
                                          ["Gluten", "Lactosa", "Frutos secos", "Mariscos"])

    # Display the user's input
    st.write("Objetivo: ", objective)
    st.write("Tipo de dieta: ", diet_type)
    st.write("Calorías consumidas: ", consumed_calories)
    st.write("Restricciones alimenticias: ", dietary_restrictions)

if __name__ == "__main__":
    main()