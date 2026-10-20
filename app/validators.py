"""Input validation helpers for task titles."""


def normalize_title(title: str) -> str:
    """Normalize and validate a task title."""
    if not title or not title.strip():
        raise ValueError("Judul tugas tidak boleh kosong.")
    normalized = title.strip()
    if len(normalized) > 120:
        raise ValueError("Judul tugas maksimal 120 karakter.")
    return normalized
