import streamlit as st
from PIL import Image
import urllib.parse
import requests
import io
import time

st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio (Instant)")
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
                "Royal Indian Bride wearing traditional Red and Gold Silk Saree, royal bridal look, professional studio lighting",
                "Elegant Indian woman in Navy Blue designer saree, realistic skin texture, modern bridal portrait",
                "Close-up high-end luxury jewellery photoshoot, soft cinematic spotlight, blurry royal background",
                "Modern elegant woman wearing emerald green evening attire, studio photoshoot"
            ]
        )
    with col2:
        ornament_type = st.selectbox(
            "Ornament Type:",
            [
                "Gold necklace with intricate filigree and hanging droplets",
                "Gold choker necklace set",
                "Traditional gold earrings jhumka",
                "Gold bangles and kada set"
            ]
        )

    custom_notes = st.text_input("Extra Details (Optional):", placeholder="e.g. glowing jewelry, 8k uhd, sharp focus")

    if st.button("Generate Instant Shoot"):
        with st.spinner("AI model shoot generate ho raha hai (instant)..."):
            # Construct high quality realistic prompt
            full_prompt = (
                f"hyperrealistic professional jewelry shoot, authentic Indian gold craftsmanship, "
                f"{ornament_type}, worn by {model_style}, {custom_notes}, "
                f"intricate gold filigree details, sharp focus, 8k uhd photography, dramatic studio rim lighting, photorealistic skin pores"
            )
            
            encoded_prompt = urllib.parse.quote(full_prompt)
            # Seed to ensure fresh generation every click
            seed = int(time.time())
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=1024&seed={seed}&model=flux&nologo=true"
            
            try:
                response = requests.get(image_url, timeout=40)
                if response.status_code == 200:
                    generated_img = Image.open(io.BytesIO(response.content))
                    st.success("Photo Generated Successfully!")
                    st.image(generated_img, caption="Generated Studio Shoot", use_container_width=True)
                    
                    # Download button
                    buf = io.BytesIO()
                    generated_img.save(buf, format="JPEG")
                    byte_im = buf.getvalue()
                    st.download_button(
                        label="Download High-Res Image",
                        data=byte_im,
                        file_name="jewellery_shoot.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.error("Generation me error aaya. Kripya dubara click karein.")
            except Exception as e:
                st.error(f"Error: {e}")
