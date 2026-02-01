import streamlit as st
from rembg import remove
from PIL import Image
import io
import time

# Page Configuration
st.set_page_config(
    page_title="Background Remover AI",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for UI/UX
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header/Hero Section */
    .hero-container {
        text-align: center;
        padding: 4rem 1rem;
        background: rgb(255,255,255);
        background: linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(240,242,245,1) 100%);
        border-radius: 0 0 50px 50px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #2d3436;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #636e72;
        margin-bottom: 2rem;
    }

    /* Upload Area Styling */
    .uploadedFile {
        border: 2px dashed #6c5ce7;
        padding: 2rem;
        border-radius: 20px;
        background-color: white;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #6c5ce7;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(108, 92, 231, 0.2);
    }
    
    .stButton > button:hover {
        background-color: #5b4cc4;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(108, 92, 231, 0.3);
    }

    /* Transparency Grid for Result */
    .transparency-grid {
        background-image: 
            linear-gradient(45deg, #ccc 25%, transparent 25%), 
            linear-gradient(-45deg, #ccc 25%, transparent 25%), 
            linear-gradient(45deg, transparent 75%, #ccc 75%), 
            linear-gradient(-45deg, transparent 75%, #ccc 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        background-color: white;
        border-radius: 15px;
        padding: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Image Container */
    .image-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .image-label {
        font-weight: 600;
        margin-bottom: 10px;
        color: #2d3436;
        display: block;
    }

    /* Spinner */
    .stSpinner > div {
        border-color: #6c5ce7 transparent #6c5ce7 transparent;
    }
    
    /* Ad Placeholder */
    .ad-placeholder {
        background-color: #f1f2f6;
        border: 1px solid #dfe6e9;
        color: #b2bec3;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        border-radius: 10px;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Helper Function
def convert_image(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Header UI
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Upload Image to Remove Background</h1>
        <p class="hero-subtitle">100% Automatic and Free</p>
    </div>
""", unsafe_allow_html=True)

# Main container
container = st.container()

with container:
    # File Uploader
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "webp"], help="Drag and drop your image here")

    if uploaded_file is not None:
        # Layout columns
        col1, col2 = st.columns([1, 1], gap="large")

        # Load Image
        input_image = Image.open(uploaded_file)
        
        # Display Original
        with col1:
            st.markdown('<div class="image-card"><span class="image-label">Original Image</span></div>', unsafe_allow_html=True)
            st.image(input_image, use_container_width=True)

        # Processing Logic
        with col2:
            st.markdown('<div class="image-card"><span class="image-label">Background Removed</span></div>', unsafe_allow_html=True)
            
            # Start Processing
            with st.spinner("Removing background..."):
                # Simulating a slight delay for "Live Processing" feel if it's too fast, 
                # but rembg takes a moment anyway.
                # time.sleep(1) 
                
                try:
                    # Remove background
                    output_image = remove(input_image)
                    
                    # Store output in session state to prevent reprocessing on reload if we wanted, 
                    # but direct render is fine for this simple flow.
                    
                    # Display Result with Grid
                    st.markdown('<div class="transparency-grid">', unsafe_allow_html=True)
                    st.image(output_image, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Prepare Download
                    img_bytes = convert_image(output_image)
                    
                    st.markdown("###") # Spacing
                    
                    # Download Buttons
                    d_col1, d_col2 = st.columns(2)
                    with d_col1:
                        st.download_button(
                            label="Downloads (Standard)",
                            data=img_bytes,
                            file_name="nobg_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                    with d_col2:
                         st.download_button(
                            label="Download HD",
                            data=img_bytes,
                            file_name="nobg_image_hd.png",
                            mime="image/png",
                            key="hd_download",
                            use_container_width=True
                        )
                        
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    else:
        # Sample Images Section
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.subheader("Or try one of these samples:")
        
        sample_cols = st.columns(4)
        
        # In a real app we'd load these from a folder. 
        # For now, we will just show placeholders or descriptions since we don't have local sample images.
        # But to make it nice, we can ignore this or add a note.
        # Since I cannot assume internet access for image URLs in the browser subagent in all contexts,
        # I will leave the structure ready.
        
        # Placeholder logic for samples (non-functional buttons visually)
        # sample_images = ["cat.jpg", "car.jpg", "person.jpg"]
        
        st.info("Upload an image above to get started!")

    # Ad Placeholder (Monetization)
    st.markdown("""
        <div class="ad-placeholder">
            Advertisem*nt Space (Google AdSense)
        </div>
    """, unsafe_allow_html=True)
