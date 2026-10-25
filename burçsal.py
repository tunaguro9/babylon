while True:
    try:
        gun = int(input("Doğum gününüzü giriniz: "))
        ay = int(input("Doğduğunuz ayı giriniz (sayısal olarak): "))
        yil = int(input("Doğduğunuz yılı giriniz: "))
        kalan = yil % 12

        if yil == 0:
            print("İsa mısın sen?\n")
            continue
        elif yil < 0:
            print("Milattan önce mi doğdun?\n")
            continue

        if ay < 1 or ay > 12:
            print("Ay 1 ile 12 arasında olmalıdır.\n")
            continue

        if ay == 2:
            if yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0):
                maksimum_gun = 29
            else:
                maksimum_gun = 28
        elif ay == 4 or ay == 6 or ay == 9 or ay == 11:
            maksimum_gun = 30
        else:
            maksimum_gun = 31

        if gun < 1 or gun > maksimum_gun:
            print("Bu ay için gün, 1 ile", maksimum_gun, "arasında olmalıdır.\n")
            continue

        break

    except ValueError:
        print("Lütfen yalnızca tam sayı giriniz.\n")

print("\n")

if (ay == 12 and gun >= 22) or (ay == 1 and gun <= 19):
    print("Burcunuz Oğlak,\nKararlılığınız ve sorumluluk duygunuzla hedeflerinize ilerler, dinlenmeye ve duygularınıza yer açmayı öğrenirsiniz.")
elif (ay == 1 and gun >= 20) or (ay == 2 and gun <= 18):
    print("Burcunuz Kova,\nÖzgün fikirleriniz ve bağımsızlığınızla yeniliklere yönelir, farklılığınızı korurken yakınlık kurmayı öğrenirsiniz.")
elif (ay == 2 and gun >= 19) or (ay == 3 and gun <= 20):
    print("Burcunuz Balık,\nHayal gücünüz ve empatinizin rehberliğinde derin bağlar kurar, başkalarını hissederken kendinizi korumayı öğrenirsiniz.")
elif (ay == 3 and gun >= 21) or (ay == 4 and gun <= 19):
    print("Burcunuz Koç,\nCesaretiniz ve girişkenliğinizle harekete geçer, sabrı ve başladığınızı sürdürmeyi öğrenirsiniz.")
elif (ay == 4 and gun >= 20) or (ay == 5 and gun <= 20):
    print("Burcunuz Boğa,\nGüven ve huzur ararken sağlam bağlar kurar, değişime alan açmayı öğrenirsiniz.")
elif (ay == 5 and gun >= 21) or (ay == 6 and gun <= 20):
    print("Burcunuz İkizler,\nMerakınız ve iletişim gücünüzle farklı dünyaları keşfeder, odağınızı korumayı öğrenirsiniz.")
elif (ay == 6 and gun >= 21 ) or (ay == 7 and gun <= 22):
    print("Burcunuz Yengeç,\nDuygularınız ve aidiyet ihtiyacınızla derin bağlar kurar, kendi sınırlarınızı gözetmeyi öğrenirsiniz.")
elif (ay == 7 and gun >= 23 ) or (ay == 8 and gun <= 22):
    print("Burcunuz Aslan,\nYaratıcılığınız ve sıcaklığınızla kendinizi ifade eder, değerinizi kendi içinizde bulmayı öğrenirsiniz.")
elif (ay == 8 and gun >= 23 ) or (ay == 9 and gun <= 22):
    print("Burcunuz Başak,\nDikkatiniz ve çözüm üretme becerinizle hayatı iyileştirir, kusurlara da yer açmayı öğrenirsiniz.")
elif (ay == 9 and gun >= 23 ) or (ay == 10 and gun <= 22):
    print("Burcunuz Terazi,\nUyum ve adalet arayışınızla ilişkiler kurar, kendi isteklerinizi açıkça dile getirmeyi öğrenirsiniz.")
elif (ay == 10 and gun >= 23 ) or (ay == 11 and gun <= 21):
    print("Burcunuz Akrep,\nDerinliğiniz ve tutkunuzla yaşadıklarınızın özüne iner, güvenmeyi ve kontrolü gevşetmeyi öğrenirsiniz.")
else:
    print("Burcunuz Yay,\nÖzgürlük ve anlam arayışınızla ufkunuzu genişletir, keşfettiklerinizi hayatınıza taşımayı öğrenirsiniz.")

print("\n")

if kalan == 0:
    print("Çin burcunuz Maymun,\nKıvrak zekânız ve mizahınızla çözümler bulur, yeteneklerinizi tek bir hedefte derinleştirmeyi öğrenirsiniz.")
elif kalan == 1:
    print("Çin burcunuz Horoz,\nDikkatiniz ve açık sözlülüğünüzle düzen kurar, eleştirinizi anlayışla dengelemeyi öğrenirsiniz.")
elif kalan == 2:
    print("Çin burcunuz Köpek,\nSadakatiniz ve adalet duygunuzla sevdiklerinizi korur, kendi huzurunuzu da gözetmeyi öğrenirsiniz.")
elif kalan == 3:
    print("Çin burcunuz Domuz,\nCömertliğiniz ve içtenliğinizle hayatın tadını çıkarır, verirken sınırlarınızı korumayı öğrenirsiniz.")
elif kalan == 4:
    print("Çin burcunuz Fare,\nZekânız ve pratikliğinizle fırsatları fark eder, her şeyi hesaplamadan da güvenmeyi öğrenirsiniz.")
elif kalan == 5:
    print("Çin burcunuz Öküz,\nSabrın ve çalışkanlığınla sağlam bir hayat kurar, gerektiğinde esnemeyi öğrenirsin.")
elif kalan == 6:
    print("Çin burcunuz Kaplan,\nCesaretiniz ve bağımsızlığınızla kendi yolunuzu açar, gücünüzü sabırla yönlendirmeyi öğrenirsiniz.")
elif kalan == 7:
    print("Çin burcunuz Tavşan,\nNezaketiniz ve duyarlılığınızla huzur yaratır, ihtiyaçlarınızı açıkça savunmayı öğrenirsiniz.")
elif kalan == 8:
    print("Çin burcunuz Ejderha,\nBüyük hayalleriniz ve etkileyici enerjinizle ilham verir, başkalarına da alan açmayı öğrenirsiniz.")
elif kalan == 9:
    print("Çin burcunuz Yılan,\nSezgileriniz ve derin düşüncenizle olayların özünü kavrar, güvenip kendinizi paylaşmayı öğrenirsiniz.")
elif kalan == 10:
    print("Çin burcunuz At,\nÖzgürlüğünüz ve hareketli ruhunuzla yeni deneyimlere koşar, bağlılık içinde de özgür kalmayı öğrenirsiniz.")
else:
    print("Çin burcunuz Keçi,\nYaratıcılığınız ve şefkatinizle güzellik üretir, kendi gücünüze dayanmayı öğrenirsiniz.")

tarih = str(gun) + str(ay) + str(yil)
toplam = 0

for rakam in tarih:
    toplam += int(rakam)

while toplam > 21:
    yeni_toplam = 0

    for rakam in str(toplam):
        yeni_toplam += int(rakam)

    toplam = yeni_toplam

print("\nTarot sayınız:", toplam,)

if toplam == 1:
    print("Tarot kartınız: Büyücü, \nFikirlerinizi gerçeğe dönüştürme gücünüz, yaratıcılığınız ve girişkenliğiniz öne çıkar.")
elif toplam == 2:
    print("Tarot kartınız: Başrahibe,\nSezgileriniz, iç dünyanız ve görünenden fazlasını anlama yeteneğiniz size yol gösterir.")
elif toplam == 3:
    print("Tarot kartınız: İmparatoriçe,\nÜretmek, güzellik yaratmak ve sevgiyle büyütmek temel temalarınızdır.")
elif toplam == 4:
    print("Tarot kartınız: İmparator,\nDüzen kurmak, sorumluluk almak ve sağlam temeller oluşturmak sizin alanınızdır.")
elif toplam == 5:
    print("Tarot kartınız: Aziz,\nDeğerlerinizi keşfetmek, öğrenmek ve bilginizi başkalarıyla paylaşmak hayatınızda önem taşır.")
elif toplam == 6:
    print("Tarot kartınız: Âşıklar, \nİlişkiler ve seçimler aracılığıyla kendinize sadık kalmayı öğrenirsiniz.")
elif toplam == 7:
    print("Tarot kartınız: Savaş Arabası,\nKararlılığınızla yönünüzü belirler, zıt güçleri ortak bir hedefe taşırsınız.")
elif toplam == 8:
    print("Tarot kartınız: Güç,\nGerçek gücünüzü sabırdan, şefkatten ve duygularınızı yönetebilmekten alırsınız.")
elif toplam == 9:
    print("Tarot kartınız: Ermiş,\nKendinizi tanımak için içe döner, deneyimlerinizden başkalarına da ışık tutan bir bilgelik çıkarırsınız.")
elif toplam == 10:
    print("Tarot kartınız: Kader Çarkı,\nDeğişen koşullara uyum sağlamak ve hayatın döngülerindeki fırsatları görmek ana temanızdır.")
elif toplam == 11:
    print("Tarot kartınız: Adalet,\nDengeyi, dürüstlüğü ve seçimlerinizin sorumluluğunu üstlenmeyi önemsersiniz.")
elif toplam == 12:
    print("Tarot kartınız: Asılan Adam,\nKontrolü gevşetip farklı bir açıdan baktığınızda yeni anlamlar bulursunuz.")
elif toplam == 13:
    print("Tarot kartınız: Ölüm,\nBiteni geride bırakıp dönüşüme alan açmak, hayatınızdaki temel gelişim temasıdır.")
elif toplam == 14:
    print("Tarot kartınız: Denge,\nFarklı ihtiyaçları uyum içinde birleştirerek sabrı ve ölçülülüğü öğrenirsiniz.")
elif toplam == 15:
    print("Tarot kartınız: Şeytan,\nSizi kısıtlayan bağları ve arzuları fark ederek özgürlüğünüzü yeniden kazanmayı öğrenirsiniz.")
elif toplam == 16:
    print("Tarot kartınız: Kule,\nSarsılan kalıpların ardından daha dürüst ve sağlam bir yaşam kurmaya yönelirsiniz.")
elif toplam == 17:
    print("Tarot kartınız: Yıldız,\nUmudu, ilhamı ve kendiniz olarak başkalarına ışık olmayı temsil edersiniz.")
elif toplam == 18:
    print("Tarot kartınız: Ay,\nGüçlü hayal dünyanız içinde sezgilerinizle korkularınızı birbirinden ayırmayı öğrenirsiniz.")
elif toplam == 19:
    print("Tarot kartınız: Güneş,\nNeşeniz, açıklığınız ve yaratıcı enerjinizle kendinizi görünür kılmaya yönelirsiniz.")
elif toplam == 20:
    print("Tarot kartınız: Mahkeme,\nGeçmişinizi değerlendirerek içinizdeki çağrıya kulak verir ve kendinizi yenilersiniz.")
elif toplam == 21:
    print("Tarot kartınız: Dünya,\nDeneyimlerinizi bütünleştirmek, tamamlanmayı yaşamak ve dünyayla bağ kurmak temel temanızdır.")

if toplam >= 10:
    ikinci = toplam // 10 + toplam % 10

    while ikinci >= 10:
        ikinci = ikinci // 10 + ikinci % 10

    if ikinci == 1:
        print("İkincil tarot kartınız: Büyücü,\nİçinizdeki girişim gücü, ihtiyaç duyduğunuzda yeteneklerinizi kullanmanıza ve ilk adımı atmanıza yardımcı olur.")
    elif ikinci == 2:
        print("İkincil tarot kartınız: Başrahibe,\nİç sesiniz, kararsız kaldığınız anlarda durup hislerinizi dinleyerek yönünüzü bulmanızı destekler.")
    elif ikinci == 3:
        print("İkincil tarot kartınız: İmparatoriçe,\nİçinizdeki yaratıcı ve şefkatli yön, kendinizi beslemenize ve emek verdiğiniz şeyleri büyütmenize yardımcı olur.")
    elif ikinci == 4:
        print("İkincil tarot kartınız: İmparator,\nDüzen kurabilen yanınız, belirsizlik karşısında sınırlarınızı belirlemenizi ve sağlam adımlar atmanızı destekler.")
    elif ikinci == 5:
        print("İkincil tarot kartınız: Aziz,\nDeneyimlerinizden anlam çıkaran yönünüz, kendi değerlerinize dayanarak karar vermenize yardımcı olur.")
    elif ikinci == 6:
        print("İkincil tarot kartınız: Âşıklar,\nBağ kurma ve uzlaşma beceriniz, seçimlerinizde hem kendinizi hem de önem verdiğiniz kişileri gözetmenizi destekler.")
    elif ikinci == 7:
        print("İkincil tarot kartınız: Savaş Arabası,\nİçsel kararlılığınız, dikkatiniz dağıldığında yeniden odaklanmanıza ve yolunuza devam etmenize yardımcı olur.")
    elif ikinci == 8:
        print("İkincil tarot kartınız: Güç,\nSakin ve şefkatli yanınız, zorlayıcı duygular karşısında kendinize anlayış göstererek dayanıklılığınızı korumanızı destekler.")
    elif ikinci == 8:
        print("İkincil tarot kartınız: Ermiş,\nİç dünyanıza dönebilme beceriniz, dışarıdaki seslerden uzaklaşıp kendi yanıtlarınızı bulmanıza yardımcı olur.")
else:
    print("\nTarot sayınız zaten tek hanelidir; bu yöntemde ayrı bir ikincil kartınız bulunmamaktadır.")

print("\nbabil devrilmiş galiba\nmade by: tunaguro") 
