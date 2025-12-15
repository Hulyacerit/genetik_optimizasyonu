
import numpy as np
import matplotlib.pyplot as plt
from genetik_operators import (
    hesapla_kalite, uygunluk_hesapla,
    rulet_secimi, mutasyon_uygula, caprazlama
)

def evrimsel_algoritma(populasyon_boyutu, nesil_sayisi, mutasyon_ihtimali):

    # 1. Başlangıç: 0-100 arası rastgele Pigment A oranları
    populasyon = np.random.uniform(0, 100, populasyon_boyutu)

    gecmis_skorlar = []
    gecmis_x1 = []

    print(f"{'NESİL':<10} | {'KALİTE (y)':<15} | {'PIGMENT A':<15} | {'PIGMENT B':<15}")
    print("-" * 65)

    for nesil in range(nesil_sayisi):
        # Herkesin puanını hesapla
        uygunluklar = np.array([uygunluk_hesapla(x) for x in populasyon])

        # En iyiyi bul (Elitizm)
        en_iyi_idx = np.argmax(uygunluklar)
        elit_birey = populasyon[en_iyi_idx]
        elit_skor = uygunluklar[en_iyi_idx]

        # Kayıt tut
        gecmis_skorlar.append(elit_skor)
        gecmis_x1.append(elit_birey)

        # Ekrana yazdır
        puan, x2 = hesapla_kalite(elit_birey)
        print(f"{nesil+1:<10} | {puan:.2f}           | %{elit_birey:.2f}          | %{x2:.2f}")

        # YENİ NESİL
        yeni_populasyon = [elit_birey] # En iyiyi koru

        while len(yeni_populasyon) < populasyon_boyutu:
            # Seçim
            p1, p2 = rulet_secimi(populasyon, uygunluklar)
            # Çaprazlama
            c1, c2 = caprazlama(p1, p2)
            # Mutasyon
            c1 = mutasyon_uygula(c1, mutasyon_ihtimali)
            c2 = mutasyon_uygula(c2, mutasyon_ihtimali)

            yeni_populasyon.extend([c1, c2])

        populasyon = np.array(yeni_populasyon[:populasyon_boyutu])

    # --- GRAFİKLERİ ÇİZ VE KAYDET ---
    plt.figure(figsize=(10, 5))

    # Grafik 1: Kalite
    plt.subplot(1, 2, 1)
    plt.plot(gecmis_skorlar, color='green', marker='o')
    plt.title("Kalite Puanı Artışı")
    plt.xlabel("Nesil")
    plt.ylabel("Puan")
    plt.grid(True)

    # Grafik 2: Oranlar
    plt.subplot(1, 2, 2)
    plt.plot(gecmis_x1, label='Pigment A', color='blue')
    plt.plot(100 - np.array(gecmis_x1), label='Pigment B', color='red')
    plt.title("Pigment Oranlarının Dengelenmesi")
    plt.xlabel("Nesil")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("sonuc_grafigi.png") # Resmi de kaydet
    plt.show()
