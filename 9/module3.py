import types,json,module1 as m1
oldfun=m1.base.loaddata
def newload(self,filename):
    if "csv" in filename:
        oldfun(filename)
    elif "json" in filename:
        try:
            with open(filename,'r') as file:

                reader=json.load(file)

                dict = []
                for section, section2 in reader.items():
                    for d in section2:
                        for i in d.values():
                            dict.append(i)
                        phone=dict.pop()
                        name=dict.pop()
                        self.addnewrecord(phone,name)




        except FileNotFoundError as e:
            print(f"Файл {filename} не найден ")
    else:
        print(f'Класс не подерживает формат {type}')

m1.base.loaddata=types.MethodType(newload,m1.base)
m1.base.loaddata('names,phones.json')
print(m1.base.database)

