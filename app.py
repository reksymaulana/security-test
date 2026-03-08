import os

def connect_to_server():
    # ✅ CLEAN: Kunci diambil dari brankas sistem, bukan ditulis langsung di kode
    private_key = os.getenv("SERVER_PRIVATE_KEY")
    print("Mencoba koneksi dengan aman...")