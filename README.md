# 🤖 Instagram Comment Bot

Sebuah script **Python** untuk mengotomatisasi login ke Instagram dan memberikan komentar pada beberapa postingan secara otomatis.  
Cocok untuk proyek pribadi atau belajar automasi web.

---

## ⚡ Fitur

- Login otomatis ke akun Instagram  
- Mengakses beberapa postingan sekaligus  
- Memberikan komentar otomatis: `"Wah keren banget!"`

---

## 🛠 Teknologi

- Python 3.x  
- Selenium  
- undetected-chromedriver  

---

## 💾 Instalasi

1. Pastikan Python 3.x sudah terpasang  
2. Install package yang dibutuhkan dengan menjalankan perintah berikut di terminal atau command prompt:
```bash
pip install selenium undetected-chromedriver
```
3. Simpan script Python di folder proyek kamu, misal instagram_bot.py

---

## 🚀 Cara Pakai

1. Buka file instagram_bot.py
2. Ganti username dan password Instagram kamu pada bagian login:
```python
driver.find_element(By.NAME, "username").send_keys("ISI USERNAME")
driver.find_element(By.NAME, "password").send_keys("ISI PASSWORD")
```
3. Ganti link postingan Instagram yang ingin dikomentari:
```python
driver.get("ISI LINK POSTINGAN")
```
4. Jalankan script dengan perintah:
```bash
python instagram_bot.py
```
Script akan otomatis login, membuka postingan, dan memberikan komentar "Wah keren banget!".

---

## ⚠️ Catatan Penting

- Gunakan dengan bijak, jangan terlalu sering untuk mencegah akun diblokir
- Script ini menggunakan time.sleep() untuk jeda supaya lebih aman
- Gunakan akun cadangan jika ingin mencoba banyak postingan

---

## ✨ Tips

- Kamu bisa mengubah komentar sesuai keinginan
- Bisa ditambahkan lebih banyak postingan dengan menyalin blok driver.get(...) dan perintah komentar

Selamat mencoba dan semoga membantu! 🚀
