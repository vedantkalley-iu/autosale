import streamlit as st

st.set_page_config(page_title="LoveShootRepeat Quote Generator")

st.title("📸 LoveShootRepeat Quote Generator")
st.write("We are here to make your wedding memorable 💫")

# Number of events
num_events = st.number_input("How many events?", min_value=1, max_value=10, step=1)

events = []

st.subheader("📅 Enter Event Details")

for i in range(num_events):
    st.write(f"### Event {i+1}")
    name = st.text_input(f"Event Name {i+1}", key=f"name_{i}")
    date = st.date_input(f"Event Date {i+1}", key=f"date_{i}")
    events.append((name, date))

# Guests
people = st.number_input("Enter Total Number of Guests", min_value=0)

# Button
if st.button("Generate Quote"):

    if people < 50:
        st.error("Minimum 50 people required")
    
    elif 50 <= people <= 300:
        st.success("✅ Recommended Team: 2 Photographers + 2 Cinematographers")

        st.subheader("📦 Packages")

        st.write("**Classic – ₹2,25,000 / day**")
        st.write("**Signature – ₹4,25,000 / 2 day**")
        st.write("**Luxe – ₹6,35,000 / 3 day**")

    elif people > 300:
        st.success("✅ Recommended Team: 3 Photographers + 3 Cinematographers")

        st.subheader("📦 Packages")

        st.write("**Classic – ₹4,25,000 / day**")
        st.write("**Signature – ₹6,25,000 / 2 day**")
        st.write("**Luxe – ₹8,95,000 / 3 day**")

    # Summary
    st.write("## 📄 Summary")

    total_days = len(events)

    for i, (name, date) in enumerate(events):
        st.write(f"**Event {i+1}:** {name} on {date}")

    st.write(f"**Total Events / Days:** {total_days}")
    st.write(f"**Guests:** {people}")

    # Contact
    st.write("---")
    st.subheader("📞 Get in Touch")
    st.write("Vedant: +91 90824 24539")
