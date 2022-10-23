def write_file(data):
    with open('file.csv','a') as file:                       # Создание и запись нового файла
        file.writelines(data)
          
def read_file():
    with open('file.csv','r') as file:                       # чтение из файла
        return file.readlines()