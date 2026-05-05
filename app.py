import streamlit as st

st.set_page_config(page_title="LoveShootRepeat Quote Generator")

st.title("📸 LoveShootRepeat Quote Generator")
st.write("We are here to make your wedding memorable 💫")

# Inputs
event_name = st.text_input("Enter Event Name")
event_date = st.date_input("Enter Event Date")
people = st.number_input("Enter Number of Guests", min_value=0)

# Button
if st.button("Generate Quote"):

    if people < 50:
        st.error("Minimum 50 people required")
    
    elif 50 <= people <= 300:
        st.success("✅ Recommended Team: 2 Photographers + 2 Cinematographers")

        st.subheader("📦 Packages")

        st.write("**Classic – ₹2,25,000**")
        st.write("- 500 edited photos")
        st.write("- Wedding short (20-40 sec)")
        st.write("- Trailer: 4-5 min")
        st.write("- Wedding film: 10-15 min")
        st.write("- 1 wedding reel")

        st.write("---")

        st.write("**Signature – ₹4,25,000**")
        st.write("- 800 edited photos")
        st.write("- 2 wedding reels")

        st.write("---")

        st.write("**Luxe – ₹6,35,000**")
        st.write("- 1200 edited photos")
        st.write("- 3 wedding reels")

    elif people > 300:
        st.success("✅ Recommended Team: 3 Photographers + 3 Cinematographers")

        st.subheader("📦 Packages")

        st.write("**Classic – ₹4,25,000**")
        st.write("- 800 edited photos")
        st.write("- Wedding short (20-40 sec)")
        st.write("- Trailer: 4-5 min")
        st.write("- Wedding film: 10-15 min")
        st.write("- 1 wedding reel")

        st.write("---")

        st.write("**Signature – ₹6,25,000**")
        st.write("- 1100 edited photos")
        st.write("- 2 wedding reels")

        st.write("---")

        st.write("**Luxe – ₹8,95,000**")
        st.write("- 1500 edited photos")
        st.write("- 3 wedding reels")

    # Summary
    st.write("## 📄 Summary")
    st.write(f"**Event:** {event_name}")
    st.write(f"**Date:** {event_date}")
    st.write(f"**Guests:** {people}")

    # Contact section 🔥
    st.write("---")
    st.subheader("📞 Get in Touch")
    st.write("For bookings and queries, contact:")
    st.write("**Vedant: +91 90824 24539**")
