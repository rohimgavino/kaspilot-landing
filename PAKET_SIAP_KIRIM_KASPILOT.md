# Paket Siap Kirim Pembeli KasPilot

Gunakan file ini setelah pembayaran pembeli terkonfirmasi. Ganti bagian `LICENSE_KEY_PEMBELI` dengan License Key yang dibuat untuk pembeli tersebut.

## Data Paket

- Produk: KasPilot Master Template
- Template buyer: https://docs.google.com/spreadsheets/d/13lgynvUMOhudeD7YdQnlBiUgbjkoQipwX1ExDWcOxpY/copy
- Script ID Library: `1cDP1qYyFTpPYi51pzg_quS83Vd9wCKOtkuPMCZney-GSDcGWZDLlNDIK`
- Identifier Library: `KasPilotLibrary`
- Panduan PDF: https://rohimgavino.github.io/kaspilot-landing/Panduan_Instalasi_KasPilot.pdf

## Pesan WhatsApp Siap Kirim

```text
Halo Kak, pembayaran KasPilot sudah kami terima. Berikut paket aktivasi lengkapnya:

1. Link Template KasPilot
https://docs.google.com/spreadsheets/d/13lgynvUMOhudeD7YdQnlBiUgbjkoQipwX1ExDWcOxpY/copy

Klik link di atas, lalu pilih Make a copy / Buat salinan ke Google Drive Kakak.

2. License Key
LICENSE_KEY_PEMBELI

3. Script ID Library KasPilot
1cDP1qYyFTpPYi51pzg_quS83Vd9wCKOtkuPMCZney-GSDcGWZDLlNDIK

Saat menambahkan Library di Apps Script, identifier wajib diisi:
KasPilotLibrary

4. Panduan Instalasi PDF
https://rohimgavino.github.io/kaspilot-landing/Panduan_Instalasi_KasPilot.pdf

Ringkas langkah aktivasi:
1. Buka link template dan buat salinan.
2. Buka Extensions / Ekstensi > Apps Script.
3. Tambahkan Library dengan Script ID di atas.
4. Deploy sebagai Web App.
5. Buka Web App URL.
6. Isi Setup Wizard: License Key, token bot Telegram, PIN dashboard, dan kosongkan Spreadsheet ID jika otomatis.
7. Klik Simpan Setup, lalu klik Set Webhook.

Catatan:
- 1 License Key hanya untuk 1 Spreadsheet aktif.
- Data transaksi tetap tersimpan di Google Drive/Spreadsheet Kakak.
- Jika butuh bantuan setup, kirim screenshot bagian yang membingungkan ke chat ini.
```

## Checklist Admin Sebelum Kirim

- [ ] Pembayaran sudah masuk.
- [ ] License Key sudah dibuat di sheet lisensi.
- [ ] License Key belum pernah dipakai pembeli lain.
- [ ] Nama/nomor WhatsApp pembeli sudah dicatat.
- [ ] `LICENSE_KEY_PEMBELI` pada pesan sudah diganti.
