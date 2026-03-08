# ❌ VULN: Menyimpan rahasia langsung di dalam teks kode (Hardcoded Secret)
#Test
def connect_to_server():
    private_key = """-----BEGIN RSA PRIVATE KEY-----
    MIIEpQIBAAKCAQEA3Tz2mr7SZiAMfQyA2X8Zz1... (kode rahasia palsu) ...
    -----END RSA PRIVATE KEY-----"""
    
    print("Menghubungkan ke server menggunakan kunci rahasia...")
    # Proses koneksi...

connect_to_server()
