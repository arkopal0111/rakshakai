from streamlit import button, session_state

def sos_button():
    if button("🚨 SOS", key="sos_button"):
        # Trigger the SOS functionality
        session_state.sos_triggered = True
        # Here you can add the logic to handle the SOS alert
        # For example, sending a notification to emergency contacts
        # or calling an API to report the SOS
        print("SOS alert triggered!")  # Placeholder for actual SOS logic

    if getattr(session_state, 'sos_triggered', False):
        # Display a message indicating that the SOS has been triggered
        st.success("SOS alert has been sent!")