import streamlit as st
from src.components.report_form import report_form
from src.services.firebase_service import submit_report, get_reports

def community_reports():
    st.title("Community Reports")
    st.subheader("Share your safety feedback and contribute to the community.")

    # Report submission form
    report_form()

    # Display recent reports
    st.subheader("Recent Community Reports")
    reports = get_reports()
    
    if reports:
        for report in reports:
            st.write(f"**Report Type:** {report['type']}")
            st.write(f"**Location:** {report['location']}")
            st.write(f"**Description:** {report['description']}")
            st.write(f"**Submitted On:** {report['timestamp']}")
            st.write("---")
    else:
        st.write("No reports available at the moment.")

if __name__ == "__main__":
    community_reports()