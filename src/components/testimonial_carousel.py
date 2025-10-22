from streamlit import st
from streamlit.components.v1 import st_components

def testimonial_carousel(testimonials):
    st.markdown("<h2 style='text-align: center;'>What Our Users Say</h2>", unsafe_allow_html=True)
    
    # Create a carousel for testimonials
    for testimonial in testimonials:
        with st.container():
            st.image(testimonial['avatar'], width=50)
            st.markdown(f"<p style='font-weight: bold;'>{testimonial['name']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p>{testimonial['quote']}</p>", unsafe_allow_html=True)
            st.markdown("---")

# Example usage
if __name__ == "__main__":
    testimonials_data = [
        {"name": "Riya, Delhi", "quote": "Rakshak helped me avoid a deserted road after class.", "avatar": "path/to/avatar1.png"},
        {"name": "Ananya, Pune", "quote": "The AI check-in made my night commute peaceful.", "avatar": "path/to/avatar2.png"},
        {"name": "Neha, Gurgaon", "quote": "Finally, a safety app that feels built for us.", "avatar": "path/to/avatar3.png"},
    ]
    
    testimonial_carousel(testimonials_data)