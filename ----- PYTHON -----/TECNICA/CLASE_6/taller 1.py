nums = []

print("ingresa 10 numeros aleatorios")
for i in range(10):
    num = float(input("ingresa un numero: "))
    if num % 5== 0:
        nums.append(num)

if len(nums) != 0:
    print(f"los siguientes numeros son multiplo de 5: {nums}")
else:
    print("no colocaste ningun numero multiplo de 5")
   