import streamlit as st
from PIL import Image
import urllib.parse
import time

st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio (Fast & Reliable)")
st.write("Instant Free AI Jewellery Photoshoot Generator")

uploaded_file = st.file_uploader("Upload Jewellery Photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    orig_img = Image.open(uploaded_file)
    st.image(orig_img, caption="Original Jewellery Reference", width=320)
    
    col1, col2 = st.columns(2)
    with col1:
        model_style = st.selectbox(
            "Model & Background Style:",
            [
                "Royal Indian bride in red bridal saree, studio lights, closeup jewelry portrait",
                "Indian royal woman in blue banarasi silk saree, elegant jewelry photoshoot",
                "Modern elegant woman in luxury emerald attire, clean studio portrait",
                "High end luxury jewelry studio showcase, blurred bokeh background"
            ]
        )
    with col2:
        ornament_type = st.selectbox(
            "Ornament Type:",
            [
                "intricate gold filigree necklace with hanging tassels",
                "traditional gold necklace set with ruby stones",
                "heavy Indian bridal gold jewelry collection",
                "antique handcrafted gold choker"
            ]
        )

    custom_notes = st.text_input("Extra Details (Optional):", value="sharp focus, 8k uhd, photorealistic")

    if st.button("Generate Shoot"):
        with st.spinner("AI photo load ho rahi hai..."):
            # Clean prompt
            full_prompt = f"{ornament_type}, worn by {model_style}, {custom_notes}, high quality, realistic lighting"
            encoded_prompt = urllib.parse.quote(full_prompt)
            
            # Seed for unique render
            seed = int(time.time())
            
            # Reliable ultra-fast endpoint (bypasses server timeout)
            direct_image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=1024&seed={seed}&nologo=true"
            
            # Direct display
            st.success("Photoshoot ready!")
            st.image(direct_image_url, caption="Generated Studio Shoot", use_container_width=True)
            st.markdown(f"[📥 Click yahan karein Image Download karne ke liye]({direct_image_url})")
