def habis_dibagi(list_angka,pemisah):
    total=0
    for angka in list_angka:
        if angka%2==0:
            total+=angka
    print(total)

habis_dibagi([1,2,3,4,5],2)