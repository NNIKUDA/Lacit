"""

Сервис для применения обученой модели методом k ближайших соседий

"""

from fastapi import FastAPI         # реализация сервера
from pydantic import BaseModel      # проверка исполнения аннотаций
from typing import List             # тип данных используемый для аннотаций
import uvicorn                      # запуск FastAPI сервера
import joblib                       # загрузка модели из файловой системы


class BatchModel(BaseModel):
  "Параметры запроса"
  id: str
  x: List[List[float]]

app = FastAPI()

@app.post("/")
def train_model(id_and_x : BatchModel):
  "Обработка запроса"
  model = joblib.load('models/' + id_and_x.id)
  result = model.predict(id_and_x.x)
  return {'y': list(result)}


if __name__ == '__main__':
  dictconst = {}
  try:
    with open('dop\config.txt', 'tr')as config:
      const = config.readlines()
      for note in const:
        value = note.split(' ')
        dictconst[value[0]] = value[1]
  except IOError as e:
    print('Файл config.txt недоступен, команда List не может работать коректно')
  uvicorn.run('apply:app', port=int(dictconst['PORTFORAPPLY']))