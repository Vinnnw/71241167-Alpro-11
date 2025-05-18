email_counts = dict()
filenya = "mbox-short.txt"

try:
    with open(filenya) as fhand:
        for line in fhand:
            line = line.strip()
            if line.startswith("From "):
                parts = line.split()
                if len(parts) > 1:
                    email = parts[1]
                    email_counts[email] = email_counts.get(email, 0) + 1

    print(email_counts)

except FileNotFoundError:
    print("File tidak ditemukan:", filenya)
