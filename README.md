# Tugas Machine Learning — Latihan Python Dasar

Menjalankan seluruh latihan dari PPT **Python Dasar** (11 bab).

- Nama   : _(isi nama)_
- NIM    : _(isi NIM)_
- Dosen  : Pak Wawan

## Struktur
| Folder | Isi |
|---|---|
| `bab01` | Pengenalan Python (`hello.py`) |
| `bab02` | Variabel, tipe data, casting, string |
| `bab03` | Input & output |
| `bab04` | Operator |
| `bab05` | Percabangan (if/elif/else, nested, ternary, match-case) |
| `bab06` | Perulangan (for, while, break/continue/pass) |
| `bab07` | List, tuple, set, dictionary |
| `bab08` | Function (parameter, lambda, scope) |
| `bab09` | Error handling (try/except, raise) |
| `bab10` | Module & package (`utils/`), perintah pip di `perintah_pip.md` |
| `bab11` | Pengolahan data CSV, mini project, pandas |
| `hasil_output` | Hasil (output) setiap file setelah dijalankan |

## Cara menjalankan
Gunakan Python 3.10+ (karena `match-case`). Contoh:

```bash
cd bab01
python hello.py
```

Catatan:
- `bab03/input.py` dan `bab09/try_except.py` meminta input dari keyboard.
- `bab07/tuple.py` memang berakhir dengan `TypeError` (sengaja, untuk menunjukkan tuple tidak bisa diubah).
- `bab11/pakai_pandas.py` butuh `pip install pandas`.
- File `bab11/*.py` harus dijalankan dari dalam folder `bab11` (agar `nilai.csv` terbaca).
