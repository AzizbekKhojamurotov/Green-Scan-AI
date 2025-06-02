# 🌿 GreenScanAI

**GreenScanAI** is a mobile web application (MVP) that uses artificial intelligence to detect and analyze waste, encouraging users to make environmentally conscious decisions.

This project was developed within the framework of the **Eco Expo Central Asia 2025**, aiming to reduce environmentally harmful waste, promote recycling, and support the development of **green technologies** by providing useful incentives to the public.

---

## 🔍 Main Features

- 📷 **AI-powered waste classification** (based on the CLIP model)  
- 🌿 **Environmental recommendations**: harmful impact, recycling benefits, bin direction  
- 💰 **Eco Coin system**: users collect points for their activity  
- 🗺️ **GreenMap**: displays nearby waste bins on the map  
- 👤 **Profile**: personal statistics, rank, and motivational interface  

---

## 🚀 MVP Technologies

- `Python` & `Streamlit` — frontend and backend  
- `Hugging Face Transformers` — AI model (CLIP)  
- `Torch` — to run the model  
- `Folium` & `Streamlit-Folium` — map module  
- `Pillow` — working with images  
- (In the future: `Firebase` for database and authentication)

---

## 🧪 Launch

```bash
pip install -r requirements.txt
streamlit run app.py