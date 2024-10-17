import streamlit as st

# Sample exchange rate
exchange_rate = 280  # 1 USD = 280 PKR (you can update this as per the current rate)

st.title("Currency Converter")

# Create two options for conversion
conversion_type = st.selectbox("Select conversion type:", ("USD to PKR", "PKR to USD"))

if conversion_type == "USD to PKR":
    usd_amount = st.number_input("Enter amount in USD:", min_value=0.0, step=0.01)
    if st.button("Convert"):
        pkr_amount = usd_amount * exchange_rate
        st.success(f"{usd_amount} USD is equal to {pkr_amount:.2f} PKR")

elif conversion_type == "PKR to USD":
    pkr_amount = st.number_input("Enter amount in PKR:", min_value=0.0, step=0.01)
    if st.button("Convert"):
        usd_amount = pkr_amount / exchange_rate
        st.success(f"{pkr_amount} PKR is equal to {usd_amount:.2f} USD")
