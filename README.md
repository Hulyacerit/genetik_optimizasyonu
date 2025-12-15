# 🎨 Endüstriyel Boya Karışımı Optimizasyonu

**Ders:** Yapay Zeka Sistemleri
**Konu:** Genetik Algoritma (GA) ile Kısıtlı Optimizasyon Problemi Çözümü

---

## 👤 Öğrenci Bilgileri

| Ad Soyad | Numara | Bölüm |
|---|---|---|
| **Hülya Cerit** | **2312721012** | Bilgisayar Mühendisliği |

---

## 📌 Proje Tanımı ve Senaryo

Bu proje, endüstriyel bir boya fabrikasında ideal renk tonunu yakalamak için **Pigment A** ve **Pigment B** oranlarının optimize edilmesini amaçlar. 

Geleneksel deneme-yanılma yöntemleri yerine, doğadaki evrim sürecini taklit eden **Genetik Algoritma** kullanılarak, belirlenen kısıtlar altında en yüksek kalite puanını veren karışım oranı aranmaktadır.

---

## 🧮 Matematiksel Model

Proje aşağıdaki matematiksel problemi çözmektedir:

### 1. Değişkenler
Karışım toplamı %100 olmak zorundadır.
- **$x_1$**: Pigment A Oranı (%)
- **$x_2$**: Pigment B Oranı (%)
- **Bağıntı:** $x_2 = 100 - x_1$

### 2. Amaç Fonksiyonu (Fitness Function)
Renk kalitesi (y) şu formülle hesaplanır ve **maksimize** edilmeye çalışılır:

$$y = 5x_1 + 2x_2 - (x_1 \cdot x_2)$$

### 3. Kısıtlar (Constraints)
Üretim standartları gereği aşağıdaki kısıtlara uyulması zorunludur:
- **Minimum Kullanım:** $x_1 \ge 30$ (A pigmenti en az %30 olmalı).
- **Fiziksel Sınır:** $0 \le x_1 \le 100$.

> **Ceza Mekanizması:** Algoritma, $x_1 < 30$ olan veya sınırları aşan bireylere **5000 puanlık ceza (penalty)** uygulayarak onları evrim sürecinden eler.

---

## 🧬 Algoritma Mimarisi

Bu projede **Modüler Programlama** yapısı kullanılmıştır. Algoritma şu adımları izler:

1.  **Başlangıç Popülasyonu:** 0-100 arasında rastgele $x_1$ değerlerinden oluşan 20 birey üretilir.
2.  **Uygunluk Hesabı:** Her bireyin kalite puanı hesaplanır. Kısıt ihlali varsa puan düşürülür.
3.  **Elitizm:** En iyi birey bozulmadan doğrudan bir sonraki nesle aktarılır.
4.  **Seçim (Rulet Tekerleği):** Uygunluğu yüksek bireylerin ebeveyn olarak seçilme şansı artırılır.
5.  **Çaprazlama (Aritmetik):** İki ebeveynin genleri sayısal ortalama yöntemiyle birleştirilir.
6.  **Mutasyon:** Yerel tuzaklardan (Local Optima) kurtulmak için genlerde %20 ihtimalle rastgele değişimler yapılır.

---

## 📁 Proje Dosya Yapısı

Proje dosyaları görevlerine göre ayrılmıştır:

| Dosya Adı | Görevi ve İçeriği |
|---|---|
| `main.py` | **Başlatıcı:** Parametreleri ayarlar (Popülasyon=20, Nesil=100 vb.) ve simülasyonu başlatır. |
| `evrim_motoru.py` | **Simülasyon Çekirdeği:** Nesiller arası döngüyü kurar, elitizmi uygular ve sonuç grafiklerini çizer. |
| `genetik_operators.py` | **Matematik Kütüphanesi:** Fitness hesaplama, seçim, çaprazlama ve mutasyon fonksiyonlarını barındırır. |
| `sonuc_grafigi.png` | **Çıktı:** Program çalıştığında üretilen başarı ve değişim grafiği. |

---

## 🚀 Kurulum ve Çalıştırma

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1.  Gerekli kütüphanelerin yüklü olduğundan emin olun:
    ```bash
    pip install numpy matplotlib
    ```

2.  Ana dosyayı çalıştırın:
    ```bash
    python main.py
    ```

---

## 📊 Sonuçlar

Program çalıştığında konsolda her nesil için **En İyi Kalite Puanı** ve **Karışım Oranlarını** listeler. Ayrıca işlemin sonunda iki adet grafik üretir:
* **Grafik 1:** Kalite puanının nesiller boyunca artışı (Yakınsama).
* **Grafik 2:** Pigment A ve B oranlarının optimum noktaya yerleşmesi.

---
*Bu proje Python dili ve NumPy/Matplotlib kütüphaneleri kullanılarak geliştirilmiştir.*
