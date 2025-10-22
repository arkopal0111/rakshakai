import streamlit as st

def contact_page():
    st.title("Contact Us")
    st.subheader("We'd love to hear from you!")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you — our team will reach out soon.")

    st.markdown("### Follow Us")
    st.markdown("[Instagram](https://instagram.com/rakshak.ai) | [LinkedIn](https://linkedin.com/company/rakshak-ai) | [Twitter](https://twitter.com/rakshak_ai)")
    st.markdown("For immediate assistance, contact us at: [support@rakshak.ai](mailto:support@rakshak.ai)")

contact_page()