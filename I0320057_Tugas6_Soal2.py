print("==Nilai rata-rata==")

n = int(input("\nBanyaknyaa nilai : "))

data = []
jml = 0

for i in range(0, n):
    nilai = int(input("Masukkan nilai ke-%d: " % (i+1)))
    data.append(nilai)
    jml += data[i]
    rr = jml / n
print("\nNilai rata-rata anda :  %f" % rr)