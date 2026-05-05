import streamlit as st

st.set_page_config(page_title="LoveShootRepeat", layout="centered")

st.title("📸 LoveShootRepeat")
st.write("We are here to make your wedding memorable 💍")

# Inputs
date = st.text_input("Enter the date of events")
event = st.selectbox("Type your events")
nop = st.number_input("Enter number of guests", min_value=0, step=1)

# Button
if st.button("Generate Quote"):
    
    if nop == 0:
        st.warning("Please enter number of guests")

    elif 0 <= nop <= 300:
        st.success(f"""
Event: {event}  
Date: {date}

📸 Team of 4 (2 photographers + 2 cinematographers)  
💰 ₹2.25L / Day  

• 500 edited photos  
• Wedding short (20–40 seconds)  
• Trailer: 4–5 minutes  
• Wedding film: 10–15 minutes  
""")

    elif 301 <= nop <= 1000:
        st.success(f"""
Event: {event}  
Date: {date}

📸 Team of 6 (3 photographers + 3 cinematographers)  
💰 ₹4.25L / Day  

• 800 edited photos  
• Wedding short (20–40 seconds)  
• Trailer: 4–5 minutes  
• Wedding film: 10–15 minutes  
""")

    else:
        st.error("Please enter valid number of guests (50–1000)")
