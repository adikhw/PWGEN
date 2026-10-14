<div align="center">

# 🔐 PWGEN

**Generator Password + Pengecek Kekuatan Password untuk terminal**

Buat password acak yang aman, dan cari tahu *kenapa* sebuah password dinilai lemah, sedang, atau kuat.

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependensi-tidak%20ada-success?style=for-the-badge)
![Interface](https://img.shields.io/badge/interface-CLI-black?style=for-the-badge&logo=gnubash&logoColor=white)
![Status](https://img.shields.io/badge/status-selesai-brightgreen?style=for-the-badge)

</div>

---

## ✨ Apa itu PWGEN?

PWGEN adalah aplikasi terminal (CLI) kecil yang punya dua fungsi:

1. **Membuat** password acak dengan panjang dan jenis karakter pilihan kamu.
2. **Mengecek** seberapa kuat sebuah password (Weak / Medium / Strong) dan **menjelaskan alasannya**.

Tanpa internet, tanpa database, tanpa library eksternal. Cukup modul bawaan Python.

> 🎓 Ini **Project #2** dari jalur belajar saya. Tujuannya latihan string, modul `secrets`, regex, dan memilih tipe data yang tepat.

---

## 🚀 Fitur

| | Fitur | Keterangan |
|---|---|---|
| 🎲 | **Generator aman** | Pakai `secrets` (aman secara kriptografi), bukan `random` |
| 🔡 | **Jenis karakter bebas pilih** | Huruf kecil, huruf besar, angka, simbol, dalam kombinasi apa pun |
| 📏 | **Atur panjang** | 8 sampai 64 karakter |
| ✅ | **Variasi terjamin** | Setiap jenis karakter yang dipilih muncul minimal sekali |
| 🧪 | **Validator kekuatan** | Menilai password: Weak, Medium, atau Strong |
| 💬 | **Hasil disertai alasan** | Menjelaskan *kenapa* password mendapat nilai tersebut |
| 🛡️ | **Input salah tidak bikin crash** | Input yang keliru menampilkan pesan, bukan error |
| 🔒 | **Tidak ada yang disimpan** | Password tidak pernah disimpan ke file atau ditulis ke log |

---

## 📦 Kebutuhan

- Python **3.6 atau lebih baru** (diperlukan untuk modul `secrets`)
- Itu saja. Tidak perlu `pip install`.

Cek versi Python kamu:

```bash
python --version
```

---

## ▶️ Cara Menjalankan

```bash
# 1. Ambil project-nya
git clone https://github.com/adikhw/pwgen.git
cd pwgen

# 2. Jalankan
python main.py
```

---

## 🖥️ Cara Pakai

### Menu utama

```
1. Generate password
2. Check password strength
3. Exit
Choose:
```

### 🎲 Membuat password

```
Choose: 1
Length: 16
Use lowercase letters? (y/n): y
Use uppercase letters? (y/n): y
Use digits? (y/n): y
Use symbols? (y/n): y
Xk7#mP2$vQ9&wLz!
```

> Password di atas hanya contoh. Hasil kamu akan berbeda setiap kali.

### 🧪 Mengecek kekuatan password

```
Choose: 2
Password: Kopi2026
Level: Medium
- Fewer than 12 characters
```

> ⚠️ **Jangan tes pakai password yang benar-benar kamu pakai.** Pakai contoh karangan.

---

## 📊 Cara Penilaian Kekuatan

| Level | Kriteria |
|---|---|
| 🔴 **Weak** | Kurang dari 8 karakter, **atau** hanya 1 jenis karakter, **atau** mengandung pola lemah |
| 🟡 **Medium** | Tidak lemah, tapi belum memenuhi kriteria Strong |
| 🟢 **Strong** | Minimal 12 karakter, minimal 3 jenis karakter, **dan** tanpa pola lemah |

**Jenis karakter:** huruf kecil, huruf besar, angka, simbol.
Karakter apa pun yang bukan huruf atau angka ASCII (termasuk spasi dan emoji) dihitung sebagai simbol.

**Pola lemah yang dideteksi:**

- 🔁 Karakter berulang, seperti `aaaa`
- 🔢 Urutan, seperti `1234` atau `abcd`
- 📖 Kata umum, seperti `password` atau `qwerty` (termasuk yang terselip di dalam, seperti `superuser1`)

---

## 🧠 Kenapa Pakai `secrets`, Bukan `random`?

Modul `random` di Python dibuat untuk simulasi dan game. Hasilnya **bisa ditebak** kalau seseorang berhasil mengetahui kondisi internalnya, jadi **tidak aman untuk password**.

Modul `secrets` mengambil angka acak dari sumber acak yang aman milik sistem operasi, dan memang dirancang untuk nilai sensitif seperti password dan token.

| | `random` | `secrets` |
|---|---|---|
| Tujuan | Simulasi, game | Password, token |
| Bisa ditebak? | Bisa | Dirancang agar tidak bisa |
| Cocok untuk password? | ❌ Tidak | ✅ Ya |

---

## 🗂️ Struktur Project

```
pwgen/
├── main.py          # Titik masuk, menangani Ctrl+C dan error tak terduga
├── cli.py           # Menu dan input/output terminal
├── generator.py     # Logika pembuatan password
├── validator.py     # Logika pengecekan kekuatan password
└── README.md
```

**Aturan desain:** satu file, satu tanggung jawab.
`cli.py` yang berhubungan dengan user. `generator.py` dan `validator.py` berisi logika dan tidak pernah memanggil `print()` atau `input()`.

---

## 🔒 Catatan Keamanan

- Password dibuat dengan `secrets`.
- Password **tidak pernah disimpan** dan **tidak pernah ditulis ke log**.
- Validator berjalan sepenuhnya offline. Validator tidak mengecek apakah password pernah bocor.
- Ini project belajar. Untuk pemakaian sungguhan, password manager khusus adalah pilihan yang lebih baik.

---

## 🙅 Di Luar Cakupan

Sengaja tidak dibuat supaya project tetap fokus:

- Versi GUI, web, atau API
- Menyimpan password ke file atau database
- Cek kebocoran password lewat internet
- Hashing atau enkripsi
- Copy otomatis ke clipboard
- Library eksternal (seperti `zxcvbn`)

---

## 📚 Yang Saya Pelajari

- Method string dan konstanta di modul `string`
- `secrets` vs `random`, dan kenapa itu penting untuk keamanan
- Regex dasar: kelas karakter, negasi, dan backreference
- Memilih antara `list`, `tuple`, `dict`, dan `set`
- Mengembalikan hasil terstruktur dari fungsi (dict berisi `level` dan `reasons`)
- Validasi input dan error handling
- Memecah kode jadi file-file kecil dengan satu tugas masing-masing

---

<div align="center">

Dibuat dengan 🐍 sambil belajar Python

</div>