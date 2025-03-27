import chromadb
from sentence_transformers import SentenceTransformer
import logging

# Logger ayarı
def setup_logger():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
setup_logger()

# ChromaDB istemcisini başlat
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

# Embedding modeli yükle
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Hafif ve hızlı model

def search_documents(query, top_n=3, similarity_threshold=0.8):
    """Kullanıcının sorgusuna en uygun N sonucu döndürür."""
    try:
        query_embedding = embedding_model.encode([query]).tolist()
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=top_n
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]
        
        if not documents:
            logging.warning("⚠️ Hiçbir sonuç bulunamadı!")
            return [], []
        
        filtered_results = []
        filtered_metadata = []
        
        for doc, meta, score in zip(documents, metadatas, distances):
            logging.info(f"🔍 Sonuç skoru: {score:.4f} - Kaynak: {meta.get('source', 'Bilinmeyen Kaynak')}")
            if score >= similarity_threshold:  # Eşik değer hatasını düzelttik
                filtered_results.append(doc)
                filtered_metadata.append(meta)

        if not filtered_results:
            logging.warning("⚠️ Eşik değer üzerinde sonuç bulunamadı!")
            return [], []

        return filtered_results, filtered_metadata
    
    except Exception as e:
        logging.error(f"❌ Arama sırasında hata oluştu: {e}")
        return [], []

if __name__ == "__main__":
    while True:
        query = input("\n🔎 Sorgunuzu girin (çıkış için 'exit' yazın): ")
        if query.lower() == "exit":
            print("👋 Görüşmek üzere!")
            break
        docs, meta = search_documents(query)
        
        if not docs:
            print("❌ Sonuç bulunamadı! Daha farklı bir sorgu deneyin.")
        else:
            for i, (doc, meta_data) in enumerate(zip(docs, meta)):
                source = meta_data.get("source", "Bilinmeyen Kaynak")
                print(f"\n[{i+1}] Kaynak: {source}\n{doc[:500]}...\n")