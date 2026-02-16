# エンコード

"あ".encode()
"い".encode()

b'\xe3\x81\x84'.decode()
b'\xe3\x81\x86'.decode()


"あ".encode(encoding="shift-jis")

"あい".encode()
b'\xe3\x81\x82\xe3\x81\x84'.decode(encoding="shift-jis")


# cord point
ord("あ")
chr(128576)