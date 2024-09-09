#1
cortege=(0,1,2,3)
print(cortege[1],end='\n\n')

#2
str=input('Введите строку: ')
print(len(str),end='\n\n')

#3
print({'name':'Egor','age':19,'class':3},end='\n\n')

#4
print([w for w in range(1,11)],end='\n\n')

#5
sum([1,2,3])

#6
my_set={1,2,3,4,5}
print(my_set.add(6),end='\n\n')

#7
num=int(input("Введите целое число: "))
print(num**2,end='\n\n')

#8
fruit_colors={"яблоко":"красный","банан":"желтый","виноград":"фиолетовый","апельсин":"оранжевый","киви":"зеленый"}
for w in fruit_colors.keys():print(w)
print()

#9
def reverse_string(s):return s[::-1]

#10
string_list=["первая","вторая","третья","четвертая","пятая"]
string_list[2]="новая третья"

#11
mixed_tuple=(1,"строка",3.14,True,None,[1,2,3])
for element in mixed_tuple:print(f"Тип элемента {element}: {type(element)}")
print()

#12
num1=int(input("Введите первое число: "))
num2=int(input("Введите второе число: "))
print(num1*num2,end='\n\n')

#13
book_info = {"автор":"Достоевский","название":"Преступление и наказание","год издания":1866}
for key,value in book_info.items():print(f"{key}: {value}")
print()

#14
cities_set={"Москва","Париж","Нью-Йорк","Токио","Лондон"}
cities_set.remove("Нью-Йорк")
print(cities_set,end='\n\n')

#15
def max_from_list(n):return max(n)

#16
print([n for n in list(range(1,21)) if n%2==0],end='\n\n')

#17
input_string=input("Введите строку: ")
is_palindrome=input_string==input_string[::-1]
print(is_palindrome,end='\n\n')

#18
mixed_tuple=(42,"текст",3.14)
a,b,c=mixed_tuple
print(a,b,c,end='\n\n')

#19
def print_student_info(student):
    for key,value in student.items():print(f"{key}: {value}")
print()

#20
my_list=[]
my_list+=[1,"строка",True,3.14,None]
print(my_list,end='\n\n')
