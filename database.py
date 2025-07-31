# -*- coding: utf-8 -*-

"""
Database Sumber Daya Pembelajaran

File ini berisi data statis untuk sumber daya pembelajaran yang digunakan
oleh aplikasi Jalur Pembelajaran yang Dipersonalisasi. Untuk MVP, kami menggunakan
kamus Python sederhana untuk menyimpan data ini.

Struktur Data:
{
    "topik": {
        "modul_1": [
            {"judul": "Judul Sumber Daya 1", "tipe": "Buku", "tingkat": "Dasar"},
            ...
        ],
        ...
    }
}
"""

LEARNING_RESOURCES = {
    "python": {
        "Dasar-dasar Python": [
            {"judul": "Python for Everybody", "tipe": "Buku", "tingkat": "Dasar"},
            {"judul": "Official Python Tutorial", "tipe": "Artikel", "tingkat": "Dasar"},
        ],
        "Struktur Data dan Algoritma": [
            {"judul": "GeeksforGeeks - Data Structures", "tipe": "Artikel", "tingkat": "Menengah"},
            {"judul": "Problem Solving with Algorithms and Data Structures using Python", "tipe": "Buku", "tingkat": "Menengah"},
        ],
        "Analisis Data dengan Python": [
            {"judul": "Pandas Documentation", "tipe": "Artikel", "tingkat": "Menengah"},
            {"judul": "Python for Data Analysis by Wes McKinney", "tipe": "Buku", "tingkat": "Mahir"},
            {"judul": "Intro to Data Analysis with Python", "tipe": "Video", "tingkat": "Mahir"},
        ],
    },
    "komputasi kuantum": {
        "Pengenalan Komputasi Kuantum": [
            {"judul": "Quantum Computing for Everyone", "tipe": "Buku", "tingkat": "Dasar"},
            {"judul": "Nielsen & Chuang - Quantum Computation and Quantum Information", "tipe": "Buku", "tingkat": "Dasar"},
        ],
        "Algoritma Kuantum": [
            {"judul": "The Quantum Algorithm Zoo", "tipe": "Artikel", "tingkat": "Menengah"},
            {"judul": "Quantum Algorithms", "tipe": "Video", "tingkat": "Menengah"},
        ],
        "Implementasi Praktis": [
            {"judul": "Qiskit Documentation", "tipe": "Artikel", "tingkat": "Mahir"},
            {"judul": "Cirq Tutorial", "tipe": "Artikel", "tingkat": "Mahir"},
        ],
    }
}
