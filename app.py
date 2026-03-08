# File: app.py
def connect_to_server():
    # Satpam akan mendeteksi kunci palsu ini dan membunyikan alarm
    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA3Tz2mr7SZiAMfQyA2X8Zz1... 
-----END RSA PRIVATE KEY-----"""
    print("Mencoba koneksi...")