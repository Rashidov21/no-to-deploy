# Pythonda map() funksiyasi 

# map() - berilgan har bir ketma-ketlik elementlari 
# uchun ma'lum bir funksiyani qo'llash 

def square(num):
    return int(num) ** 2

arr = [1,2,3] # sonlarni darajalarini chiqaring

print(map(square,arr))

print(list(map(square,arr))) # [1, 4, 9]


