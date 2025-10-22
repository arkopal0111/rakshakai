import streamlit as st

def about_page():
    st.title("About Rakshak.ai")
    st.write("""
    Rakshak.ai is an AI-driven women's safety and navigation app designed to empower women commuters, students, night-shift workers, and families in India. Our mission is to ensure that every woman reaches home safely using advanced technology and community intelligence.
    """)

    st.subheader("How It Works")
    st.write("""
    Rakshak combines real-time data — crowd density, lighting levels, CCTV coverage, and police proximity — analyzed through Python-based machine learning models. The backend integrates Firebase for location synchronization and Google Maps API for route rendering.
    """)

    st.image("path/to/your/illustration.png", caption="AI-Powered Safety")
    
    st.subheader("Our Process")
    st.write("""
    1️⃣ Data Collection  
    2️⃣ AI Analysis  
    3️⃣ Safety Scoring  
    4️⃣ Route Recommendation  
    5️⃣ Community Feedback Loop  
    """)

    st.write("""
    Our AI models evaluate real-time crowd density, lighting quality, police proximity, and user reports to generate the safest route possible. We believe in the power of community participation to enhance safety for everyone.
    """)

    st.subheader("Join Us")
    st.write("""
    Be a part of the Rakshak community and contribute to making travel safer for women everywhere. Together, we can create a safer environment for all.
    """)

if __name__ == "__main__":
    about_page()