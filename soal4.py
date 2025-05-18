nama_file = "mbox-short.txt"
jumlah_domain = {}

try:
    with open(nama_file) as fhand:
        for baris in fhand:
            if baris.startswith("From "):
                email = baris.split()[1]
                domain = email.split('@')[1]
                jumlah_domain[domain] = jumlah_domain.get(domain, 0) + 1
    print(jumlah_domain)

except FileNotFoundError:
    print("File tidak ditemukan:", nama_file)
