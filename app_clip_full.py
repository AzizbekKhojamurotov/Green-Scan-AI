
import streamlit as st
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="GreenScanAI",
    page_icon="GSA_Logo.png",  # your uploaded logo file path
    layout="wide"
)
# st.title("♻️ GreenScanAI")
col1, col2 = st.columns([1, 5])

with col1:
    st.image("GSA_Logo.png", width=80)

with col2:
    st.title("♻️ GreenScanAI")
# Load model
@st.cache_resource
def load_model():
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    model.eval()
    return processor, model

processor, model = load_model()

# Waste categories
classes = ["a plastic bottle", "a crumpled paper", "a rusty metal can", "a banana peel", "an electronic waste item"]
labels = ["plastic", "paper", "metal", "food", "e-waste"]

# App tabs
tab1, tab2, tab3, tab4 = st.tabs(["📷 Scan", "🌿 Eco Coins", "🗺️ GreenMap", "👤 Profile"])

with tab1:
    st.header("Scan a Waste Item (AI Recognition)")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, use_column_width=True)

        inputs = processor(text=classes, images=image, return_tensors="pt", padding=True).to(model.device)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits_per_image
            probs = logits.softmax(dim=1).squeeze()

        idx = torch.argmax(probs).item()
        predicted_class = labels[idx]
        confidence = probs[idx].item() * 100

        st.success(f"✅ Identified as: **{predicted_class.upper()}** ({confidence:.2f}%)")

        info = {
            "plastic": ("500 years to degrade", "Can be recycled into new bottles", "Plastic Bin"),
            "paper": ("2 months to degrade", "Saves 60% energy", "Paper Bin"),
            "metal": ("50 years to degrade", "Saves 95% energy", "Metal Bin"),
            "food": ("Produces methane gas", "Used for compost", "Organic Bin"),
            "e-waste": ("Highly toxic heavy metals", "Parts can be reused", "E-waste Bin"),
        }

        harm, benefit, bin_type = info[predicted_class]
        st.write(f"🌍 Environmental Harm: {harm}")
        st.write(f"✅ Recycling Benefit: {benefit}")
        st.write(f"🗑️ Recommended Bin: {bin_type}")
        st.success("+10 Eco Coins added!")

with tab2:
    st.header("Eco Coin Dashboard")
    st.metric(label="Your Eco Coin Balance", value="370 Coins")
    st.progress(370 / 10000)
    st.caption("Earn 10,000 coins to unlock premium rewards!")

with tab3:
    st.header("Nearby Drop-off Points")
    m = folium.Map(location=[41.3111, 69.2797], zoom_start=12)
    folium.Marker([41.3200, 69.2420], tooltip="Plastic Bin").add_to(m)
    folium.Marker([41.3050, 69.2850], tooltip="Paper Bin").add_to(m)
    folium.Marker([41.3100, 69.2700], tooltip="E-waste Bin").add_to(m)
    st_folium(m, width=700, height=500)

with tab4:
    st.header("User Profile")
    st.write("👤 Name: Azizbek Khojamurotov")
    st.write("📧 Email: azizbekxojamurotov2001@gmail.com")
    st.write("🧾 Total Items Scanned: 37")
    st.write("🏆 Eco Rank: Green Ambassador")
