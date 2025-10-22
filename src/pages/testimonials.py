from streamlit import st
from src.components.testimonial_carousel import testimonial_carousel

def testimonials_page():
    st.title("Testimonials")
    st.subheader("What Our Users Say")

    # Display the testimonial carousel
    testimonial_carousel()

if __name__ == "__main__":
    testimonials_page()