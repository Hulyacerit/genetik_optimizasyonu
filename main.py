
from evrim_motoru import evrimsel_algoritma

print(" BOYA KARIŞIMI OPTİMİZASYONU BAŞLATILIYOR...")
print("Senaryo: y = 5x1 + 2x2 - x1x2 (Maksimum Kalite)")
print("Kısıt: Pigment A (x1) >= 30\n")

if __name__ == "__main__":
    # 20 Birey, 20 Nesil, %20 Mutasyon Şansı
    evrimsel_algoritma(populasyon_boyutu=20, nesil_sayisi=20, mutasyon_ihtimali=0.2)
