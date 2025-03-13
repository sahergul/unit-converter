import streamlit as st

st.title("🌍Unit Converter")
st.markdown("### Converts Length, Weight, Temperature & Time Instantly")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature"])

def convert_units(category, value, unit):
    conversions = {
        "Length": {
            "Kilometers to Meters": 1000,
            "Meters to Kilometers": 0.001,
            "Miles to Kilometers": 1.60934,
            "Kilometers to Miles": 0.621371,
            "Foot to Inches": 12,
            "Inches to Foot": 1/12
        },
        "Weight": {
            "Kilograms to Pounds": 2.20462,
            "Pounds to Kilograms": 0.453592,
            "Kilograms to Grams": 1000,
            "Grams to Kilograms": 0.001
        },
        "Time": {
            "Seconds to Minutes": 1/60,
            "Minutes to Seconds": 60,
            "Minutes to Hours": 1/60,
            "Hours to Minutes": 60,
            "Hours to Days": 1/24,
            "Days to Hours": 24
        }
    }
    
    if category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
    else:
        return value * conversions[category][unit]

# Unit selection based on category
unit = ""
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", [
        "Kilometers to Meters",
        "Meters to Kilometers",
        "Miles to Kilometers",
        "Kilometers to Miles",
        "Foot to Inches",
        "Inches to Foot"
    ])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", [
        "Kilograms to Pounds",
        "Pounds to Kilograms",
        "Kilograms to Grams",
        "Grams to Kilograms"
    ])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", [
        "Seconds to Minutes",
        "Minutes to Seconds",
        "Minutes to Hours",
        "Hours to Minutes",
        "Hours to Days",
        "Days to Hours"
    ])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    try:
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f}")
    except KeyError:
        st.error("Invalid conversion selection - please check unit options")

print("Created by Saher Rammez")