from streamlit import st
import folium
from streamlit_folium import st_folium

def display_map():
    # Create a Folium map centered around a specific location
    m = folium.Map(location=[28.6139, 77.2090], zoom_start=12)  # Example: New Delhi coordinates

    # Add safe route markers (example data)
    safe_route = [[28.6139, 77.2090], [28.6150, 77.2100], [28.6160, 77.2110]]
    folium.PolyLine(safe_route, color='green', weight=5, opacity=0.7).add_to(m)

    # Add risk zone markers (example data)
    risk_zone = [[28.6120, 77.2080], [28.6100, 77.2070]]
    for location in risk_zone:
        folium.CircleMarker(location, radius=10, color='red', fill=True, fill_color='red', fill_opacity=0.6).add_to(m)

    # Add CCTV and lighting coverage markers (example data)
    cctv_locations = [[28.6140, 77.2095], [28.6155, 77.2105]]
    for location in cctv_locations:
        folium.Marker(location, icon=folium.Icon(color='blue', icon='info-sign')).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=725)

def main():
    st.title("SafeRoute Map")
    st.write("Our AI models evaluate real-time crowd density, lighting quality, police proximity, and user reports to generate the safest route possible.")
    display_map()

if __name__ == "__main__":
    main()