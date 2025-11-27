# =====================================
# ÇOKLU DRONE KOORDİNASYON SİSTEMİ
# =====================================

def drone_olustur(id, model):
    """Yeni bir drone dictionary'si oluşturur"""
    return {
        "id": id,
        "model": model,
        "batarya": 100,
        "yukseklik": 0,
        "x": 0,
        "y": 0,
        "durum": "Hazır",
        "gorev_sayisi": 0
    }

def drone_bilgi(drone):
    """Drone bilgilerini gösterir"""
    print(f"  🚁 {drone['id']} ({drone['model']})")
    print(f"     🔋 Batarya: %{drone['batarya']}")
    print(f"     📍 Konum: ({drone['x']}, {drone['y']}, {drone['yukseklik']}m)")
    print(f"     ✅ Durum: {drone['durum']}")
    print(f"     📊 Görev: {drone['gorev_sayisi']}")

def filo_durumu(dronlar):
    """Tüm drone filosunun durumunu gösterir"""
    print("\n" + "=" * 60)
    print("📊 DRONE FİLOSU DURUMU")
    print("=" * 60)
    for drone in dronlar:
        drone_bilgi(drone)
        print()
    print("=" * 60)

def drone_kalkis(drone, hedef_yukseklik):
    """Drone'u belirtilen yüksekliğe çıkarır"""
    print(f"\n🚀 {drone['id']} kalkış yapıyor...")
    
    for yukseklik in range(0, hedef_yukseklik + 1, 10):
        drone['yukseklik'] = yukseklik
        drone['batarya'] -= 2

    drone['durum'] = "Havada"
    print(f"✅ {drone['id']} {hedef_yukseklik}m yüksekliğe ulaştı!")

def drone_hareket(drone, yon, mesafe):
    """Drone'u belirtilen yönde hareket ettirir"""
    print(f"🧭 {drone['id']} {yon} yönünde {mesafe}m hareket ediyor...")
    
    if yon == "Kuzey":
        drone['y'] += mesafe
    elif yon == "Güney":
        drone['y'] -= mesafe
    elif yon == "Doğu":
        drone['x'] += mesafe
    elif yon == "Batı":
        drone['x'] -= mesafe
    
    drone['batarya'] -= mesafe // 10
    drone['gorev_sayisi'] += 1
    
    print(f"✅ Yeni konum: ({drone['x']}, {drone['y']})")

def drone_acil_inis(drone):
    """Batarya düşükse drone'u acil indirir"""
    if drone['batarya'] < 15 and drone['durum'] == "Havada":
        print(f"\n⚠️ ACİL DURUM! {drone['id']} batarya kritik (%{drone['batarya']})!")
        print(f"⬇️ {drone['id']} acil iniş yapıyor...")

        while drone['yukseklik'] > 0:
            drone['yukseklik'] -= 10
            drone['batarya'] -= 1

        drone['durum'] = "Acil İniş"
        print(f"✅ {drone['id']} acil iniş yaptı!")

def drone_inis(drone):
    """Drone'u indirir"""
    print(f"\n⬇️ {drone['id']} iniş yapıyor...")
    
    while drone['yukseklik'] > 0:
        drone['yukseklik'] -= 10
        drone['batarya'] -= 1

    drone['yukseklik'] = 0
    drone['durum'] = "Yerde"
    print(f"✅ {drone['id']} iniş tamamladı!")

def otonom_gorev(drone, rota):
    """Drone'a otonom görev verir"""
    print(f"\n📋 {drone['id']} otonom görev başlatıyor...")
    print(f"   Rota: {len(rota)} nokta")
    
    for i, nokta in enumerate(rota, 1):
        # Görev sırasında acil iniş kontrolü
        if drone['batarya'] < 20:
            print(f"⚠️ {drone['id']} batarya kritik! Görev iptal.")
            break
        
        yon, mesafe = nokta
        print(f"\n   {i}. Adım:", end=" ")
        drone_hareket(drone, yon, mesafe)

    print(f"\n✅ {drone['id']} görev tamamlandı!")

# =====================================
# ANA PROGRAM
# =====================================

print("🚁 ÇOKLU DRONE KOORDİNASYON SİSTEMİ BAŞLATILIYOR...")
print("=" * 60)

# Drone filosu oluştur
drone_filosu = [
    drone_olustur("ALFA-1", "Bayraktar TB2"),
    drone_olustur("ALFA-2", "Akıncı"),
    drone_olustur("ALFA-3", "Bayraktar TB2"),
    drone_olustur("ALFA-4", "Akıncı")
]

# Başlangıç durumu
filo_durumu(drone_filosu)

# -----------------------------
# AŞAMA 1: TOPLU KALKIŞ
# -----------------------------
print("\n" + "🚀" * 30)
print("AŞAMA 1: TOPLU KALKIŞ")
print("🚀" * 30)

for drone in drone_filosu:
    drone_kalkis(drone, 50)

filo_durumu(drone_filosu)

# -----------------------------
# AŞAMA 2: GÖREVLER
# -----------------------------
print("\n" + "📋" * 30)
print("AŞAMA 2: GÖREV DAĞITIMI")
print("📋" * 30)

rota_1 = [("Kuzey", 30), ("Doğu", 20), ("Güney", 10)]
rota_2 = [("Doğu", 40), ("Kuzey", 30)]
rota_3 = [("Batı", 20), ("Güney", 25), ("Doğu", 15)]
rota_4 = [("Doğu", 30), ("Batı", 20), ("Kuzey", 20)]

otonom_gorev(drone_filosu[0], rota_1)
otonom_gorev(drone_filosu[1], rota_2)
otonom_gorev(drone_filosu[2], rota_3)
otonom_gorev(drone_filosu[3], rota_4)

filo_durumu(drone_filosu)

# -----------------------------
# ACİL İNİŞ KONTROLÜ
# -----------------------------
for drone in drone_filosu:
    drone_acil_inis(drone)

# -----------------------------
# AŞAMA 3: TOPLU İNİŞ
# -----------------------------
print("\n" + "⬇️" * 30)
print("AŞAMA 3: TOPLU İNİŞ")
print("⬇️" * 30)

for drone in drone_filosu:
    if drone['durum'] == "Havada":
        drone_inis(drone)

# Son durum
filo_durumu(drone_filosu)

# -----------------------------
# MİSYON RAPORU
# -----------------------------
print("\n📊 MİSYON RAPORU")
print("=" * 60)

toplam_gorev = sum(drone['gorev_sayisi'] for drone in drone_filosu)
ortalama_batarya = sum(drone['batarya'] for drone in drone_filosu) / len(drone_filosu)

print(f"✅ Toplam görev sayısı: {toplam_gorev}")
print(f"🔋 Ortalama kalan batarya: %{ortalama_batarya:.1f}")
print(f"🚁 Aktif drone sayısı: {len(drone_filosu)}")
print("=" * 60)
