from streamlit import footer

def display_footer():
    footer("""
    <style>
        .footer {
            background-color: #2C2C2C;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
        .footer a {
            color: #1FC5A8;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        <p>&copy; 2023 Rakshak.ai. All rights reserved.</p>
        <p>
            <a href="/about">About Us</a> | 
            <a href="/contact">Contact</a> | 
            <a href="/privacy">Privacy Policy</a>
        </p>
    </div>
    """, unsafe_allow_html=True)