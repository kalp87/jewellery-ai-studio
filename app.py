import streamlit as st
from PIL import Image
import requests
import io

st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio (FLUX Engine)")
st.write("Professional Free AI Jewellery Photoshoot Generator")

hf_token = st.sidebar.text_input("Enter Hugging Face API Token (hf_...):", type="password")

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
                "Indian royal woman in blue silk saree, elegant jewelry photoshoot",
                "Modern elegant woman in evening luxury attire, studio portrait"
            ]
        )
    with col2:
        ornament_type = st.selectbox(
            "Ornament Type:",
            [
                "intricate gold necklace with traditional craftsmanship",
                "luxurious bridal gold necklace set",
                "antique handcrafted gold choker"
            ]
        )

    if st.button("Generate Photoshoot"):
        if not hf_token:
            st.warning("Please left sidebar me apna Hugging Face Token paste karein.")
        else:
            with st.spinner("FLUX engine se photo create ho rahi hai..."):
                # Supported Serverless Model on HF Router
                API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
                headers = {"Authorization": f"Bearer {hf_token}"}
                
                prompt = f"hyperrealistic professional jewelry shoot, authentic Indian gold craftsmanship, {ornament_type}, worn by {model_style}, intricate gold filigree, sharp focus, 8k uhd, photorealistic skin"
                payload = {
                    "inputs": prompt
                }
                
                try:
                    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                    if response.status_code == 200:
                        res_image = Image.open(io.BytesIO(response.content))
                        st.success("Photoshoot ready!")
                        st.image(res_image, caption="Generated Studio Shoot", use_container_width=True)
                        
                        buf = io.BytesIO()
                        res_image.save(buf, format="JPEG")
                        st.download_button(
                            label="Download High-Res Image",
                            data=buf.getvalue(),
                            file_name="jewellery_shoot.jpg",
                            mime="image/jpeg"
                        )
                    elif response.status_code == 503:
                        st.info("Server model load kar raha hai. Kripya 20-30 second wait karke dubara button dabayein.")
                    else:
                        st.error(f"Server response: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
