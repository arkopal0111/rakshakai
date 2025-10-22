from streamlit import sidebar, markdown, container

def render_header(title):
    """Render the header with the given title."""
    container().header(title)

def render_subheader(subtitle):
    """Render the subheader with the given subtitle."""
    container().subheader(subtitle)

def render_cta_button(label, url):
    """Render a call-to-action button."""
    if sidebar.button(label):
        # Logic to handle button click can be added here
        pass

def render_section(title, content):
    """Render a section with a title and content."""
    container().markdown(f"### {title}")
    container().markdown(content)

def render_testimonial(avatar_url, quote, name):
    """Render a testimonial with an avatar, quote, and name."""
    container().markdown(f"![Avatar]({avatar_url})")
    container().markdown(f"**{quote}** — *{name}*")

def render_sos_button():
    """Render a mock SOS button."""
    container().button("SOS", key="sos_button")

def render_footer(text):
    """Render the footer with the given text."""
    container().footer(text)