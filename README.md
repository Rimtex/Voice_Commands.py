# Voice_Commands.py

голосовой ассистент умеющий делать всякие штуки `голосовыми` командами  
со встроенной локальной нейросетью для `одноразовых запросов` пока что без режима чата

# Основные требования
1. https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip - в эту же папку  
2. http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin            - в папку - \pygpt4all\pygpt4all\models

### для запуска файлов голосом   
* создаём папку - **ярлыки** 
* копируем файл   
* вставляем ярлык в папку **ярлыки**                
* переименовываем ярлык в нужное `слово`     
* если цикл распознал только одно `слово`
* запускаем его устно этим `слово`м 
* также можно запускать ярлыки адресов браузера

#### по-умолчанию нажатый Caps Lock записывает `голос` в курсор и выключает Caps Lock

* **Voice_Commands.py**
  * **config.py**               переменные адресов для файлов
  * **English_trans_writer.py** `согласен` для голосового общения с языковой моделью 
  * **converter.py**            `покажи` преобразователь для показа команд
  * **loader.py**               для генерации всяких вещей
  * **vocabulary.py**           словарь ассистента
  * **Coloring.py**             просто напоминалка для всяких вещей 
  * **Model_writer.py**         для теста моделей распознования голоса
  * **Tester_models.py**        для теста языковых моделей 
  * **Tester.py**               для теста функций 
  * **mouse.py**                для теста мышиных функций
