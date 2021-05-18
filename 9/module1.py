

import csv

class DATABASE:
    def __init__(self):
        self.database={}
    def addnewrecord(self,name,phone):
        if phone not in self.database:
            self.database[phone]=name
        else:
            print(f'Данный {phone} номер уже есть в ,базе данных ')
    def loaddata(self,filename):
        try:
            with open(filename,'r') as file:
                reader=csv.reader(file)
                flag=0
                for i in reader:
                    if flag:
                        self.addnewrecord(i[1],i[0])
                    else:
                        flag+=1

        except FileNotFoundError as e:
            print(f"Файл {filename} не найден ")
base=DATABASE()



