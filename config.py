# File: config.py
# PERINGATAN: Ini adalah contoh kode rentan untuk testing pipeline.

def connect_to_cloud():
    # ❌ BAHAYA: Menyimpan API Key atau Password secara langsung di dalam kode (Hardcoded Secret)
    # Trivy akan mendeteksi ini dan membunyikan alarm!
    
    aws_access_key_id = "AKIAIOSFODNN7EXAMPLE" 
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    db_password = "SuperSecretPassword123!"

    print("Menghubungkan ke server cloud...")
    # ... proses koneksi .....