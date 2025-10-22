import streamlit as st
from src.components.map_widget import MapWidget

def safe_route_map():
    st.title("SafeRoute Map")
    st.subheader("AI-Powered Navigation for Your Safety")

    st.write("""
    Our AI models evaluate real-time crowd density, lighting quality, police proximity, and user reports to generate the safest route possible.
    """)

    # Display the map widget
    MapWidget()

    st.write("### Safe Routes and Risk Zones")
    st.write("""
    - **Safe Routes**: Indicated by a green glow on the map.
    - **Risk Zones**: Highlighted in red/orange heatmap.
    - **CCTV and Lighting Coverage**: Shown with pin icons on the map.
    """)

    st.write("Hover over the indicators on the map for more information.")

if __name__ == "__main__":
    safe_route_map()