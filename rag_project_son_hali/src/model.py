import os
import torch
import logging
from transformers import AutoModelForCausalLM, AutoTokenizer

# Logging ayarları
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Hugging Face Token kontrolü
HF_TOKEN = os.getenv("HF_TOKEN")  # Çevre değişkeni olarak belirlenmişse al
if not HF_TOKEN:  
    HF_TOKEN = input("🔑 Lütfen Hugging Face tokenınızı girin: ").strip()

# Model ve cihaz ayarları
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Tokenizer ve model yükleme
logging.info(f"📥 {MODEL_NAME} modeli yükleniyor...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, 
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32, 
        device_map="auto", 
        token=HF_TOKEN
    )
    logging.info(f"✅ {MODEL_NAME} başarıyla yüklendi!")
except Exception as e:
    logging.error(f"❌ Model yüklenirken hata oluştu: {e}")
    exit(1)  # Hata durumunda programdan çık

def generate_answer(prompt, context=""):
    """LLM modelinden yanıt üretir, main.py ile uyumlu hale getirildi."""
    final_prompt = f"Question: {prompt}\nContext: {context}\nAnswer:"
    inputs = tokenizer(final_prompt, return_tensors="pt").to(DEVICE)

    try:
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=50)  # 🔹 Token limiti 50 olarak bırakıldı
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        logging.error(f"❌ Model yanıt üretemedi: {e}")
        response = "Üzgünüm, yanıt üretemedim. Lütfen daha kısa veya farklı bir soru deneyin."

    return response
