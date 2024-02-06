# Pythonda list.sort() va sorted() metodlari haqida 

# arr = [2.3,3,4.2,5,1,6]
# # oddiy saralash - alfavit yoki raqamlar orqali
# arr.sort()
# print(arr)

# # saralangan elementlarni teskari qilish
# arr.sort(reverse=True)
# print(arr)

# sorted faqat list emas balki istalgan iteratorni 
# saralay oladi
# sorted_data = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
# print(sorted_data)

# sorted_data = sorted("This is a test string from Andrew".split(), 
#                      key=str.lower)
# print(sorted_data)

# sorted uchun key parametri namunasi
student_points = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
sorted_student_points = sorted(student_points, 
                               key=lambda student: student[2])
print(sorted_student_points)