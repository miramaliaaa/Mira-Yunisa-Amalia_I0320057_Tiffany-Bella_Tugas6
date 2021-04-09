def tugas6(i):
    if i % 2 == 0 or i % 3 == 0:
        print(i, 'bukan prima')

    else:
        print(i, 'adalah bilangan prima')


for i in range(10, 25):
    tugas6(i)