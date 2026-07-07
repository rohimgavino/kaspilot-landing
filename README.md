# 🚀 KasPilot - Landing Page

Landing page premium untuk produk **KasPilot**, sistem pencatatan keuangan bulanan otomatis berbasis Bot Telegram, Google Apps Script, dan Google Sheets terintegrasi AI (Gemini & Groq).

Halaman ini didesain modern menggunakan konsep *dark mode* futuristik, transisi yang halus, layout responsif (*mobile-friendly*), dan dilengkapi navigasi yang intuitif untuk meningkatkan konversi penjualan produk Anda.

🌐 **Link Live Demo**: [https://rohimgavino.github.io/kaspilot-landing/](https://rohimgavino.github.io/kaspilot-landing/)

---

## ✨ Fitur Landing Page
- **Hero Section**: Judul utama dengan gradien teks yang memikat, penjelasan singkat produk, serta tombol CTA (*Call to Action*) ganda.
- **Dashboard Preview Mockup**: Pratinjau visual dari dashboard dark mode KasPilot yang menyala (*neon border effect*).
- **Fitur Unggulan**: Blok kartu fitur yang menjelaskan integrasi Voice Note (AI Whisper), Scan Struk Belanja (AI Gemini/Groq), pemisahan kas usaha & keluarga, pengingat tagihan otomatis, dan target tabungan impian.
- **Cara Kerja**: Alur aktivasi pembeli berlisensi (*Paket Aktivasi*, *Pasang Library*, *Deploy Web App*, *Setup Wizard & Webhook*).
- **Pricing Card**: Skema harga penawaran terbatas sekali bayar seumur hidup (*one-time lifetime access*) dengan daftar benefit lengkap.
- **Checkout Pembayaran**: Modal pembelian dengan data pembeli, QRIS custom/dinamis, transfer bank, pembayaran manual, kode unik, dan konfirmasi WhatsApp.
- **FAQ Accordion**: Tanya jawab interaktif untuk mengatasi keraguan calon pembeli (keamanan data, biaya langganan, dll).

---

## 🛠️ Cara Menyesuaikan Landing Page

Untuk mengubah tautan pemesanan WhatsApp, harga, metode pembayaran, admin, dan template spreadsheet internal:

1. Buka berkas `index.html`.
2. Cari blok `ADMIN_SETTINGS` di bagian bawah file.
3. Ubah `whatsappNumber` dengan nomor admin Anda sendiri. Gunakan format kode negara, misal `628xxxxxxxxxx` tanpa angka `0` di depan.
4. Ubah `adminName` jika ingin mengganti nama admin.
5. Ubah `basePrice` jika harga promo berubah.
6. Ubah `payment.qris.staticPayload` dengan payload QRIS statis merchant agar checkout dapat membuat QRIS nominal otomatis.
7. Ubah `payment.bank` jika ingin menerima transfer bank.
8. Ubah `spreadsheetTemplateCopyUrl` jika link template master berubah. Link ini hanya catatan internal untuk admin dan tidak ditampilkan sebagai tombol publik.
9. Untuk membalas pembeli setelah pembayaran, salin format di `PAKET_SIAP_KIRIM_KASPILOT.md`, lalu ganti bagian License Key sesuai lisensi pembeli.

### Panel Admin Online (Terintegrasi Google Sheets)

KasPilot kini dilengkapi dengan halaman panel admin mandiri (`admin.html`) seperti halnya Taaruf Planner. Data pesanan pembeli dan pengaturan website disimpan langsung di Google Sheets Master Penjualan Anda, sehingga:
- Pengaturan harga, WhatsApp, bank, dan QRIS berubah seketika untuk semua pengunjung website tanpa perlu mengubah kode `index.html`.
- Setiap pesanan pembeli yang mengklik tombol bayar tercatat otomatis di Google Sheets.
- Anda bisa memantau status pesanan, total bayar, bukti transaksi, hingga omset penjualan real-time di dasbor admin.

#### Cara Mengaktifkan:
1. **Buat Google Sheets Master**: Buat sebuah spreadsheet di Google Drive Anda (misal: `Database Penjualan KasPilot`).
2. **Pasang Apps Script**: Klik menu **Ekstensi > Apps Script**. Hapus kode bawaan, lalu tempel isi berkas `AppsScript_MasterPenjualan.js` yang ada di proyek ini.
3. **Konfigurasi & Deploy**: 
   - Ubah `ADMIN_TOKEN_DEFAULT` di baris 19 sesuai sandi/token admin pilihan Anda.
   - Klik tombol **Terapkan > Penerapan baru (New Deployment)**.
   - Pilih jenis penerapan: **Aplikasi web**.
   - Setel *Jalankan sebagai:* **Saya** dan *Siapa yang memiliki akses:* **Siapa saja**.
   - Klik **Terapkan** dan berikan otorisasi Google.
   - Salin **URL Aplikasi Web** yang diberikan.
4. **Integrasikan ke Landing Page**:
   - Buka berkas `index.html`. Cari `googleWebAppUrl` di dalam blok `ADMIN_DEFAULT_SETTINGS`, lalu tempel URL Web App tersebut di sana:
     `googleWebAppUrl: "https://script.google.com/macros/s/.../exec"`
   - Push perubahan `index.html` ini ke GitHub.
5. **Gunakan Dasbor Admin**:
   - Buka URL website Anda dengan tambahan path `/admin.html` (misal: `https://rohimgavino.github.io/kaspilot-landing/admin.html`).
   - Masukkan **URL Web App** dan **Sandi/Token Admin** Anda untuk login.
   - Sekarang Anda dapat mengelola pengaturan penjualan dan daftar pesanan langsung dari browser!

### Panel Admin Lokal (Cadangan Offline)

Jika Anda tidak menggunakan database Google Sheets (kolom `googleWebAppUrl` dikosongkan), Anda tetap bisa menggunakan panel admin lokal bawaan (di dalam halaman utama) dengan parameter query:
```js
const ADMIN_DEFAULT_SETTINGS = {
  whatsappNumber: "6285712345678",
  adminName: "Admin KasPilot",
  productName: "KasPilot Master Template",
  basePrice: 99000,
  useUniqueCode: true,
  buyerLibraryScriptId: "1cDP1qYyFTpPYi51pzg_quS83Vd9wCKOtkuPMCZney-GSDcGWZDLlNDIK",
  spreadsheetTemplateCopyUrl: "https://docs.google.com/spreadsheets/d/13lgynvUMOhudeD7YdQnlBiUgbjkoQipwX1ExDWcOxpY/copy",
  spreadsheetTemplateEditUrl: "https://docs.google.com/spreadsheets/d/13lgynvUMOhudeD7YdQnlBiUgbjkoQipwX1ExDWcOxpY/edit",
  payment: {
    qris: {
      enabled: true,
      merchantName: "KasPilot",
      staticPayload: "TEMPEL_PAYLOAD_QRIS_STATIS_DI_SINI"
    },
    bank: {
      enabled: true,
      bankName: "BCA",
      accountNumber: "0000000000",
      accountName: "NAMA PEMILIK REKENING"
    },
    manual: {
      enabled: true,
      label: "Manual via WhatsApp"
    }
  }
};
```

Alur penjualan yang disarankan:
1. Calon pembeli klik tombol beli dan mengisi checkout.
2. Pembeli memilih QRIS, transfer bank, atau pembayaran manual.
3. Pembeli mengirim konfirmasi dan bukti pembayaran lewat WhatsApp dari tombol checkout.
4. Setelah pembayaran terkonfirmasi, admin membuat/mengambil License Key pembeli.
5. Admin mengirim paket aktivasi: link Make a Copy template, License Key, Script ID Library, dan panduan setup.
6. Pembeli copy template, memasang Library dengan identifier `KasPilotLibrary`, deploy Web App, isi Setup Wizard, lalu klik Set Webhook.

Catatan QRIS:
- `staticPayload` diisi dengan payload teks QRIS statis merchant, bukan gambar QR.
- Jika `staticPayload` kosong atau tidak valid, checkout tetap bisa dipakai untuk transfer bank atau konfirmasi manual via WhatsApp.
- Kode unik bisa dimatikan dengan mengubah `useUniqueCode` menjadi `false`.

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
