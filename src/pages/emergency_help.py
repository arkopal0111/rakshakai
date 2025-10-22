import streamlit as st

def emergency_help_page():
    st.title("Emergency Help")
    
    st.subheader("Immediate Assistance")
    
    st.write("In case of an emergency, you can activate the SOS feature to alert your emergency contacts and share your location.")
    
    # SOS Button Demo
    st.markdown("""
    <div style="text-align: center;">
        <button style="background-color: #FF4C4C; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 20px;">
            SOS
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("This button will trigger an SOS alert, sharing your GPS location and an audio snapshot.")
    
    st.write("Real-time data synchronization with Firebase ensures instant response to your SOS alerts.")
    
    st.subheader("Nearby Emergency Helplines")
    st.write("Here are some important helplines you can reach out to:")
    st.write("- Police: 100")
    st.write("- Ambulance: 112")
    st.write("- Women Helpline: 181")
    
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 18px; color: #2C2C2C;">Stay safe and remember, help is just a button away!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    emergency_help_page()