import streamlit as st

# Sample exchange rate
exchange_rate = 280  # 1 USD = 280 PKR (you can update this as per the current rate)

# Set page configuration
st.set_page_config(page_title="Currency Converter", page_icon="💱")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #e9ecef;
    }
    h1 {
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: #007bff;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: None;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .converter-container {
        display: flex;
        justify-content: center;
        margin: 20px;
    }
    .input-box {
        margin: 10px;
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .result {
        margin-top: 20px;
        font-size: 1.5em;
        text-align: center;
        color: #28a745;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Currency Converter 💱")

# Add a brief description
st.markdown("""
Convert between USD and PKR. Select the conversion type, enter the amount, and click "Convert" to see the result!
""")

# Create a container for the input boxes
with st.container():
    conversion_type = st.selectbox("Select conversion type:", ("USD to PKR", "PKR to USD"))

    # Create input boxes based on conversion type
    if conversion_type == "USD to PKR":
        with st.container():
            usd_amount = st.number_input("Enter amount in USD:", min_value=0.0, step=0.01, format="%.2f", key="usd")
            if st.button("Convert to PKR", key="convert_usd_to_pkr"):
                pkr_amount = usd_amount * exchange_rate
                st.markdown(f"<div class='result'>{usd_amount:.2f} USD = {pkr_amount:.2f} PKR</div>", unsafe_allow_html=True)

    elif conversion_type == "PKR to USD":
        with st.container():
            pkr_amount = st.number_input("Enter amount in PKR:", min_value=0.0, step=0.01, format="%.2f", key="pkr")
            if st.button("Convert to USD", key="convert_pkr_to_usd"):
                usd_amount = pkr_amount / exchange_rate
                st.markdown(f"<div class='result'>{pkr_amount:.2f} PKR = {usd_amount:.2f} USD</div>", unsafe_allow_html=True)

# Add a footer
st.markdown("""
---
*Developed with ❤️ by [SYED SARIM].*
""")
