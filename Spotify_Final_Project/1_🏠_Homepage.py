import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_url = "https://lottie.host/5f64a327-5233-46f4-ab9e-d88ef2fb261c/dAatL3ybh0.json"
lottie_json = load_lottie_url(lottie_url)

# Set page layout
st.set_page_config(layout="wide")

# Add custom CSS for animation, heading, and centering Lottie
st.markdown(
    """
    <style>
    .title {
        font-size: 4em;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: bold;
        text-align: center;
        color: #1DB954;
        animation: slideIn 3s ease-in-out;
        margin-bottom: 20px;
    }
    @keyframes slideIn {
        from {
            transform: translateY(-50px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    .subtitle {
        font-size: 2em;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        color: #1DB954;
        margin-bottom: 20px;
    }
    .lottie-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with animation
st.markdown('<div class="title">Welcome to Spotify Song Recommendations!</div>', unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">Find your next favorite song with AI-powered recommendations</div>', unsafe_allow_html=True)

# Lottie animation centered
st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
if lottie_json:
    st_lottie(lottie_json, speed=1, height=300, width=300, key="centered_lottie")
st.markdown('</div>', unsafe_allow_html=True)

# Add the image below the heading and animation
st.image(
    "https://images.pexels.com/photos/2322727/pexels-photo-2322727.jpeg",
    caption="Discover new tracks, albums, and artists.",
    use_container_width=True,
)







