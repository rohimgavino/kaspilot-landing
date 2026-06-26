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

Untuk mengubah tautan pemesanan WhatsApp, admin, dan template spreadsheet internal:

1. Buka berkas `index.html`.
2. Cari blok `ADMIN_SETTINGS` di bagian bawah file.
3. Ubah `whatsappNumber` dengan nomor admin Anda sendiri. Gunakan format kode negara, misal `628xxxxxxxxxx` tanpa angka `0` di depan.
4. Ubah `adminName` jika ingin mengganti nama admin.
5. Ubah `spreadsheetTemplateCopyUrl` jika link template master berubah. Link ini hanya catatan internal untuk admin dan tidak ditampilkan sebagai tombol publik.

Contoh blok konfigurasi:
```js
const ADMIN_SETTINGS = {
  whatsappNumber: "6285712345678",
  adminName: "Admin KasPilot",
  spreadsheetTemplateCopyUrl: "https://docs.google.com/spreadsheets/d/ID_SPREADSHEET/copy",
  spreadsheetTemplateEditUrl: "https://docs.google.com/spreadsheets/d/ID_SPREADSHEET/edit"
};
```

Alur penjualan yang disarankan:
1. Calon pembeli klik WhatsApp dari landing page.
2. Admin mengirim instruksi pembayaran.
3. Setelah pembayaran terkonfirmasi, admin mengirim link Make a Copy template secara manual.

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
