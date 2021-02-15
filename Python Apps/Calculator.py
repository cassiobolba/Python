# My Calcultor
print(
"********************* CALCUALTOR ***************\n"
"Select the operation you want to perform:\n"
"1 - Sum\n"
"2 - Subtraction\n"
"3 - Multiply\n"
"4 - Division\n"
)

oper = input("Select an option(1/2/3/4):")
num_1 = input("Type first number:")
num_2 = input("Type second number:")


if int(oper) == 1:
    result = int(num_1)+int(num_2)
    print(f"{num_1} + {num_2} = "+str(result))
elif int(oper) == 2:
    result = int(num_1)-int(num_2)
    print(f"{num_1} + {num_2} = "+str(result))
elif int(oper) == 3:
    result = int(num_1)*int(num_2)
    print(f"{num_1} + {num_2} = "+str(result))
elif int(oper) == 4:
    result = int(num_1)/int(num_2)
    print(f"{num_1} + {num_2} = "+str(result))
else:
    print("No such operation!")






