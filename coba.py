# class Kalkulator:
#     def __init__(self, angka1, angka2):
#         self.angka1 = angka1
#         self.angka2 = angka2
        
#     def penjumlahan(self):
#         hasil = self.angka1 + self.angka2
#         return hasil
    
#     def perkalian(self):
#         hasil = self.angka1 * self.angka2
#         return hasil
    
#     def pembagian(self):
#         hasil = self.angka1 / self.angka2
#         return hasil
    
#     def pengurangan(self):
#         hasil = self.angka1 - self.angka2
#         return hasil
    
#     def pangkat(self):
#         hasil = self.angka1 ** self.angka2
#         return hasil


# pilihan =  int(input("Pilih Operasi (1-5): "))

# print("Pilih operasi 1 - 5: ")
# print("1. Penjumlahan")
# print("2. Pengurangan")
# print("3. Perkalian")
# print("4. pembagian")
# print("5. pangkat")


# angka1 = float(input("Masukan angka pertama: "))
# angka2 = float(input("Masukan angka kedua: "))


# kalkulator = Kalkulator(angka1, angka2)



# if pilihan == 1:
#     hasil = kalkulator.penjumlahan()
#     print("Hasil Penjumlahan", hasil)
# elif pilihan == 2:
#     hasil = kalkulator.pengurangan()
#     print("Hasil Pengurangan", hasil)
# elif pilihan == 3:
#     hasil = kalkulator.perkalian()
#     print("Hasil Perkalihan", hasil)
# elif pilihan == 4:
#     hasil = kalkulator.pembagian()
#     print("Hasil Pembagian", hasil)
# elif pilihan == 5:
#     hasil = kalkulator.pangkat()
#     print("Hasil Pangkat", hasil)
# else:
#     print("Salah")

def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

print(first(5))
        


