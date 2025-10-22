import streamlit as st
from components.hero import Hero
from components.sos_button import SOSButton
from components.cta_buttons import CTAButtons

def home():
    st.title("Rakshak.ai")
    
    # Hero Section
    Hero()

    # Quick SOS Button
    SOSButton()

    # Mini Intro Section
    st.subheader("Empowering Women Commuters")
    st.write("Rakshak ensures every woman reaches home safely using AI, real-time data, and community intelligence.")
    
    # Animated infographic (placeholder)
    st.image("assets/infographic.png", caption="Key Pillars: AI | Awareness | Action", use_column_width=True)

    # Call to Action Buttons
    CTAButtons()

if __name__ == "__main__":
    home()