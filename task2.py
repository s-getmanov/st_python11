# Ссылка на github
#https://github.com/s-getmanov/st_python11.git

pets = {}

#Функция определяет набор команд и их обработчики.
def commands():
    commands = {"stop":{},             
            "create":{"handler":hendler_create},            
            "read"  :{"handler":hendler_read},
            "update":{"handler":hendler_update},
            "delete":{"handler":hendler_delete},
            "list" :{"handler":hendler_pets_list},
            }
    return commands

def get_suffix(age):
    if age % 10 == 1 and age != 11:
                return 'год'
    elif 2 <= age % 10 <= 4 and not (12 <= age <= 14):
                return'года'
    else:
                return'лет'
    
#Конструктор нового питомца. Возвращает новый ID
def new_pet(name):
    #Ключи у нас числовые, поэтому максимальный ключ можно вычислить простой функцией МАХ
    current_max_id = 0
    #проверим что pets не пустой, иначе будет ошибка
    if pets:
        current_max_id = max(pets)
    new_id = current_max_id + 1
    pet = {           
            name:{
                "Вид питомца":"",
                "Имя владельца":"",
                "Возраст питомца":"",
            }            
        }
    pets[new_id] = pet
    return new_id

#Функции работы с данными
def get_pet_by_id(id):
    if id in pets:
        return pets[id]
    return False

def get_pet_name(pet):
    if pet:
        return next(iter(pet.keys()))
    return False

def get_pet_data(pet):
    if pet:       
        return next(iter(pet.values()))
    return False

def input_pet_data(id):
    current_pet = get_pet_by_id(id)

    if not current_pet:
        print(f"Не найден питомец с ID {id}")
        return       
     
    current_pet_data = get_pet_data(current_pet) 
    
    tek_data = f"(текущий - {current_pet_data['Вид питомца']})" if not current_pet_data['Вид питомца'] == "" else ""
    input_data = input(f"Введите вид питомца {tek_data}:")
    if not input_data == "":
        current_pet_data["Вид питомца"] = input_data

    tek_data = f"(текущее - {current_pet_data['Имя владельца']})" if not current_pet_data['Имя владельца'] == "" else ""
    input_data = input(f"Имя владельца {tek_data}:")
    if not input_data == "":
        current_pet_data["Имя владельца"] = input_data

    tek_data = f"(текущий - {current_pet_data['Возраст питомца']})" if not current_pet_data['Возраст питомца'] == "" else ""
    input_data = input(f"Возраст питомца {tek_data}:")
    if not input_data == "":
        current_pet_data["Возраст питомца"] = int(input_data)  

def print_pet(id):   
    current_pet = get_pet_by_id(id)

    if not current_pet:
        print(f"Не найден питомец с ID {id}")
        return
    
    current_pet_data = get_pet_data(current_pet)
    suffix = get_suffix(current_pet_data['Возраст питомца'])

    print(f"{id}. Это {current_pet_data['Вид питомца']} по кличке '{get_pet_name(current_pet)}'. Возраст питомца: {current_pet_data['Возраст питомца']} {suffix}. Имя владельца: {current_pet_data['Имя владельца']}")

#Обработчики команд
def hendler_create(): 
    name = ""
    while name == "":
        name = input("Введите имя питомца:")

    new_pet_id = new_pet(name)
    input_pet_data(new_pet_id)   

def hendler_read():
    pet_id = 0
    while pet_id == 0:
        pet_id = int(input("Введите ID питомца:"))
    print_pet(pet_id)

def hendler_update():
    pet_id = 0
    while pet_id == 0:
        pet_id = int(input("Введите ID питомца:"))
    input_pet_data(pet_id)     

def hendler_delete():
    pet_id = 0
    while pet_id == 0:
        pet_id = int(input("Введите ID питомца:"))
    res = pets.pop(pet_id, False)
    if res:
        print(f"Успешно удален питомец с ID '{pet_id}'")
    else:   
        print(f"Питомца с ID '{pet_id}' нет в базе !")

def hendler_pets_list():
    for k in pets:
        print_pet(k)        

#Роутер. Обрабатывает команды. При вводе команды stop возвращает ложь для завершение цикла обработки команд.
def route_commands(commands):    
    command = input(f"Введите команду(доступные команды {list(commands)}):")

    if not command in commands:
        print("Неверная команда!")
        return True
    
    if command == "stop":
        return False
    
    commands[command]["handler"]()

    return True
    
#Запустим безконечный цикл для ввода команд.  
while route_commands(commands()):
    pass
print("Работа программы зевершена!")

