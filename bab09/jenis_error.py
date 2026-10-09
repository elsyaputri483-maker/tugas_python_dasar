# Mendemonstrasikan 8 jenis error yang sering muncul (ditangkap agar program tidak berhenti)
contoh = {
    "SyntaxError":       'print("hai"',
    "IndentationError":  "if True:\nprint(1)",
    "NameError":         "print(skor_x)",
    "TypeError":         '"5" + 3',
    "ValueError":        'int("abc")',
    "ZeroDivisionError": "10 / 0",
    "IndexError":        "[1, 2][5]",
    "KeyError":          '{"a": 1}["b"]',
}

for nama, kode in contoh.items():
    try:
        exec(kode)
    except Exception as e:
        print(f"{nama:<18} -> {type(e).__name__}: {e}")
