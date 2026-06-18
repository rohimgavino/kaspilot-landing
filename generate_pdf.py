import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            return  # Tidak menggambar header/footer di halaman sampul
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(HexColor("#4f46e5")) # Warna Indigo
        
        # Header Text
        self.drawString(54, 755, "PANDUAN INSTALASI KASPILOT")
        self.setFont("Helvetica", 8)
        self.setFillColor(HexColor("#64748b")) # Slate gray
        self.drawRightString(541, 755, "Edisi Integrasi AI")
        
        # Header Line
        self.setStrokeColor(HexColor("#e2e8f0"))
        self.setLineWidth(0.75)
        self.line(54, 747, 541, 747)
        
        # Footer Line
        self.line(54, 55, 541, 55)
        
        # Footer Text
        self.drawString(54, 42, "© 2026 KasPilot. All Rights Reserved.")
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(541, 42, page_text)
        self.restoreState()

def build_pdf(filename="Panduan_Instalasi_KasPilot.pdf"):
    # Margins: 0.75 inch (54 pt) kiri-kanan, 1 inch (72 pt) atas-bawah
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=HexColor("#1e1b4b"), # Deep Indigo
        alignment=1, # Center
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=HexColor("#4f46e5"), # Indigo
        alignment=1,
        spaceAfter=30
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=HexColor("#1e1b4b"),
        spaceBefore=16,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=HexColor("#4f46e5"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14.5,
        textColor=HexColor("#334155"), # Slate-700
        spaceBefore=4,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=5
    )
    
    code_text_style = ParagraphStyle(
        'CodeText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=HexColor("#0f172a")
    )

    warning_style = ParagraphStyle(
        'Warning_Custom',
        parent=body_style,
        textColor=HexColor("#991b1b") # Red-800
    )

    story = []
    
    # ----------------------------------------------------
    # HALAMAN 1: COVER PAGE
    # ----------------------------------------------------
    story.append(Spacer(1, 40))
    story.append(Paragraph("🚀 KASPILOT SYSTEM", subtitle_style))
    story.append(Paragraph("PANDUAN INSTALASI & SETUP", title_style))
    story.append(Paragraph("Sistem Catat Keuangan Otomatis via Bot Telegram & Google Sheets", subtitle_style))
    story.append(Spacer(1, 10))
    
    # Overview Image on Cover (Centered)
    if os.path.exists("overview.jpg"):
        img_overview = Image("overview.jpg", width=380, height=214)
        img_overview.hAlign = 'CENTER'
        story.append(img_overview)
    
    story.append(Spacer(1, 50))
    
    meta_style = ParagraphStyle(
        'Meta',
        parent=body_style,
        fontName='Helvetica-Bold',
        fontSize=9,
        textColor=HexColor("#64748b"),
        alignment=1
    )
    story.append(Paragraph("Edisi Integrasi AI (Gemini & Groq) &bull; Versi 2.0 (Lifetime License)", meta_style))
    story.append(PageBreak())
    
    # ----------------------------------------------------
    # HALAMAN 2: PENDAHULUAN & PERSIAPAN
    # ----------------------------------------------------
    story.append(Paragraph("1. Pendahuluan & Persiapan", h1_style))
    story.append(Paragraph(
        "Selamat atas pembelian template <b>KasPilot</b>! Panduan ini akan menuntun Anda menyelesaikan setup dalam "
        "waktu kurang dari 3 menit tanpa memerlukan kemampuan coding atau menyewa server hosting. Seluruh sistem berjalan "
        "di infrastruktur gratis milik Google (Google Drive & Apps Script).", body_style))
    
    story.append(Paragraph("Bahan-bahan yang Wajib Disiapkan:", h2_style))
    story.append(Paragraph("&bull; <b>Akun Google</b> aktif (untuk meng-host Google Spreadsheet dan Google Apps Script).", bullet_style))
    story.append(Paragraph("&bull; <b>Akun Telegram</b> aktif untuk berinteraksi dengan bot.", bullet_style))
    story.append(Paragraph("&bull; <b>Token Bot Telegram</b> (didapatkan gratis dari @BotFather).", bullet_style))
    story.append(Paragraph("&bull; <b>API Key Gemini / Groq</b> (opsional, jika Anda ingin mengaktifkan fitur catat via pesan suara / scan foto struk).", bullet_style))
    
    # Warning Box (Centered table, padded width)
    warning_content = [
        [Paragraph("⚠️ <b>PENTING: JANGAN BAGIKAN TOKEN BOT ANDA!</b><br/>"
                   "Token Telegram Bot dan PIN Dashboard Anda adalah kunci keamanan data keuangan Anda. "
                   "Jangan pernah membagikan informasi ini kepada siapa pun demi menjaga privasi data kas.", warning_style)]
    ]
    warning_table = Table(warning_content, colWidths=[460])
    warning_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#fef2f2")),
        ('BOX', (0,0), (-1,-1), 1, HexColor("#fee2e2")),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    warning_table.hAlign = 'CENTER'
    story.append(Spacer(1, 15))
    story.append(warning_table)
    story.append(PageBreak())
    
    # ----------------------------------------------------
    # HALAMAN 3: LANGKAH 1 - MENYALIN SPREADSHEET
    # ----------------------------------------------------
    story.append(Paragraph("2. Langkah 1: Menyalin Master Spreadsheet", h1_style))
    story.append(Paragraph(
        "Langkah pertama adalah menyalin lembar kerja (spreadsheet) master KasPilot ke Google Drive pribadi Anda.", body_style))
    
    story.append(Paragraph("Langkah detail:", h2_style))
    story.append(Paragraph("1. Buka tautan Google Spreadsheet master yang dikirimkan oleh penjual di browser Anda.", bullet_style))
    story.append(Paragraph("2. Pada menu kiri atas, klik menu <b>File</b> &gt; kemudian klik <b>Make a copy (Buat salinan)</b>.", bullet_style))
    story.append(Paragraph("3. Beri nama spreadsheet tersebut (misalnya: <i>'Dashboard Keuangan Saya'</i>) dan klik **Make a copy**.", bullet_style))
    story.append(Paragraph("4. Tunggu beberapa saat sampai tab spreadsheet salinan baru Anda terbuka sepenuhnya.", bullet_style))
    story.append(Paragraph("5. <b>Salin Spreadsheet ID Anda</b>. ID ini terdapat di URL browser Anda, di antara huruf <i>/d/</i> dan <i>/edit</i>.", bullet_style))
    
    # Code Block Table
    code_content = [
        [Paragraph("Jika URL browser Anda adalah:<br/>"
                   "<code>https://docs.google.com/spreadsheets/d/<b>1A2b3C4d5E6f7G8h9I0J_kLMnOpQrStUvWxYz</b>/edit#gid=0</code><br/><br/>"
                   "Maka ID Spreadsheet Anda adalah bagian yang dicetak tebal:<br/>"
                   "<code>1A2b3C4d5E6f7G8h9I0J_kLMnOpQrStUvWxYz</code>", code_text_style)]
    ]
    code_table = Table(code_content, colWidths=[460])
    code_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.5, HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    code_table.hAlign = 'CENTER'
    story.append(Spacer(1, 10))
    story.append(code_table)
    story.append(PageBreak())

    # ----------------------------------------------------
    # HALAMAN 4: LANGKAH 2 - DEPLOY WEB APP
    # ----------------------------------------------------
    story.append(Paragraph("3. Langkah 2: Deploy Google Apps Script", h1_style))
    story.append(Paragraph(
        "Setelah memiliki salinan spreadsheet, kita perlu mendeploy kode Google Apps Script di dalamnya agar bertindak sebagai jembatan "
        "antara Telegram dan Spreadsheet.", body_style))
    
    story.append(Paragraph("Langkah detail:", h2_style))
    story.append(Paragraph("1. Di halaman Google Spreadsheet Anda, buka menu <b>Extensions (Ekstensi)</b> &gt; klik <b>Apps Script</b>.", bullet_style))
    story.append(Paragraph("2. Halaman editor Google Apps Script akan terbuka di tab baru. Seluruh kode bot sudah terisi di sana secara otomatis.", bullet_style))
    story.append(Paragraph("3. Di pojok kanan atas halaman Apps Script, klik tombol <b>Deploy</b> &gt; klik <b>New deployment</b>.", bullet_style))
    story.append(Paragraph("4. Pada jendela pop-up yang muncul, pastikan jenis deployment adalah <b>Web app</b> (klik ikon gir jika belum).", bullet_style))
    story.append(Paragraph("5. Konfigurasikan tiga kolom berikut dengan tepat:", bullet_style))
    story.append(Paragraph("&bull; <b>Description</b>: Isi bebas, misal: <i>v2.0</i>", bullet_style))
    story.append(Paragraph("&bull; <b>Execute as</b>: Pilih <b>Me (email Anda@gmail.com)</b>", bullet_style))
    story.append(Paragraph("&bull; <b>Who has access</b>: Wajib pilih <b>Anyone (Siapa saja)</b>", bullet_style))
    story.append(Paragraph("6. Klik tombol **Deploy** di bagian bawah.", bullet_style))
    story.append(Paragraph("7. Jendela otorisasi akses Google akan muncul. Klik <b>Authorize Access</b> &gt; Pilih Akun Google Anda &gt; Klik <b>Advanced</b> di bagian kiri bawah &gt; Klik <b>Go to KasPilot (unsafe)</b> &gt; Klik <b>Allow</b>.", bullet_style))
    story.append(Paragraph("8. Setelah proses selesai, **Salin Web App URL** yang diberikan. Simpan URL ini karena akan dimasukkan ke Setup Wizard.", bullet_style))
    story.append(PageBreak())

    # ----------------------------------------------------
    # HALAMAN 5: LANGKAH 3 - SETUP WIZARD & WEBHOOK
    # ----------------------------------------------------
    story.append(Paragraph("4. Langkah 3: Setup Wizard & Aktivasi Webhook", h1_style))
    story.append(Paragraph(
        "Langkah terakhir adalah mengaktifkan webhook Telegram menggunakan Setup Wizard terintegrasi.", body_style))
    
    story.append(Paragraph("Langkah detail:", h2_style))
    story.append(Paragraph("1. Tempelkan (Paste) **Web App URL** yang telah Anda salin sebelumnya ke tab browser baru Anda.", bullet_style))
    story.append(Paragraph("2. Layar PIN Akses akan muncul. Masukkan PIN bawaan Anda (Anda dapat mengecek PIN awal pada dokumen penjualan).", bullet_style))
    story.append(Paragraph("3. Setelah masuk, halaman **Setup Wizard** akan terbuka. Masukkan data berikut:", bullet_style))
    story.append(Paragraph("&bull; <b>Nama Produk</b>: Masukkan nama aplikasi Anda (misal: <i>KasPilot</i>).", bullet_style))
    story.append(Paragraph("&bull; <b>PIN Dashboard</b>: Buat PIN baru 4-8 angka keamanan untuk mengunci dashboard Anda.", bullet_style))
    story.append(Paragraph("&bull; <b>Bot Token Telegram</b>: Tempelkan token yang Anda dapat dari BotFather.", bullet_style))
    story.append(Paragraph("&bull; <b>Spreadsheet ID</b>: Tempelkan ID Spreadsheet yang didapat di Langkah 1.", bullet_style))
    story.append(Paragraph("&bull; <b>Gemini / Groq API Key</b>: Isi jika ingin memakai pencatatan suara / foto struk.", bullet_style))
    story.append(Paragraph("&bull; <b>Web App URL</b>: Isi otomatis dari link halaman saat ini.", bullet_style))
    story.append(Paragraph("4. Klik tombol <b>Simpan Setup</b>. Data akan disimpan aman di memori internal script Google Anda.", bullet_style))
    story.append(Paragraph("5. Klik tombol <b>Set Webhook</b> untuk menghubungkan bot Telegram Anda dengan script Google.", bullet_style))
    story.append(Paragraph("6. Terakhir, klik <b>Cek Setup</b> untuk memastikan status integrasi sukses (berwarna hijau).", bullet_style))
    
    # Setup Image (Centered)
    if os.path.exists("setup_wizard.jpg"):
        story.append(Spacer(1, 10))
        img_setup = Image("setup_wizard.jpg", width=380, height=214)
        img_setup.hAlign = 'CENTER'
        story.append(img_setup)
    
    story.append(PageBreak())

    # ----------------------------------------------------
    # HALAMAN 6: CARA PENGGUNAAN & PENDUKUNG
    # ----------------------------------------------------
    story.append(Paragraph("5. Panduan Penggunaan & Tips Keuangan", h1_style))
    story.append(Paragraph(
        "Selamat! Bot Anda kini sudah aktif sepenuhnya. Buka chat Telegram dengan Bot Anda, ketik tombol <code>/start</code> "
        "dan Anda dapat segera melakukan pencatatan keuangan.", body_style))
    
    story.append(Paragraph("Format Pencatatan Chat Telegram:", h2_style))
    story.append(Paragraph("&bull; <b>Pencatatan Manual Teks</b>: "
                           "Ketik: <code>Beli bakso 25.000 makanan usaha</code> atau <code>Gaji bulanan 5.000.000 masuk keluarga</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>Pencatatan Voice Note (Suara)</b>: "
                           "Kirim pesan suara secara natural, misal: <i>'Beli bensin motor dua puluh ribu rupiah dompet usaha'</i>.", bullet_style))
    story.append(Paragraph("&bull; <b>Pencatatan Foto Struk</b>: "
                           "Kirim foto struk belanjaan supermarket atau slip transfer bank, dan AI akan membaca nominal total secara otomatis.", bullet_style))
    
    # Dashboard Mockup Preview (Centered)
    if os.path.exists("dashboard_mockup.jpg"):
        story.append(Spacer(1, 10))
        img_mockup = Image("dashboard_mockup.jpg", width=380, height=200)
        img_mockup.hAlign = 'CENTER'
        story.append(img_mockup)
    
    story.append(Spacer(1, 12))
    story.append(Paragraph("Hubungi Layanan Support jika Anda mengalami kesulitan dalam proses instalasi ini. Selamat mencatat keuangan dengan cerdas!", body_style))
    
    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    build_pdf()
