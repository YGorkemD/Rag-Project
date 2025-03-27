# LLM Tabanlı Retrieval-Augmented Generation (RAG) Sistemi

## 📌 Proje Açıklaması
Bu proje, **Büyük Dil Modelleri (LLM)** ile **Retrieval-Augmented Generation (RAG)** tekniğini kullanarak belge tabanlı sorgu yanıtları üreten bir sistem geliştirmeyi amaçlar. Sistemde:
- **Llama 2** dil modeli kullanılır.
- **ChromaDB** ile dış veri kaynakları indekslenir ve sorgulamalar yapılır.
- **Python**, **Hugging Face Transformers**, **SentenceTransformers** ve **PyMuPDF** gibi teknolojilerle entegrasyon sağlanır.

## 📂 Proje Yapısı
```
/rag_project
│── data/                  # PDF dosyaları burada olacak  
│── models/                # Model dosyaları  
│── src/                   # Ana kodların olduğu klasör  
│   │── preprocess.py      # PDF işleme ve indeksleme kodları  
│   │── search.py          # ChromaDB ile sorgu yapma  
│   │── model.py           # Llama entegrasyonu  
│   │── main.py            # Ana çalıştırılabilir dosya  
│── README.md              # Proje dokümantasyonu  
│── requirements.txt       # Gereklilikleri listele  
```

## 🔧 Minimum Sistem Gereksinimleri
Bu proje yüksek işlem gücü gerektiren **Llama 2** modelini kullandığı için minimum sistem gereksinimleri aşağıdaki gibidir:

| Bileşen            | Minimum Gereksinim       | Önerilen Gereksinim |
|--------------------|-------------------------|---------------------|
| **İşlemci (CPU)** | Intel i7 / Ryzen 7       | Intel i9 / Ryzen 9 |
| **Bellek (RAM)**  | 16 GB                    | 32 GB              |
| **Ekran Kartı (GPU)** | NVIDIA RTX 3090 (24GB VRAM) | NVIDIA A100 (40GB VRAM) |
| **Depolama**      | 50 GB boş alan (SSD önerilir) | 100 GB boş alan (NVMe SSD) |
| **İşletim Sistemi** | Linux veya Windows 10+ | Linux (Ubuntu 20.04+) |

> **⚠️ Düşük sistemlerde çalıştırmak için:** Eğer sisteminizin VRAM kapasitesi düşükse, **CPU ile çalıştırmak** için model yükleme parametrelerinde `torch_dtype=torch.float32` kullanabilirsiniz ancak bu çok yavaş olacaktır.

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Gerekli Kütüphaneleri Yükleyin
```
pip install -r requirements.txt
```

### 2️⃣ PDF Dosyalarını İşleyin ve İndeksleyin
```
python src/preprocess.py
```
📌 **Bu adım PDF'leri metne çevirir, embedding oluşturur ve ChromaDB'ye kaydeder.**

### 3️⃣ ChromaDB ile Arama Yapın
```
python src/search.py
```
📌 **Bu adım kullanıcı sorgularına uygun belgeleri bulur ve gösterir.**

### 4️⃣ Llama Modelini Test Edin
```
python src/model.py
```
📌 **Bu adım yalnızca Llama modelini test etmek için kullanılır.**

### 5️⃣ Tam Sistemi Çalıştırın
```
python src/main.py
```
📌 **Bu adım ChromaDB’den veri alıp, Llama modeline vererek tam bir yanıt üretir.**

## 📊 Kullanılan Teknolojiler
- **Python** (Ana programlama dili)
- **Hugging Face Transformers** (LLM entegrasyonu için)
- **ChromaDB** (Vektör tabanlı arama motoru)
- **SentenceTransformers** (Embedding üretimi için)
- **PyMuPDF (fitz)** (PDF işleme için)
- **Torch** (Derin öğrenme kütüphanesi)

## 🛠 Karşılaşılabilecek Sorunlar ve Çözümleri

### **1️⃣ CUDA Out of Memory Hatası**
**Çözüm:** Daha düşük boyutlu bir model kullanabilir veya `torch_dtype=torch.float32` ayarı ile CPU üzerinden çalıştırabilirsiniz.

### **2️⃣ Hugging Face Token Hatası**
**Çözüm:** `HF_TOKEN` değerinizin doğru olduğundan emin olun ve Hugging Face hesabınıza giriş yaparak doğrulayın.

### **3️⃣ Modelin Yavaş Çalışması**
**Çözüm:**
- Eğer GPU kullanıyorsanız, **VRAM yetersiz olabilir**. Daha güçlü bir GPU tercih edin.
- CPU modunda çalıştırıyorsanız, **çok uzun yanıtlar yerine `max_new_tokens=50` gibi bir limit koyun**.
- **Daha hafif bir model (örneğin Llama-2-7B yerine Llama-2-3B) seçin**.



# Örnek Sorgular ve Yanıtlar
### Aşağıda sistemin verdiği bazı örnek sorgular ve yanıtları bulunmaktadır.

### 1 

PS C:\Users\YavuzCan\Desktop\rag_project_(2)> & C:/Users/YavuzCan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/YavuzCan/Desktop/rag_project_(2)/src/main.py"
2025-03-22 17:55:11,516 - INFO - Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.
2025-03-22 17:55:11,758 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-03-22 17:55:14,816 - INFO - 🔧 PyTorch CPU optimizasyonu aktif! 6 çekirdek kullanılacak.
2025-03-22 17:55:14,816 - INFO - 📥 meta-llama/Llama-2-7b-chat-hf modeli yükleniyor...
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:16<00:00,  8.48s/it] 
2025-03-22 17:55:32,929 - WARNING - Some parameters are on the meta device because they were offloaded to the cpu and disk.
2025-03-22 17:55:32,932 - INFO - ✅ Model başarıyla yüklendi!
2025-03-22 17:55:32,932 - INFO - 🟢 Sistem başlatıldı. Kullanıcı sorguları bekleniyor...
Enter your question (or type 'exit' to quit): How often should Lapidus Corebeserviced?
2025-03-22 17:56:01,004 - INFO - 🔍 Sorgu alındı: How often should Lapidus Corebeserviced?
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  5.68it/s]
2025-03-22 17:56:01,432 - INFO - 🔍 Sonuç skoru: 1.5583 - Kaynak: 220041_Lapidus-Core-Warranty.pdf
2025-03-22 17:56:01,432 - INFO - 🔍 Sonuç skoru: 1.6587 - Kaynak: 220041_Lapidus-Core-Maintenance-Procedures.pdf
2025-03-22 17:56:01,432 - INFO - 🔍 Sonuç skoru: 1.6994 - Kaynak: 220041_Lapidus-Core-Installation-Instructions.pdf

Response:
 Question: Question: How often should Lapidus Corebeserviced?
Context:

Date: 06/01/21

Supersedes: 10/14/19

Milliken Commercial Modular Carpet Warranties
These warranties are subject to the Warranty Terms and Conditions provided at the end of this document and
apply only to commercial modular carpet products sold by Milliken. Details about the test methods supporting
these warranties are available upon request.


WARRANTIES APPLICABLE TO ALL MILLIKEN COMMERCIAL MODULAR PRODUCTS:
(See additional warranties under Specialty Product Limited Warranties below.)


FACE FIBER WEAR
Milliken warrants that the carpet will lose no more than ten percent (10%) of its face fiber by weight during the
Lifetime of the carpet. If the carpet is installed on stairs, this warranty will be limited to five years. A claim against
this warranty requires the submittal of a sample (one square yard minimum) of unused attic stock and a like-size
piece of carpet from the area that is believed to be worn beyond the terms of this warranty. These samples will
be submitted to an independent testing lab for verification.

STAINING/SOILING RESISTANCE (StainSmart®)
StainSmart provides lifetime resistance for your carpet against penetrating stains and soil.

COLOR PATTERN PERMANENCY
Milliken warrants that the carpet will exhibit no pattern loss during the Lifetime of the carpet. If the carpet is
installed on stairs this warranty will be limited to five years.


DELAMINATION OF BACKING
Milliken warrants that the backing of the carpet will not delaminate during the Lifetime of the carpet.

EDGE RAVEL
Milliken warrants that the carpet will exhibit no edge ravel or “zippering” during the Lifetime of the carpet.

TUFT BIND
Milliken warrants that the carpet will maintain its tuft bind integrity during the Lifetime of the carpet.
.
FLOOR COMPATIBILITY
Milliken warrants that the carpet will not cause a reactivation of old adhesives due to plasticizer migration during
the Lifetime of the carpet.

ANTISTATIC
Milliken warrants that the carpet will not generate static shock greater than 3.5 kilovolts during the Lifetime of
the carpet.

FLAMMABILITY

Milliken warrants that at the time of shipment the carpet will comply with the applicable provisions of the
Federal Flammable Fabrics Act for carpet used as floor covering in commercial installations. Milliken does not
represent that this or any other carpet fabric will not burn or generate smoke under actual fire conditions.

CUSHION RESILIENCY
Milliken warrants that the modular carpet with WellBAC™ cushion will retain 90% of its cushion resilience
during the Lifetime of the modular carpet.

DIMENSIONAL STABILITY
Milliken warrants that the modular carpet will maintain its dimensional stability during the Lifetime of the
modular carpet.

FLOOR RELEASE
Milliken warrants that the initial installation of the modular carpet will release from the floor during the Lifetime
of the modular carpet.

TOP DOWN MOISTURE RESISTANCE
Milliken warrants that the modular carpet will resist moisture penetration during the Lifetime of the modular
carpet. This warranty does not include moisture penetration at the seams of modular carpet.

SITE RELATED SOLUTIONS
Additional warranties may apply when Milliken Non-Reactive Standard or Milliken Mosaic Moisture XT
Adhesive is used with Milliken Modular Carpet Tile. Click on one of the links below to learn more:

Milliken Non-Reactive Standard Adhesive – Warranty

Milliken Mosaic Moisture XT Spray Adhesive - Warranty

SPECIALTY PRODUCT LIMITED WARRANTIES:

TRACTIONBACK® MODULAR CARPET
Milliken warrants that at the time of shipment, modular carpet with TractionBack will maintain sufficient bond
strength to hold the modular carpet in place under normal foot traffic use for ten (10) years.

ENTRY BARRIER CARPET (OBEX® TILE)
Milliken warrants that the OBEX Tile entry barrier carpet will lose no more than ten percent (10%) of its face
fiber b
Answer:
Lapidus Core Beserviced every 6 months.


Enter your question (or type 'exit' to quit): exit
2025-03-22 18:10:34,350 - INFO - 🔴 Sistem durduruldu. Programdan çıkılıyor...
Goodbye!


### 2 

PS C:\Users\YavuzCan\Desktop\rag_project_(2)> & C:/Users/YavuzCan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/YavuzCan/Desktop/rag_project_(2)/src/main.py"
2025-03-22 17:34:14,708 - INFO - Use pytorch device_name: cpu
2025-03-22 17:34:14,709 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-03-22 17:34:17,319 - INFO - 🔧 PyTorch CPU optimizasyonu aktif! 6 çekirdek kullanılacak.
2025-03-22 17:34:17,320 - INFO - 📥 meta-llama/Llama-2-7b-chat-hf modeli yükleniyor...
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:15<00:00,  7.57s/it] 
2025-03-22 17:34:33,614 - WARNING - Some parameters are on the meta device because they were offloaded to the cpu and disk.
2025-03-22 17:34:33,617 - INFO - ✅ Model başarıyla yüklendi!

Enter your question (or type 'exit' to quit): What tools are needed for Lapidus Core installation?
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  5.52it/s]

2025-03-22 17:34:57,622 - INFO - 🔍 Sonuç skoru: 1.6899 - Kaynak: 220041_Lapidus-Core-Installation-Instructions.pdf
2025-03-22 17:34:57,622 - INFO - 🔍 Sonuç skoru: 1.8515 - Kaynak: 220041_Lapidus-Core-Maintenance-Procedures.pdf
2025-03-22 17:34:57,622 - INFO - 🔍 Sonuç skoru: 2.0269 - Kaynak: 220041_Lapidus-Core-Warranty.pdf

Response:
 Question: Question: What tools are needed for Lapidus Core installation?
Context:
 Modular Carpet Installation InstructionsThese instructions are for use ONLYwith WellBAC
™Comfort Plus® cushion backandWellBAC
™Comfort cushionbackmodular carpet. DO NOT use these instructions or any Milliken Adhesive to install carpet containing PVC.APPLICABLE CRI INSTALLATION METHODS:  Except where exceeded or modified by this instruction, Milliken recognizes the CRI Carpet Installation Standard104 Standard for Installation of Commercial Carpet, September 2015 asthe minimum acceptable standard for the installation of its carpet products.NOTE:Installation contractor 
is responsible for reasonable inspection of the product prior to installation and for maintenance of dyelot integrity during installation. Should problems be discovered during inspection, please contact your local Milliken sales representative or call Toll Free 1-800-528-8453 –Select Option #2.  Milliken will not be responsible for visible defects after carpet has been installed.GENERAL:AllMilliken modular carpet is designed for installation without permanent adhesives. This allows easy removal and reinstallation. Installation contractor should review these instructions before starting the actual installation. As a first preference, Millikenstrongly recommendsthe use of a Milliken Certified Installation Contractorto install its products. As an alternatesource, companies that can document that they employ installers certified at the C-2 level or higher by the International Certified Floorcovering Installers Association (CFI)are also recognized as viable sources of quality installation. TILE ORIENTATION: Some Milliken designs require specific installation methods (Quarter-turn, Ashlar, etc.) to achieve the intended appearance.   PRIOR TO INSTALLATION, always consult your local Milliken sales representative or Milliken Technical Services (1-800-528-8453 Option 3)if you have questions or concerns about the correct installation method.Due to the nature and construction of solution-dyed nylon(SDN), we are able to provide very unique, tufted design patterns.  From time to 
time during installation, these products may require that tiles be shifted within the layout in order to avoid a dark line in one tile being positioned next to a dark line in another tile. The dark seam is not a carpet manufacturing defect and can be avoided by attention during the installation phase.SDNand multitile patternproducts requireadditional shuffling during installation.    Tiles must be mixed up when pulling off the pallet to assure randomization on the floor when installing.    Should repeating design elements be observed during installation, the repetitive tiles should be shifted or replaced with other tiles to alleviate the repetitive visual that may occur.   FLOOR PREPARATION: NOTE: The following are guidelines. The Flooring Contractor has responsibility to assure compliance. Financial responsibility for bringing any floor into conformance with these guidelines must 
be determined prior to beginning work.
• Floor preparation in accordance with ASTM F710(current version)unless specifically allowed per this document.
• All topical membrane forming concrete curing compoundsmust be removed prior to application of adhesive.
• Concrete subfloorsmust be structurally sound, clean, dust free, smooth,trowel finish (not burnished) and level. Cracks and holes in excess of 1/8" 
(3.2mm) should be filled with a Portland Cementbased floor patching material such as W.W. Henry 547 Unipro™, DAP “Webcrete 98”, Maipei “PlaniPatch”, 
Ardex “Featherfinish” or similar. Gypsum based compounds are not recommended.
typically eliminates the necessity of old adhesive removal.   See adhesive Technical Data Sheet for specifics.  All Milliken Modular carpets carry the “Lifetime Floor Compatibility” warranty. Milliken is not responsible for subfloor conditions.The installer


Enter your question (or type 'exit' to quit): exit
INFO - 🔴 Sistem durduruldu. Programdan çıkılıyor...
Goodbye!

### 3 

PS C:\Users\YavuzCan\Desktop\rag_project_(2)> & C:/Users/YavuzCan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/YavuzCan/Desktop/rag_project_(2)/src/main.py"
2025-03-22 16:57:09,068 - INFO - Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.
2025-03-22 16:57:09,308 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-03-22 16:57:11,955 - INFO - 🔹 Hugging Face giriş başarılı: JBown123
2025-03-22 16:57:11,955 - INFO - 📥 meta-llama/Llama-2-7b-chat-hf modeli yükleniyor...

Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00, 12.45it/s] 
2025-03-22 16:57:12,893 - WARNING - Some parameters are on the meta device because they were offloaded to the cpu and disk.
2025-03-22 16:57:12,894 - INFO - ✅ Model başarıyla yüklendi!

Enter your question (or type 'exit' to quit): What are the recommended maintenance procedures for Lapidus Core?
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  8.76it/s] 

2025-03-22 16:57:36,874 - INFO - 🔍 Sonuç skoru: 1.4676 - Kaynak: 220041_Lapidus-Core-Maintenance-Procedures.pdf
2025-03-22 16:57:36,874 - INFO - 🔍 Sonuç skoru: 1.5916 - Kaynak: 220041_Lapidus-Core-Warranty.pdf
2025-03-22 16:57:36,875 - INFO - 🔍 Sonuç skoru: 1.6559 - Kaynak: 220041_Lapidus-Core-Installation-Instructions.pdf
2025-03-22 16:57:36,875 - INFO - 📝 Prompt işleniyor: Question: What are the recommended maintenance procedures for Lapidus Core?
Context: Milliken Recomm...
2025-03-22 17:19:47,182 - INFO - ✅ Yanıt oluşturuldu!

Response:
 Question: What are the recommended maintenance procedures for Lapidus Core?
Context: Milliken Recommended Carpet Maintenance Procedures

!!
Consistent, thorough cleaning is required to remove soil that has
bonded to carpet fibers.  To ensure optimum performance and
appearance, Milliken recommends using the MilliCare Dry Carpet
Cleaning system. 
 
MilliCare Textile and Carpet Care® is Green Seal Certified and an IICRC Certified training provider. 
The proprietary dry care system is CRI Certified as a Deep Cleaning Methodology and can contribute   
to LEED points. To find a MilliCare service provider in your area, please visit www.millicare.com.   
!!
Prevention Procedures
!
Barrier Mats - Barrier mats should be placed at all entrance ways into the facility and at locations
were there is a transition from hard surface flooring onto the carpet if possible. This will help
prevent soil from being tracked onto the carpet, improving its appearance and extending its life.
Barrier mats should be vacuumed daily and cleaned or replaced frequently depending on the weather
and use.


Vacuuming - Proper vacuuming is one of the most important parts of a total preventive
maintenance program.  Ineffective equipment or procedures will accelerate the appearance loss of
the carpet by allowing dirt and grit to penetrate the pile surface. The accumulation of this soil,
especially the smaller respirable particulates, can lead to Indoor Air Quality problems.
!
The janitorial / housekeeping staff is typically assigned the task of scheduled vacuuming.  Vacuuming
frequencies should be determined by four factors:
!
1. Type of carpet installed and appearance expectations.
2. Type and quality of vacuum used.
3. Expected traffic for each area of the facility.
4. Soiling environment of each area of the facility.
!
A commercial upright vacuum with a beater brush is recommended for vacuuming all carpet. Regular
maintenance of vacuums is also essential.  Vacuums should be emptied and inspected after every
use.   Particular attention should be paid to the condition of the brushes. Also, make sure that there
is no material obstructing the air-flow channel.
!
Typical vacuuming frequencies are as follows:
!!
High traffic:  Every full work day.  All entrances, exits, lobbies, food service areas, main corridors,
elevators, funnel and pivot points.  The vacuum should make a minimum of three
passes in all high traffic areas.
!!
Medium traffic: Every other work day.  All secondary corridors, conference rooms, private offices.
!


Low traffic: Once a week. Minimal use corridors, rarely used conference rooms and training rooms.
!!
"1

Milliken Recommended Carpet Maintenance Procedures (Cont.)
!
Spot Cleaning - Spots and stains are one of the biggest detriments to high appearance levels. In
order to maintain a consistent appearance level between periodic maintenance, it's critical that
spots and stains be removed on a daily basis.  In most cases, daily spotting is the responsibility of the
janitorial or housekeeping staff. Milliken recommends the use of a Capture® Spot Kit or MilliCare®
Spot Kit for treating most spots, following these procedures:
1. Remove as much excess material as possible prior to spot removal. Blot up liquids with a
clean white terry cloth, vacuum up soil and gently scrap up encrusted material.
2. Spray Capture Pre-mist onto a clean, white terry towel and work in gently. Do not scrub.
Blot, absorbing as much of the spot into the towel as possible. Work from the outside edge
of the spot into the center to prevent spreading.
3. Apply Capture dry carpet cleaner to the spot. Gently agitate with a brush, wait 30 mins.
And vacuum.
!
Note: Milliken does not recommend using any spotting agents containing solvents as they can leave
residue that contributes to resoiling and can possibly damage the carpet.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
millicare.com
1300 Brownwood Avenue ・ LaGrange, Georgia 30240 ・ 1.888.886.2273 (1.888.88.MCARE)
MilliCare® is a registered tr
Answer: Milliken recommends the following maintenance procedures for Lapidus Core carpet:

1. Vacuuming: Vacuum the carpet regularly, based on traffic levels and carpet type. Use a commercial upright vacuum with a beater brush for all carpet.
2. Barrier mats: Place barrier mats at entrances and areas where there are transitions from hard surfaces to carpet. Vacuum and clean or replace these mats frequently.
3. Spot cleaning: Remove spots and stains daily using a Capture® Spot Kit or MilliCare® Spot Kit. Do not use spotting agents containing solvents as they can damage the carpet.
4. Prevention procedures: Prevent soil from being tracked onto the carpet by using barrier mats and ensuring that entrances and exits are clean.  


Enter your question (or type 'exit' to quit): exit
2025-03-22 17:20:55,350 - INFO - 🔴 Sistem durduruldu. Programdan çıkılıyor...
Goodbye!


### 4

PS C:\Users\YavuzCan\Desktop\rag_project_(2)> & C:/Users/YavuzCan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/YavuzCan/Desktop/rag_project_(2)/src/main.py"
2025-03-22 18:15:23,539 - INFO - Use pytorch device_name: cpu
2025-03-22 18:15:23,540 - INFO - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-03-22 18:15:26,937 - INFO - 📥 meta-llama/Llama-2-7b-chat-hf modeli yükleniyor...
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:17<00:00,  8.55s/it] 
2025-03-22 18:15:45,213 - WARNING - Some parameters are on the meta device because they were offloaded to the disk and cpu.
2025-03-22 18:15:45,216 - INFO - ✅ Model başarıyla yüklendi!
2025-03-22 18:15:45,217 - INFO - 🟢 Sistem başlatıldı. Kullanıcı sorguları bekleniyor...

Enter your question (or type 'exit' to quit): How long does the warranty for Lapidus Core last?
2025-03-22 18:18:00,072 - INFO - 🔍 Sorgu alındı: How long does the warranty for Lapidus Core last?
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  5.45it/s]
2025-03-22 18:18:00,457 - INFO - 🔍 Sonuç skoru: 1.3581 - Kaynak: 220041_Lapidus-Core-Warranty.pdf
2025-03-22 18:18:00,457 - INFO - 🔍 Sonuç skoru: 1.8517 - Kaynak: 220041_Lapidus-Core-Installation-Instructions.pdf
2025-03-22 18:18:00,458 - INFO - 🔍 Sonuç skoru: 1.8833 - Kaynak: 220041_Lapidus-Core-Maintenance-Procedures.pdf

Response:
 Question: Question: How long does the warranty for Lapidus Core last?
Context:

Date: 06/01/21

Supersedes: 10/14/19

Milliken Commercial Modular Carpet Warranties
These warranties are subject to the Warranty Terms and Conditions provided at the end of this document and
apply only to commercial modular carpet products sold by Milliken. Details about the test methods supporting
these warranties are available upon request.



WARRANTIES APPLICABLE TO ALL MILLIKEN COMMERCIAL MODULAR PRODUCTS:
(See additional warranties under Specialty Product Limited Warranties below.)


FACE FIBER WEAR
Milliken warrants that the carpet will lose no more than ten percent (10%) of its face fiber by weight during the
Lifetime of the carpet. If the carpet is installed on stairs, this warranty will be limited to five years. A claim against
this warranty requires the submittal of a sample (one square yard minimum) of unused attic stock and a like-size
piece of carpet from the area that is believed to be worn beyond the terms of this warranty. These samples will
be submitted to an independent testing lab for verification.

STAINING/SOILING RESISTANCE (StainSmart®)
StainSmart provides lifetime resistance for your carpet against penetrating stains and soil.

COLOR PATTERN PERMANENCY
Milliken warrants that the carpet will exhibit no pattern loss during the Lifetime of the carpet. If the carpet is
installed on stairs this warranty will be limited to five years.


DELAMINATION OF BACKING
Milliken warrants that the backing of the carpet will not delaminate during the Lifetime of the carpet.

EDGE RAVEL
Milliken warrants that the carpet will exhibit no edge ravel or “zippering” during the Lifetime of the carpet.

TUFT BIND
Milliken warrants that the carpet will maintain its tuft bind integrity during the Lifetime of the carpet.
.
FLOOR COMPATIBILITY
Milliken warrants that the carpet will not cause a reactivation of old adhesives due to plasticizer migration during
the Lifetime of the carpet.

ANTISTATIC
Milliken warrants that the carpet will not generate static shock greater than 3.5 kilovolts during the Lifetime of
the carpet.

FLAMMABILITY

Milliken warrants that at the time of shipment the carpet will comply with the applicable provisions of the
Federal Flammable Fabrics Act for carpet used as floor covering in commercial installations. Milliken does not
represent that this or any other carpet fabric will not burn or generate smoke under actual fire conditions.

CUSHION RESILIENCY
Milliken warrants that the modular carpet with WellBAC™ cushion will retain 90% of its cushion resilience
during the Lifetime of the modular carpet.

DIMENSIONAL STABILITY
Milliken warrants that the modular carpet will maintain its dimensional stability during the Lifetime of the
modular carpet.

FLOOR RELEASE
Milliken warrants that the initial installation of the modular carpet will release from the floor during the Lifetime
of the modular carpet.

TOP DOWN MOISTURE RESISTANCE
Milliken warrants that the modular carpet will resist moisture penetration during the Lifetime of the modular
carpet. This warranty does not include moisture penetration at the seams of modular carpet.

SITE RELATED SOLUTIONS
Additional warranties may apply when Milliken Non-Reactive Standard or Milliken Mosaic Moisture XT
Adhesive is used with Milliken Modular Carpet Tile. Click on one of the links below to learn more:

Milliken Non-Reactive Standard Adhesive – Warranty

Milliken Mosaic Moisture XT Spray Adhesive - Warranty


SPECIALTY PRODUCT LIMITED WARRANTIES:

TRACTIONBACK® MODULAR CARPET
Milliken warrants that at the time of shipment, modular carpet with TractionBack will maintain sufficient bond
strength to hold the modular carpet in place under normal foot traffic use for ten (10) years.

ENTRY BARRIER CARPET (OBEX® TILE)
Milliken warrants that the OBEX Tile entry barrier carpet will lose no more than ten percent (10%) of its face

The warranty for Lapidus Core lasts for the lifetime of the carpet.

Reason:
The warranty for Lapidus Core is specified as "Lifetime of the carpet" in the provided




