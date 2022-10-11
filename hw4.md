# Бизнес сценарий

Использовать распределённую базу данных для хранения изображений предметов гардероба.

Засчёт базы данных хочется сделать хранилище изображений более удобным в плане интерфейса, устойчивым к падению серверов и переиспользуемым в других сервисах.

## Рассмотренные варианты баз данных

- **Redis**

  Из преимуществ, быстрый доступ к данным и расширяемость. 
  
  Есть возможность сохранять снапшоты состояния базы данных через определённые интервалы времени. 

- **PostgreSQL**

  Эта база данных имеет более сильные гарантии восстановления данных после отказов. Состояние базы данных можно восстановить после каждой успешной транзакции.

  К тому же реляционная модель более удобна для запроса картинок по определённым признакам (тип одежды или сезон).

  Скорость доступа к данным ниже, чем у Redis.

- **MongoDB**

  Тоже имеет сильные гарантии восстановления, но уступает Redis по скорости.

  Есть возможнось хранить бинарные файлы как поля формата BSON. В тот же формат можно записать дополнтельную информацию, по которой удобно искать картинки, подходящие под запрос.


Я думаю, что лучше всего будет хранить картинки в Redis из-за высокой скорости и простоты использования. Данные в базе данных обновляются не часто, так что снапшоты достаточно делать изредка. Структура данных довольно простая, так что нет большого преимущетва в использовании файловой структуры MongoDB или реляционной PostgreSQL.

