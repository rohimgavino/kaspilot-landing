# 🚀 KasPilot - Landing Page

Landing page premium untuk produk **KasPilot**, sistem pencatatan keuangan bulanan otomatis berbasis Bot Telegram, Google Apps Script, dan Google Sheets terintegrasi AI (Gemini & Groq).

Halaman ini didesain modern menggunakan konsep *dark mode* futuristik, transisi yang halus, layout responsif (*mobile-friendly*), dan dilengkapi navigasi yang intuitif untuk meningkatkan konversi penjualan produk Anda.

🌐 **Link Live Demo**: [https://rohimgavino.github.io/kaspilot-landing/](https://rohimgavino.github.io/kaspilot-landing/)

---

## ✨ Fitur Landing Page
- **Hero Section**: Judul utama dengan gradien teks yang memikat, penjelasan singkat produk, serta tombol CTA (*Call to Action*) ganda.
- **Dashboard Preview Mockup**: Pratinjau visual dari dashboard dark mode KasPilot yang menyala (*neon border effect*).
- **Fitur Unggulan**: Blok kartu fitur yang menjelaskan integrasi Voice Note (AI Whisper), Scan Struk Belanja (AI Gemini/Groq), pemisahan kas usaha & keluarga, pengingat tagihan otomatis, dan target tabungan impian.
- **Cara Kerja**: Alur instalasi produk 3 langkah mudah (*Copy Template*, *Deploy Web App*, *Setup Wizard*).
- **Pricing Card**: Skema harga penawaran terbatas sekali bayar seumur hidup (*one-time lifetime access*) dengan daftar benefit lengkap.
- **FAQ Accordion**: Tanya jawab interaktif untuk mengatasi keraguan calon pembeli (keamanan data, biaya langganan, dll).

---

## 🛠️ Cara Menyesuaikan Landing Page

Untuk mengubah tautan pemesanan WhatsApp agar langsung masuk ke nomor Anda sendiri:

1. Buka berkas `index.html`.
2. Cari bagian tombol CTA (Gunakan `Ctrl + F` dan cari kata kunci `wa.me`).
3. Ubah nomor WhatsApp `6281234567890` dengan nomor Anda sendiri (gunakan format kode negara, misal `628xxxxxxxxxx` tanpa angka `0` di depan).
4. Sesuaikan pesan pembuka otomatis di belakang teks `?text=...` sesuai keinginan Anda.

Contoh baris kode yang perlu diubah (terdapat di tombol navigasi atas, hero section, dan pricing card):
```html
<!-- Sebelum -->
<a href="https://wa.me/6281234567890?text=Halo%20saya%20tertarik%20membeli%20bot%20KasPilot" class="btn-cta-nav" target="_blank">Beli Sekarang</a>

<!-- Sesudah (Misal nomor Anda 085712345678) -->
<a href="https://wa.me/6285712345678?text=Halo%20saya%20ingin%20membeli%20bot%20KasPilot" class="btn-cta-nav" target="_blank">Beli Sekarang</a>
```

---

## 🚀 Cara Menghosting Kembali di GitHub Pages

Jika Anda menggarpu (*fork*) repositori ini dan ingin mengaktifkannya kembali di GitHub Pages akun Anda:

1. Buka repositori Anda di GitHub.
2. Masuk ke menu **Settings > Pages**.
3. Pada bagian **Build and deployment**, pilih **Deploy from a branch** pada opsi *Source*.
4. Pada bagian **Branch**, pilih **main** dan direktori **`/ (root)`**, kemudian klik **Save**.
5. Tunggu sekitar 1-2 menit, situs landing page Anda akan live secara otomatis!

---

## 📄 Lisensi
Proyek ini dilindungi hak cipta untuk penggunaan personal dalam memasarkan produk KasPilot. Modifikasi dan penyesuaian konten untuk keperluan penjualan pribadi diperbolehkan.
