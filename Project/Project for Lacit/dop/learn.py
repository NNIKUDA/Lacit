"""

Сервис для обучения модели методом k ближайших соседей

"""

from fastapi import FastAPI                        # реализация сервера
from pydantic import BaseModel                     # проверка исполнения аннотаций
from typing import List                             # тип данных используемый для аннотаций
import uvicorn                                      # запуск FastAPI сервера
from uuid import uuid1                              # генерация имен соделий
import joblib                                       # сохранение модели в файловой системе
from sklearn.neighbors import KNeighborsClassifier  # модель которую будем обучать


class ModelSamples(BaseModel):
  """
  Класс хранящий параметры запроса
  """

  x: List[List[float]]
  y: List[float]

app= FastAPI()

@app.post("/")
def train_model(samples):


  for i in samples.x[0]:
    if (-1.0>i or i>1.0):
      return 'Неправельный формат данных'
  for i in samples.x[1]:
    if (-1.0>i or i>1.0):
      return 'Неправельный формат данных'
  for i in samples.y:
    if i!=0 and i!=1 and i!=2:
      return 'Неправельный формат данных'

  name = str(uuid1())
  model = KNeighborsClassifier(n_neighbors=2)
  model.fit(samples.x, samples.y)

  try:
    with open(r'models\models.txt', 'a') as filewithmodels:
      filewithmodels.write(name+' \n')
      joblib.dump(model, 'models/' + name)
    return 'OK'
  except IOError :
    return 'Файл models недоступен'


if __name__ == '__main__':

  dictconst={}
  try:
    with open('dop\config.txt', 'tr')as config:
      const = config.readlines()
      for note in const:
        value = note.split(' ')
        dictconst[value[0]] = value[1]
  except IOError as e:
    print('Файл config.txt недоступен, команда List не может работать коректно')
  uvicorn.run('learn:app', port=int(dictconst['PORTFORLEARN']))