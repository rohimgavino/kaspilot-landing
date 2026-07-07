/**
 * GOOGLE APPS SCRIPT - MASTER DATABASE PENJUALAN KASPILOT
 * 
 * Petunjuk Pemasangan:
 * 1. Buat Google Spreadsheet baru di Google Drive Anda (misal: "Database Penjualan KasPilot").
 * 2. Klik menu Extensi -> Apps Script.
 * 3. Hapus kode bawaan, lalu tempel seluruh kode di bawah ini.
 * 4. Ganti nilai "ADMIN_TOKEN_DEFAULT" sesuai keinginan Anda (ini adalah sandi login admin).
 * 5. Klik tombol Deploy -> Penerapan Baru (New Deployment).
 * 6. Pilih Jenis Penerapan: Aplikasi Web (Web App).
 * 7. Konfigurasi:
 *    - Jalankan sebagai: Saya (Execute as: Me)
 *    - Siapa yang memiliki akses: Siapa saja (Who has access: Anyone)
 * 8. Klik Terapkan (Deploy), lalu setujui izin Google.
 * 9. Salin URL Aplikasi Web yang diberikan, lalu masukkan ke Panel Admin website KasPilot Anda.
 */

var ADMIN_TOKEN_KEY = "KASPILOT_ADMIN_TOKEN";
var ADMIN_TOKEN_DEFAULT = "kaspilot123"; // Ganti password login admin Anda di sini

function setupSheetsOtomatis() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // 1. Buat Sheet Settings jika belum ada
  var sheetSettings = ss.getSheetByName("Settings");
  if (!sheetSettings) {
    sheetSettings = ss.insertSheet("Settings");
    var headers = ["Key", "Value", "Deskripsi"];
    sheetSettings.appendRow(headers);
    sheetSettings.getRange("A1:C1").setFontWeight("bold").setBackground("#e2e8f0");
    
    // Tulis default settings ke sheet
    var defaultSettings = [
      ["whatsappNumber", "628991977560", "Nomor WhatsApp admin penjualan"],
      ["adminName", "Admin KasPilot", "Nama Admin yang tampil"],
      ["productName", "KasPilot Master Template", "Nama Produk"],
      ["basePrice", "99000", "Harga promo dasar"],
      ["useUniqueCode", "true", "Tambahkan kode unik pada total bayar (true/false)"],
      ["bankName", "BCA", "Nama Bank tujuan transfer"],
      ["accountNumber", "0000000000", "Nomor rekening bank"],
      ["accountName", "NAMA PEMILIK REKENING", "Nama pemilik rekening bank"],
      ["qrisMerchantName", "KasPilot", "Nama merchant QRIS"],
      ["qrisStaticPayload", "", "Payload QRIS statis merchant"],
      ["buyerLibraryScriptId", "1cDP1qYyFTpPYi51pzg_quS83Vd9wCKOtkuPMCZney-GSDcGWZDLlNDIK", "Script ID Library KasPilot"],
      ["spreadsheetTemplateCopyUrl", "https://docs.google.com/spreadsheets/d/13lgynvUMOhudeD7YdQnlBiUgbjkoQipwX1ExDWcOxpY/copy", "Link copy template spreadsheet master"]
    ];
    for (var i = 0; i < defaultSettings.length; i++) {
      sheetSettings.appendRow(defaultSettings[i]);
    }
  }

  // 2. Buat Sheet Orders jika belum ada
  var sheetOrders = ss.getSheetByName("Orders");
  if (!sheetOrders) {
    sheetOrders = ss.insertSheet("Orders");
    var headers = ["Timestamp", "OrderID", "Nama Pembeli", "WhatsApp", "Email", "Metode", "Nominal", "Kode Unik", "Total Bayar", "Status Payment"];
    sheetOrders.appendRow(headers);
    sheetOrders.getRange("A1:J1").setFontWeight("bold").setBackground("#e2e8f0");
    sheetOrders.setFrozenRows(1);
  }
}

function getAdminToken() {
  var props = PropertiesService.getScriptProperties();
  var token = props.getProperty(ADMIN_TOKEN_KEY);
  if (!token) {
    props.setProperty(ADMIN_TOKEN_KEY, ADMIN_TOKEN_DEFAULT);
    token = ADMIN_TOKEN_DEFAULT;
  }
  return token;
}

function validateAdminToken(token) {
  return token === getAdminToken();
}

function getSettingsObject() {
  setupSheetsOtomatis();
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Settings");
  var data = sheet.getDataRange().getValues();
  var settings = {};
  
  // Lewati baris header ke-1
  for (var i = 1; i < data.length; i++) {
    var key = data[i][0];
    var val = data[i][1];
    if (key) {
      if (val === "true") val = true;
      else if (val === "false") val = false;
      else if (!isNaN(val) && val.toString().trim() !== "") {
        val = Number(val);
      }
      settings[key] = val;
    }
  }
  return settings;
}

function doGet(e) {
  var params = e && e.parameter ? e.parameter : {};
  var action = params.action;
  var token = params.token;
  
  try {
    setupSheetsOtomatis();
    
    // API Publik: Ambil setting website (tanpa info sensitif token)
    if (action === "getSettings") {
      var settings = getSettingsObject();
      return JSONResponse({ success: true, settings: settings });
    }
    
    // API Admin: Butuh validasi Token
    if (action === "getOrders") {
      if (!validateAdminToken(token)) {
        return JSONResponse({ success: false, message: "Unauthorized. Token tidak valid." }, 401);
      }
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var sheet = ss.getSheetByName("Orders");
      var values = sheet.getDataRange().getValues();
      var orders = [];
      
      // Ambil data (baris header diabaikan)
      for (var i = values.length - 1; i >= 1; i--) {
        orders.push({
          row: i + 1, // index baris spreadsheet asli (1-based)
          timestamp: values[i][0],
          orderId: values[i][1],
          name: values[i][2],
          whatsapp: values[i][3],
          email: values[i][4],
          method: values[i][5],
          nominal: values[i][6],
          uniqueCode: values[i][7],
          total: values[i][8],
          status: values[i][9]
        });
      }
      return JSONResponse({ success: true, orders: orders });
    }
    
    return JSONResponse({ success: false, message: "Action tidak dikenal." }, 400);
  } catch (err) {
    return JSONResponse({ success: false, message: err.toString() }, 500);
  }
}

function doPost(e) {
  var postData = "";
  try {
    setupSheetsOtomatis();
    postData = e && e.postData ? e.postData.contents : "";
    var payload = JSON.parse(postData);
    var action = payload.action;
    var token = payload.token;
    
    // 1. API Publik: Kirim pesanan baru dari checkout landing page
    if (action === "submitOrder") {
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var sheet = ss.getSheetByName("Orders");
      
      var orderId = "KP-" + Utilities.getUuid().substring(0, 8).toUpperCase();
      var rowData = [
        new Date(),
        orderId,
        payload.name || "",
        payload.whatsapp || "",
        payload.email || "",
        payload.method || "",
        Number(payload.nominal || 0),
        Number(payload.uniqueCode || 0),
        Number(payload.total || 0),
        "Baru" // default status pesanan
      ];
      
      sheet.appendRow(rowData);
      return JSONResponse({ success: true, orderId: orderId, message: "Pesanan berhasil dicatat." });
    }
    
    // 2. API Admin: Simpan setting baru dari admin panel
    if (action === "saveSettings") {
      if (!validateAdminToken(token)) {
        return JSONResponse({ success: false, message: "Unauthorized. Token tidak valid." }, 401);
      }
      var newSettings = payload.settings || {};
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var sheet = ss.getSheetByName("Settings");
      var range = sheet.getDataRange();
      var values = range.getValues();
      
      // Update baris-baris setting
      for (var key in newSettings) {
        var found = false;
        var valString = String(newSettings[key]);
        for (var i = 1; i < values.length; i++) {
          if (values[i][0] === key) {
            sheet.getRange(i + 1, 2).setValue(valString);
            found = true;
            break;
          }
        }
        // Tambahkan jika key baru
        if (!found) {
          sheet.appendRow([key, valString, "Setting kustom"]);
        }
      }
      return JSONResponse({ success: true, message: "Pengaturan berhasil diperbarui." });
    }

    // 3. API Admin: Ganti status pesanan
    if (action === "updateOrderStatus") {
      if (!validateAdminToken(token)) {
        return JSONResponse({ success: false, message: "Unauthorized. Token tidak valid." }, 401);
      }
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var sheet = ss.getSheetByName("Orders");
      var row = Number(payload.row);
      var statusBaru = payload.status || "Baru";
      
      if (!row || row < 2) {
        return JSONResponse({ success: false, message: "Baris spreadsheet tidak valid." }, 400);
      }
      
      sheet.getRange(row, 10).setValue(statusBaru); // Kolom J adalah status payment
      return JSONResponse({ success: true, message: "Status pesanan berhasil diupdate." });
    }

    // 4. API Admin: Ganti password / admin token baru
    if (action === "updateAdminToken") {
      if (!validateAdminToken(token)) {
        return JSONResponse({ success: false, message: "Unauthorized." }, 401);
      }
      var newToken = payload.newToken;
      if (!newToken || newToken.trim().length < 4) {
        return JSONResponse({ success: false, message: "Token baru minimal harus 4 karakter." }, 400);
      }
      PropertiesService.getScriptProperties().setProperty(ADMIN_TOKEN_KEY, newToken.trim());
      return JSONResponse({ success: true, message: "Token/Sandi admin berhasil diubah." });
    }
    
    return JSONResponse({ success: false, message: "Action tidak dikenal." }, 400);
  } catch (err) {
    return JSONResponse({ success: false, message: err.toString() }, 500);
  }
}

function JSONResponse(data, statusCode) {
  var output = ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
  return output;
}
