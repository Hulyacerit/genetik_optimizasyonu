
import numpy as np
import random

def hesapla_kalite(x1):
    """
    Amaç Fonksiyonu: y = 5x1 + 2x2 - x1*x2
    x2 = 100 - x1 (Toplam %100 olmalı)
    """
    x2 = 100 - x1
    y = (5 * x1) + (2 * x2) - (x1 * x2)
    return y, x2

def uygunluk_hesapla(x1):
    """
    Genetik algoritma puanı (Fitness).
    Kısıt: x1 >= 30 olmalı.
    """
    kalite_puani, x2 = hesapla_kalite(x1)

    ceza = 0
    # KISIT KONTROLÜ
    if x1 < 30:
        ceza = 5000 # 30'un altındaysa puanı öldür (Elensin diye)
    if x1 > 100 or x1 < 0:
        ceza = 5000 # Mantıksız değerler için ceza

    return kalite_puani - ceza

def rulet_secimi(populasyon, uygunluklar):
    # Negatif puanları pozitife çevir (Rulet mantığı için şart)
    min_val = min(uygunluklar)
    if min_val < 0:
        pozitif = uygunluklar - min_val + 1
    else:
        pozitif = uygunluklar + 1e-6

    prob = pozitif / sum(pozitif)
    secilenler = np.random.choice(len(populasyon), size=2, p=prob)
    return populasyon[secilenler[0]], populasyon[secilenler[1]]

def mutasyon_uygula(x1, ihtimal, buyukluk=5.0):
    """
    Pigment A oranını %5 civarında rastgele oynatır.
    """
    if random.random() < ihtimal:
        degisim = random.uniform(-buyukluk, buyukluk)
        x1 += degisim
        x1 = max(0, min(100, x1)) # 0-100 arasında tut
    return x1

def caprazlama(p1, p2):
    """
    İki oranın ortalamasını alarak çocuk üretir.
    """
    c1 = (p1 + p2) / 2
    c2 = (p1 * 0.7) + (p2 * 0.3)
    return c1, c2
