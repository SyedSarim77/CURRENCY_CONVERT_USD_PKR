import streamlit as st

# Sample exchange rate
exchange_rate = 280  # 1 USD = 280 PKR (you can update this as per the current rate)

# Set page configuration
st.set_page_config(page_title="Currency Converter", page_icon="💱")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
        color: #333;
    }
    h1 {
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: #4CAF50;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        border: None;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Currency Converter 💱")

# Add a brief description
st.markdown("""
This app converts between USD and PKR. Select the conversion type, enter the amount, and click "Convert" to see the result!
""")

# Create two options for conversion
conversion_type = st.selectbox("Select conversion type:", ("USD to PKR", "PKR to USD"))

if conversion_type == "USD to PKR":
    usd_amount = st.number_input("Enter amount in USD:", min_value=0.0, step=0.01)
    if st.button("Convert"):
        pkr_amount = usd_amount * exchange_rate
        st.success(f"{usd_amount:.2f} USD is equal to {pkr_amount:.2f} PKR")

elif conversion_type == "PKR to USD":
    pkr_amount = st.number_input("Enter amount in PKR:", min_value=0.0, step=0.01)
    if st.button("Convert"):
        usd_amount = pkr_amount / exchange_rate
        st.success(f"{pkr_amount:.2f} PKR is equal to {usd_amount:.2f} USD")

# Add a footer
st.markdown("""
---
*Developed with ❤️ by [SYED SARIM].*
""")
