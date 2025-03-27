import os
import fitz  # PyMuPDF
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

# ChromaDB istemcisi başlat
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

# Embedding modeli yükle
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Hafif ve hızlı model

def extract_text_from_pdf(pdf_path):
    """PDF dosyasından metni çıkarır."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text.strip()
    except Exception as e:
        logging.error(f"❌ PDF işleme hatası: {pdf_path} - {e}")
        return ""

def chunk_text(text, chunk_size=500):
    """Metni küçük parçalara böler."""
    words = text.split()
    chunks = [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def get_existing_ids():
    """ChromaDB'deki mevcut belge ID'lerini alır."""
    try:
        existing_docs = collection.get(include=["metadatas"])
        return {meta["source"] for meta in existing_docs.get("metadatas", []) if "source" in meta}
    except Exception as e:
        logging.error(f"❌ ChromaDB'den mevcut ID'ler alınamadı: {e}")
        return set()

def index_pdfs(data_folder):
    """Sadece yeni PDF dosyalarını ChromaDB'ye ekler."""
    if not os.path.exists(data_folder):
        logging.error(f"❌ '{data_folder}' klasörü bulunamadı! PDF'leri ekleyin.")
        return

    pdf_files = [f for f in os.listdir(data_folder) if f.endswith(".pdf")]
    if not pdf_files:
        logging.warning(f"⚠️ '{data_folder}' klasöründe PDF bulunamadı!")
        return

    existing_ids = get_existing_ids()

    for file_name in pdf_files:
        if file_name in existing_ids:
            logging.info(f"⏩ {file_name} zaten indekslenmiş, atlanıyor.")
            continue

        file_path = os.path.join(data_folder, file_name)
        text = extract_text_from_pdf(file_path)
        if not text:
            logging.warning(f"⚠️ {file_name} içeriği boş, atlanıyor!")
            continue

        text_chunks = chunk_text(text)
        chunk_embeddings = embedding_model.encode(text_chunks).tolist()
        
        for i, (chunk, embedding) in enumerate(zip(text_chunks, chunk_embeddings)):
            collection.add(
                documents=[chunk],
                metadatas=[{"source": file_name, "chunk": i}],
                ids=[f"{file_name}_chunk_{i}"],
                embeddings=[embedding]
            )
        
        logging.info(f"✅ {file_name} -> {len(text_chunks)} parça olarak indekslendi.")

if __name__ == "__main__":
    index_pdfs("../data")