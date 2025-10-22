import streamlit as st

def display_features():
    st.title("Key Features of Rakshak.ai")
    
    features = [
        {
            "icon": "🧭",
            "title": "SafeRoute AI",
            "description": "Finds the safest route, not the fastest."
        },
        {
            "icon": "🚨",
            "title": "Smart SOS",
            "description": "One-tap or voice-trigger emergency alerts."
        },
        {
            "icon": "🧑‍🤝‍🧑",
            "title": "Community Safety Reports",
            "description": "Real-time feedback from users."
        },
        {
            "icon": "📍",
            "title": "Nearby Safe Zones",
            "description": "Police stations, hospitals, and shelters."
        },
        {
            "icon": "🧠",
            "title": "AI Guardian",
            "description": "Virtual assistant that checks in automatically."
        },
        {
            "icon": "🔔",
            "title": "Real-Time Notifications",
            "description": "Stay updated about risky areas nearby."
        }
    ]
    
    for feature in features:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"<h1 style='font-size: 48px;'>{feature['icon']}</h1>", unsafe_allow_html=True)
        with col2:
            st.subheader(feature['title'])
            st.write(feature['description'])
            st.markdown("---")

if __name__ == "__main__":
    display_features()