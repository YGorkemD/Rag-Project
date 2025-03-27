import logging
from search import search_documents  
from model import generate_answer  

# Logging ayarları
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def answer_query(user_query):  
    """Kullanıcının sorusuna ChromaDB'den bilgi alıp LLaMA modeli ile yanıt üretir."""  
    logging.info(f"🔍 Sorgu alındı: {user_query}")  
    
    # ChromaDB’den en alakalı belgeleri getir
    docs, _ = search_documents(user_query)
    
    if not docs:
        logging.warning("⚠️ Aranan sorgu ile ilgili yeterli veri bulunamadı.")
        return "Üzgünüm, bu konuda yeterli veri bulunamadı. Lütfen daha farklı bir soru deneyin."
    
    # Bağlamı oluştur (En fazla 4000 karakter)
    context = " ".join(docs)[:4000]
    
    # Model için uygun prompt hazırla
    final_prompt = f"Question: {user_query}\nContext: {context}\nAnswer:"
    
    # Modelden cevap al
    response = generate_answer(final_prompt)
    
    return response

if __name__ == "__main__":  
    logging.info("🟢 Sistem başlatıldı. Kullanıcı sorguları bekleniyor...")  

    while True:  
        user_query = input("\nEnter your question (or type 'exit' to quit): ").strip()
        
        if user_query.lower() == "exit":
            logging.info("🔴 Sistem durduruldu. Programdan çıkılıyor...")
            print("Goodbye!")
            break
        
        response = answer_query(user_query)
        print("\nResponse:\n", response)
