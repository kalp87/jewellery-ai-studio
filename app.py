import streamlit as st
from PIL import Image
import urllib.parse
import time

st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio (100% Free)")
st.write("Professional Free AI Jewellery Photoshoot Generator")

uploaded_file = st.file_uploader("Upload Jewellery Photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    orig_img = Image.open(uploaded_file)
    st.image(orig_img, caption="Original Jewellery Reference", width=320)
    
    col1, col2 = st.columns(2)
    with col1:
        model_style = st.selectbox(
            "Model & Setting Style:",
            [
                "Royal Indian Bride wearing traditional Silk Saree, studio portrait",
                "Elegant woman in designer royal attire, cinematic lighting",
                "Close-up luxury jewelry portrait, soft studio rim lighting"
            ]
        )
    with col2:
        ornament_type = st.selectbox(
            "Jewellery Details:",
            [
                "intricate gold necklace with traditional craftsmanship",
                "luxurious bridal gold jewellery piece",
                "antique handcrafted gold ornament"
            ]
        )

    if st.button("Generate Free Photoshoot"):
        with st.spinner("Photo create ho rahi hai..."):
            prompt_text = f"professional product photography, {ornament_type}, worn by {model_style}, hyperrealistic, sharp focus, 8k uhd, masterpiece"
            clean_prompt = urllib.parse.quote(prompt_text)
            
            # Free direct reliable engine (No Paywall / No Wallet)
            free_image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=768&height=1024&nologo=true&enhance=false"
            
            st.success("Generation Complete!")
            st.image(free_image_url, caption="Generated Studio Shoot", use_container_width=True)
            st.markdown(f"[📥 Image Download Link]({free_image_url})")
