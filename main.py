# -*- coding: utf-8 -*-

"""
Aplikasi Jalur Pembelajaran yang Dipersonalisasi

Aplikasi baris perintah ini memungkinkan pengguna untuk memasukkan tujuan pembelajaran
dan menghasilkan kurikulum terstruktur berdasarkan tujuan tersebut.
"""

from database import LEARNING_RESOURCES

def generate_curriculum(tujuan):
    """
    Menghasilkan kurikulum berdasarkan tujuan pembelajaran pengguna.

    Args:
        tujuan (str): Tujuan pembelajaran yang dimasukkan oleh pengguna.

    Returns:
        dict: Kurikulum yang berisi modul dan sumber daya, atau None jika tidak ada topik yang cocok.
    """
    tujuan_lower = tujuan.lower()
    for topik, kurikulum in LEARNING_RESOURCES.items():
        if topik in tujuan_lower:
            return kurikulum
    return None

def display_curriculum(kurikulum):
    """
    Menampilkan kurikulum yang terstruktur kepada pengguna.

    Args:
        kurikulum (dict): Kurikulum yang akan ditampilkan.
    """
    print("\nBerikut adalah jalur pembelajaran yang dipersonalisasi untuk Anda:")

    # Menentukan urutan tingkat kesulitan
    tingkat_urutan = {"Dasar": 0, "Menengah": 1, "Mahir": 2}

    for i, (modul, sumber_daya) in enumerate(kurikulum.items(), 1):
        print(f"\n--- Modul {i}: {modul} ---")

        # Mengurutkan sumber daya berdasarkan tingkat kesulitan
        sumber_daya_urut = sorted(sumber_daya, key=lambda x: tingkat_urutan.get(x["tingkat"], 99))

        for s in sumber_daya_urut:
            print(f"- [{s['tipe']}] {s['judul']} ({s['tingkat']})")

def main():
    """
    Fungsi utama untuk menjalankan aplikasi jalur pembelajaran.
    """
    print("Selamat Datang di Generator Jalur Pembelajaran yang Dipersonalisasi!")

    # Meminta input dari pengguna
    tujuan_pembelajaran = input("Silakan masukkan tujuan pembelajaran Anda (misalnya, 'belajar Python untuk analisis data'): ")

    print(f"\nTerima kasih! Kami akan membuat jalur pembelajaran untuk tujuan: \"{tujuan_pembelajaran}\"")

    # Menghasilkan kurikulum
    kurikulum = generate_curriculum(tujuan_pembelajaran)

    if kurikulum:
        display_curriculum(kurikulum)
    else:
        print("\nMaaf, kami tidak dapat menemukan jalur pembelajaran yang cocok untuk tujuan Anda.")

if __name__ == "__main__":
    main()
