from streamlit import st

def hero_section():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #7B61FF; font-family: 'Poppins', sans-serif;">Because every journey deserves safety.</h1>
            <h2 style="color: #1FC5A8; font-family: 'Open Sans', sans-serif;">AI-powered safety and navigation for women, by women.</h2>
            <div>
                <a href="https://play.google.com" target="_blank" style="margin: 10px; padding: 10px; background-color: #7B61FF; color: white; border-radius: 5px; text-decoration: none;">Download on Play Store</a>
                <a href="https://www.apple.com/app-store/" target="_blank" style="margin: 10px; padding: 10px; background-color: #1FC5A8; color: white; border-radius: 5px; text-decoration: none;">Get on App Store</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Quick SOS Mock Button
    if st.button("Quick SOS"):
        st.success("SOS activated! Your emergency contacts have been notified.")

    # Mini Intro Section
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <p style="font-family: 'Open Sans', sans-serif;">Rakshak ensures every woman reaches home safely using AI, real-time data, and community intelligence.</p>
            <img src="path_to_animated_infographic.gif" alt="Infographic" style="width: 80%;"/>
        </div>
        """,
        unsafe_allow_html=True
    )