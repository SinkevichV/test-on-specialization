
def input_data(n):
    data = input(n)
    return data

def cust_rec(id, f_name, l_name, Phone, Service, cost, date):
    rec = (' | ').join((id, f_name, l_name, Phone, Service, cost, date))
    with open("cust_rec.csv", "a", encoding="utf-8") as rec_data:
        rec_data.write(f'{rec} \n')
    print(rec)

def service_lst(id, name, cost):
    serv = (' | ').join((id, name, cost))
    with open("service.csv", "a", encoding="utf-8") as serv_data:
        serv_data.write(f'{serv} \n')
    print(serv)

def creat_staff(id, f_name, l_name, Phone, Service):
    staff = (' | ').join((id, f_name, l_name, Phone, Service))
    with open("staff.csv", "a", encoding="utf-8") as staff_data:
        staff_data.write(f'{staff} \n')
    print(staff)

def search_data(name):
    print('Введите значения для поиска: ')
    sc_data = input('')
    with open(f"{name}.csv", "r", encoding="utf-8") as file:
        text = file.readlines()
        for line in text:
            list_txt = line.rstrip("\n").split(" ")
            for s in list_txt:
                if s == sc_data:
                    print(line)
        else:
            print("Значение не найдено")


def edit_data(name):
    with open(f"{name}.csv", "r", encoding="utf-8") as file:
        view_file = file.read()
        word = input('Введите значение, которое нужно отредактировать: ')
        edit_word = input('Введите отредактированное значение: ')
        edit_text = view_file.replace(f"{word}", f"{edit_word}", 1)
    with open(f"{name}.csv", "w", encoding="utf-8") as file:
        file.write(f'{edit_text} \n')    


def delete_data(name):
    with open(f"{name}.csv", "r", encoding="utf-8") as file:
        list_lines = []
        for n, line in enumerate(file, start=0):
            print(n, line, end= '')
            list_lines.append(line)
        print()
        del list_lines[int(input('Введите номер строки, которую необходимо удалить: '))]
        str_file = (''.join(map(str, list_lines)))
    with open(f"{name}.csv", "w", encoding="utf-8") as file:
        file.write(f'{str_file} \n')    
        print(str_file)


                
def view_data(name):    
    with open(f"{name}.csv", "r", encoding="utf-8") as file:
        view_file = file.read()
        print(view_file)    


           
        
# delete_data('staff')
# edit_data('staff')
# view_data('')  
# search_data()
# creat_staff(input_data(), input_data(), input_data(), input_data(), input_data())