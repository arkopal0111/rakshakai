from streamlit import st

def report_form():
    st.header("Community Safety Report")
    st.write("Please fill out the form below to submit a safety report.")

    report_type = st.selectbox(
        "Select the type of report:",
        ("Broken streetlight", "Unsafe crowd", "Harassment report", "Empty area")
    )

    description = st.text_area("Description of the issue:")

    if st.button("Submit Report"):
        if description:
            # Here you would typically send the report to your backend service
            st.success("Thank you for your report! It has been submitted successfully.")
        else:
            st.error("Please provide a description of the issue.")

    st.write("Your feedback helps us improve safety in our community.")