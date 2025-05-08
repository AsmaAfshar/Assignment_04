import streamlit as st 
def calculate_bmi(weight, height):
    if height <= 0:
        return None
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Streamlit UI
st.title("🧮 BMI Calculator")

st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (in meters)", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    if bmi:
        st.success(f"Your BMI is: {bmi}")

        # Optional: Categorize the BMI
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 25:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")