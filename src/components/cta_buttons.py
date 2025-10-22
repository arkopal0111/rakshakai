from streamlit import button, markdown

def cta_buttons():
    # Call-to-Action Buttons
    markdown("<h2 style='text-align: center;'>Take Safety Into Your Own Hands</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if button("Download on Play Store"):
            # Add functionality for Play Store link
            pass
    
    with col2:
        if button("Get on App Store"):
            # Add functionality for App Store link
            pass
    
    st.markdown("<h3 style='text-align: center;'>Join the Safety Movement</h3>", unsafe_allow_html=True)
    if button("Join Community"):
        # Add functionality for joining community
        pass