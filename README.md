# stock-tracker

Command-line stock management system.

## V0 → V1 Değişiklikleri

### V0
- Sadece `init` ve `add` komutları çalışıyordu.
- Diğer komutlar "will be implemented" mesajı veriyordu.

### V1
- `list` komutu eklendi — tüm ürünleri listeler.
- `remove` komutu eklendi — stok miktarını azaltır.
- `search` komutu eklendi — ürün arar.

## V1 Görev Listesi
- [x] TASK 1: list komutunu tamamla
- [x] TASK 2: remove komutunu tamamla
- [x] TASK 3: search komutunu tamamla

## Kullanım
```bash
python stocktracker.py init
python stocktracker.py add "Apple" 50 10
python stocktracker.py list
python stocktracker.py remove "Apple" 10
python stocktracker.py search "Apple"
```

## Veri Formatı
```
id|name|quantity|price|date|status
1|Apple|50|10|2026-03-15|1
```
