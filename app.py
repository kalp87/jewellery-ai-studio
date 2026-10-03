import streamlit as st
from PIL import Image
import requests
import io

st.set_page_config(page_title="Jewellery AI Studio", layout="wide")
st.title("💎 Jewellery AI Studio")
st.write("Professional Jewellery Photoshoot Generator")

hf_token = st.sidebar.text_input("Enter Hugging Face API Token:", type="password")

uploaded_file = st.file_uploader("Upload Jewellery Photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    orig_img = Image.open(uploaded_file)
    st.image(orig_img, caption="Original Jewellery", width=350)
    
    model_style = st.selectbox(
        "Choose Model Style / Setting:",
        [
            "Royal Indian Bride wearing traditional Silk Saree, warm studio lighting",
            "Modern elegant woman wearing evening gown, soft cinematic spotlight",
            "Minimalist aesthetic model, close-up portrait, clean neutral studio background"
        ]
    )
    
    custom_prompt = st.text_input("Extra Details (Optional):", value="")
    
    if st.button("Generate Professional Shoot"):
        if not hf_token:
            st.error("Please enter Hugging Face Token in the sidebar.")
        else:
            with st.spinner("AI model shoot generate ho raha hai..."):
                API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
                headers = {"Authorization": f"Bearer {hf_token}"}
                
                final_prompt = f"Professional jewelry photography, sharp focus, {model_style}, {custom_prompt}, 8k uhd, highly detailed, realistic skin texture"
                payload = {
                    "inputs": final_prompt,
                    "parameters": {"negative_prompt": "blurry, deformed, low quality, distorted"}
                }
                
                try:
                    response = requests.post(API_URL, headers=headers, json=payload)
                    if response.status_code == 200:
                        res_img = Image.open(io.BytesIO(response.content))
                        st.success("Generation Complete!")
                        st.image(res_img, caption="AI Generated Shoot", use_container_width=True)
                    else:
                        st.warning("Model abhi load ho raha hai. Kripya 30 second baad dobara click karein.")
                except Exception as e:
                    st.error(f"Error: {e}")
