# genetik_optimizasyonu
Kısıtlı Optimizasyon Problemi: Endüstriyel Boya Karışımı (Genetik Algoritma)
Bu proje, Genetik Algoritma (GA) kullanarak endüstriyel boya karışımında ideal renk kalitesini yakalamayı amaçlayan kısıtlı bir optimizasyon probleminin çözümünü sunmaktadır.

Problem Tanımı: Fabrika, Pigment A (x1) ve Pigment B (x2) oranlarını optimize ederek Renk Kalitesi Puanı'nı maksimize etmeyi hedeflemektedir.

Amaç Fonksiyonu: Algoritmanın maksimize etmeye çalıştığı puan (y); y=5x1 + 2x2 - x1.x2
Değişkenler: x1: Pigment A oranı (%) [0,100]
             x2: Pigment B oranı (%) [0,100]
Kısıtlar: x1 + x2 = 100 : karışım toplamı %100 olmalıdır.
        : x1 >= 30 : Pigment A en az %30 oranında kullanılmalıdır.
        
Genetik Algoritma Tasarımı
Proje, kısıtlı bir alanda arama yapmak üzere tasarlanmıştır.

Kromozom Temsili
Temsil: Her birey, iki kayan nokta sayısından oluşan bir dizidir: [x1, x2]
Adaptasyon: Ödev gereği x1 ve x2 ayrı genler olarak tutulmuştur. Bu durum, operatörler sonrasında Kısıt 1'in (x1 + x2 =100) bozulmasına yol açar. Bu bozulma, uygunluk fonksiyonundaki Ceza Yöntemi ile yönetilmiştir.

Uygunluk (Fitness) Fonksiyonu
Uygunluk puanı, amaç fonksiyonu değerinden kısıt ihlali cezalarının çıkarılmasıyla hesaplanır. Amaç uygunluğu maksimize etmektir.
Fitness = (5x1 + 2x2 - x1.x2)-(İhlal Sayısı x 10)
  Ceza Yöntemi (Penalty Function): İhlal edilen her kısıt için (özellikle x1 + x2 = 100 kısıtını sağlayamayan bireyler için) uygunluktan sabit bir puan (10) düşülür.

Operatörler
Operatör                  Kullanım,               Önemi
Başlangıç Popülasyonu     Akıllı Başlangıç        İlk popülasyon, x1​≥30 ve x1​+x2​=100                                                               kısıtlarını sağlayacak şekilde oluşturularak                                                     algoritmanın hızlı başlaması sağlanmıştır.

Seçim                     Rulet Tekerleği         Popülasyon çeşitliliğini korumak ve en iyi                               veya Rank Temelli       bireylere yüksek seçilme şansı vermek için                               Seçim                   kullanılır. Negatif uygunluk değerleri, seçime                                                   uygun hale getirilmiştir.
                              
Çaprazlama                Tek Noktalı Çaprazlama  İki ebeveynin genetik materyali tek bir                                                          noktadan kesilip karıştırılır. (Bu operatör,                                                     iki genli yapı nedeniyle kısıt ihlali yaratır                                                    ve bu ihlaller ceza ile yönetilir.)

Mutasyon                  Rastgele Değişim        Belirli bir ihtimalle (MUTASYON_IHTIMALI)                                                        genlere rastgele bir kayan nokta değişimi                                                        ekleyerek çözüm uzayının keşfedilmesini                                                          sağlar. Sonuçlar 0 ile 100 arasında                                                              kliplenmiştir.

Sonuçlar (Global Optimum)
Genetik Algoritma, belirlenen kısıtlar altında en yüksek renk kalitesi puanını başarıyla bulmuştur.

Optimal Çözüm
Algoritmanın ulaştığı en yüksek y değeri, x1=100 ve x2=0 noktasıdır:
Pigment A (x1): %100.00 
Pigment B (x2): %0.00 
Amaç Fonksiyonu (y): 500.00
Kısıt İhlali: 0 (Sıfır)

Yakınsama HızıFitness grafiğinde görüldüğü gibi, algoritma başlangıçtaki iyi bir çözümden başlayarak, 35. nesilden önce global optimum değer olan Fitness = 500.0'a ulaşmış ve bu değeri korumuştur. Bu, algoritmanın yüksek bir yakınsama hızına sahip olduğunu gösterir .

Kullanım
GitHub'dan projeyi klonlayın veya .ipynb dosyasını Colab'da açın.
Parametreleri ayarlayın (Mutasyon ihtimali, Nesil sayısı vb.).
Dosyayı çalıştırın ve çıktıyı gözlemleyin.
