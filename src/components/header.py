from stbeta import st

def header():
    st.markdown(
        """
        <style>
        .header {
            background-color: #7B61FF;
            padding: 10px;
            text-align: center;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .nav-link {
            margin: 0 15px;
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        .nav-link:hover {
            text-decoration: underline;
        }
        </style>
        <div class="header">
            <h1>Rakshak.ai</h1>
            <nav>
                <a class="nav-link" href="/home">Home</a>
                <a class="nav-link" href="/safe_route_map">Safe Route Map</a>
                <a class="nav-link" href="/community_reports">Community Reports</a>
                <a class="nav-link" href="/live_tracker">Live Tracker</a>
                <a class="nav-link" href="/emergency_help">Emergency Help</a>
                <a class="nav-link" href="/about">About</a>
                <a class="nav-link" href="/features">Features</a>
                <a class="nav-link" href="/testimonials">Testimonials</a>
                <a class="nav-link" href="/contact">Contact</a>
            </nav>
        </div>
        """,
        unsafe_allow_html=True
    )