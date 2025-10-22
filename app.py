import streamlit as st
from src.components.header import header
from src.components.footer import footer

# Set the page configuration
st.set_page_config(page_title="Rakshak.ai", page_icon="🚨", layout="wide")

# Render the header
header()

# Create a sidebar for navigation
st.sidebar.title("Navigation")
pages = {
    "Home": "home",
    "SafeRoute Map": "safe_route_map",
    "Community Reports": "community_reports",
    "Live Tracker": "live_tracker",
    "Emergency Help": "emergency_help",
    "About": "about",
    "Features": "features",
    "Testimonials": "testimonials",
    "Contact": "contact"
}
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
if selection == "Home":
    from src.pages.home import show_home
    show_home()
elif selection == "SafeRoute Map":
    from src.pages.safe_route_map import show_safe_route_map
    show_safe_route_map()
elif selection == "Community Reports":
    from src.pages.community_reports import show_community_reports
    show_community_reports()
elif selection == "Live Tracker":
    from src.pages.live_tracker import show_live_tracker
    show_live_tracker()
elif selection == "Emergency Help":
    from src.pages.emergency_help import show_emergency_help
    show_emergency_help()
elif selection == "About":
    from src.pages.about import show_about
    show_about()
elif selection == "Features":
    from src.pages.features import show_features
    show_features()
elif selection == "Testimonials":
    from src.pages.testimonials import show_testimonials
    show_testimonials()
elif selection == "Contact":
    from src.pages.contact import show_contact
    show_contact()

# Render the footer
footer()