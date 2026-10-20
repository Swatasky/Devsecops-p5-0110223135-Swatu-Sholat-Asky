# SecureTask API

SecureTask API adalah aplikasi Python sederhana untuk mengelola daftar tugas (menambah, melihat, memperbarui, dan menghapus tugas) melalui modul layanan.

## Teknologi
- Python 3.11
- pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk CI

## Struktur proyek
```text
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── repository.py
│   ├── service.py
│   ├── validators.py
│   └── cli.py
├── tests/
│   └── test_tasks.py
├── scripts/
│   └── quality_gate.py
├── .github/workflows/
│   └── devsecops.yml
└── requirements.txt
```

## Cara menjalankan
Pastikan Python 3.11 atau lebih baru telah terpasang.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m app.cli
```

## Menjalankan pengujian
```bash
pytest -q
```

## Overview pipeline DevSecOps
Workflow `.github/workflows/devsecops.yml` berjalan ketika ada `push` ke branch `main` atau `pull_request` menuju `main`. Job `build` memasang dependensi dan menjalankan unit test. Setelah job `build` berhasil, job `sast-scan` menjalankan Bandit untuk memeriksa pola kode Python yang berisiko. Skrip Quality Gate membaca laporan JSON Bandit dan menggagalkan pipeline jika ada temuan dengan severity **High**. Dengan demikian, perubahan yang melewati pipeline harus lolos pengujian dan aturan keamanan yang ditentukan.
