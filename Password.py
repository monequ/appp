from random import randint

choice =int(input("Введите длинну пароля"))

    

password =""

spec_ch= False
if choice>5:
    spec_ch= False
    print("Ошибка")
    exit(0)

for i in range(choice):
    if spec_ch == True:
        password += chr(randint(48,57))
    else:
        if randint(1,2)==1:
            password += chr(randint(48,57)) 
        else:
            password += chr(randint(48,57))
        
    


print("Сгенерированный пароль:", password)
