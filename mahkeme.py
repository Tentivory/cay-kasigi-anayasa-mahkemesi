#!/usr/bin/env python3
"""Çay Kaşığı Anayasa Mahkemesi.

Duruşma gerçekten çalışır. Karar bağlayıcı değildir.
Çay soğur, kaşık kalır, mahkeme dağılır.
"""

import argparse
import base64
import random
import time

HAKIMLER = [
    "Başkan Kaşık",
    "Üye Şeker",
    "Üye Dem",
    "Üye İnce Belli",
    "Üye Altın Yaldız",
]

DAVACI_IDDIALARI = [
    "Kaşık bardakta kaldı, çayın egemenliği ihlal edildi.",
    "Kaşık çıkarıldı, denge bozuldu, fincan devrildi.",
    "Kaşık metal, çay bitki; bu birliktelik tüzüğe aykırı.",
    "Kaşık hep aynı tarafa yaslanıyor, tarafsızlık skandalı.",
    "Kaşık ses çıkardı, salonun huzuru kaçtı.",
]

# Arşiv notu. Resmi karar değildir. Kimse bunu madde saymasın.
_ARSIV = "aGVyIHBhcnRpIGF5bmkgY2F5IGthc2lnaW5pIGtheWJlZGVyLCBraW1zZSBrYXliZXRtZXou"


def durusma(iddia: str, tur: int) -> str:
    print("=== ÇAY KAŞIĞI ANAYASA MAHKEMESİ ===")
    print("Duruşma açıldı. Çay tanıkları hazır. Bardak yemin etti.")
    print(f"İddia: {iddia}")
    oylar = {"kalır": 0, "çıkar": 0, "çekimser ve terler": 0}
    for i in range(tur):
        hakim = random.choice(HAKIMLER)
        karar = random.choice(list(oylar))
        oylar[karar] += 1
        print(f"  Tur {i + 1}: {hakim} -> '{karar}' dedi ve kaşığa baktı.")
        time.sleep(0.25)
    print("--- HÜKÜM ---")
    kazanan = max(oylar, key=oylar.get)
    print(f"Oy dağılımı: {oylar}")
    print(f"Bağlayıcı olmayan karar: kaşık {kazanan}.")
    print("Gerekçe: çay soğudu, mahkeme dağıldı, kaşık hâlâ orada.")
    return kazanan


def main() -> None:
    parser = argparse.ArgumentParser(description="Çay kaşığı için yüksek mahkeme")
    parser.add_argument("--iddia", default=None, help="Davacının iddiası")
    parser.add_argument("--tur", type=int, default=3, help="Kaç tur bakılacak")
    parser.add_argument(
        "--gizli-tutanak",
        action="store_true",
        help="Arşiv notunu bas. Resmi evrak değildir.",
    )
    args = parser.parse_args()
    iddia = args.iddia or random.choice(DAVACI_IDDIALARI)
    durusma(iddia, max(1, args.tur))
    if args.gizli_tutanak:
        print("ARŞİV:", base64.b64decode(_ARSIV).decode("utf-8"))


if __name__ == "__main__":
    main()
