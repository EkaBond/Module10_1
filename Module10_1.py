import time
import threading

def wite_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf8')    #создаст и откроет файл с именем, что передадим в вызове ф-ии
    for i in range(word_count):                     #переберет нужное кол-во (напр 10 - см вызов ф-ии)
        file.write(f'Какое-то слово № {i+1}\n')     #добавит строку с номером слова соответственно циклу
        time.sleep(0.1)                             #сделает паузу после каждой строки
    file.close()                                    #закроет файл
    print(f'Завершилась запись в файл {file_name}')  #в итоге выдаст строку

#ставлю режим 'w' чтобы стирал предыдущие строки, т.к. я перезапускаю код несколько раз
#в процессе написания кода, чтобы на захламить файл. для рамок данного задания это допустимо.
#ставлю для номера слова {i+1} чтобы не было слова №0, пусть отсчет будет с 1

started_at = time.time()                          #засекаем время для 4х вызовов ф-ии

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

ended_at = time.time()                              #засекаем время конца
elapsed = round(ended_at - started_at, 2)           #итого потрачено времени, округление 2 знака после запятой
print(f'работа потоков {elapsed} сек')


started_at1 = time.time()                        #засекаем время начала для потоков
#создаем потоки для ф-ии с параметрами
thread1 = threading.Thread(target=wite_words, args =(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args =(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args =(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args =(100, 'example8.txt'))

thread1.start()  #старт потока
thread2.start()
thread3.start()
thread4.start()

thread1.join()    #стоп
thread2.join()
thread3.join()
thread4.join()

ended_at1 = time.time()                           # время конца
elapsed1 = round(ended_at1 - started_at1, 2)      #итого потрачено времени, округление 2 знака после запятой
print(f'работа потоков {elapsed1} сек')

