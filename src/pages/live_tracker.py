import streamlit as st
from src.components.sos_button import SOSButton
from src.components.cta_buttons import CTAButtons
from src.services.ai_guardian import AI_Guardian

def live_tracker():
    st.title("Live Tracker & AI Guardian")
    
    st.write("### AI Check-Ins")
    st.write("Our AI assistant checks in with you during travel. If you don’t respond, it alerts your emergency contacts.")
    
    # Trigger Options
    st.write("#### Trigger Options:")
    st.write("- Voice activation: Say 'Help me'")
    st.write("- Hardware trigger: Hold the volume button")
    
    # Emergency Flow Animation
    st.write("#### Emergency Flow Animation:")
    st.image("path_to_animation.gif", caption="Emergency Flow Animation")
    
    # Activate Guardian Mode
    if st.button("Activate Guardian Mode"):
        AI_Guardian.activate_guardian_mode()
        st.success("Guardian Mode Activated! You are now being monitored.")

    # SOS Button
    SOSButton()

    # Call to Action
    CTAButtons()

if __name__ == "__main__":
    live_tracker()