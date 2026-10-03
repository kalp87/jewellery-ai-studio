import streamlit as st
from PIL import Image
import requests
import io
from rembg import remove

# Page Setup
st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio & Virtual Try-On")
st.write("Professional product photoshoot and model try-on generator")

# Sidebar for configuration
st.sidebar.header("Settings")
hf_token = st.sidebar.text_input("Enter Hugging Face API Token:", type="password")

# Upload jewelry image
uploaded_file = st.file_uploader("Upload Jewellery Photo (Necklace, Earrings, etc.)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        orig_img = Image.open(uploaded_file)
        st.image(orig_img, use_container_width=True)
        
    with col2:
        st.subheader("Clean Isolated Piece")
        clean_img = remove(orig_img)
        st.image(clean_img, use_container_width=True)

    st.markdown("---")
    st.subheader("✨ Generate AI Model Shoot")
    
    model_style = st.selectbox(
        "Choose Model Style / Setting:",
        [
            "Royal Indian Bride wearing traditional Silk Saree, warm studio lighting",
            "Modern elegant woman wearing evening gown, soft cinematic spotlight",
            "Minimalist aesthetic model, close-up portrait, clean neutral studio background"
        ]
    )
    
    custom_prompt = st.text_input("Custom Details (Optional):", value="")
    
    if st.button("Generate Professional Shoot"):
        if not hf_token:
            st.error("Please enter your Hugging Face API Token in the sidebar.")
        else:
            with st.spinner("AI model shoot generate ho raha hai... (Design lock active)"):
                API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
                headers = {"Authorization": f"Bearer {hf_token}"}
                
                final_prompt = f"Professional jewelry photography, sharp focus, {model_style}, {custom_prompt}, 8k uhd, highly detailed, realistic skin texture"
                
                payload = {
                    "inputs": final_prompt,
                    "parameters": {"negative_prompt": "blurry, deformed jewelry, low resolution, bad hands, distorted gold"}
                }
                
                try:
                    response = requests.post(API_URL, headers=headers, json=payload)
                    if response.status_code == 200:
                        result_image = Image.open(io.BytesIO(response.content))
                        st.success("Generation Complete!")
                        st.image(result_image, caption="AI Generated Shoot", use_container_width=True)
                    else:
                        st.warning("Model load ho raha hai ya busy hai, 30 second me dobara click karein.")
                except Exception as e:
                    st.error(f"Error: {e}")
