import platform
import subprocess

import chardet
from chardet.universaldetector import UniversalDetector

"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""
import ast

data = {
    "разработка": "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430",
    "сокет ": "\u0441\u043e\u043a\u0435\u0442",
    "декоратор": "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440",
}

for key, val in data.items():
    print(f"{key} ===> {type(key)}\n{val} ===> {type(val)}")

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""
print("-" * 30, "\n")
words = "class, function, method"

for word in words.split(", "):
    byte = ast.literal_eval(f'b"{word}"')
    print(f"{byte} ===> {type(byte)}\nlength ===> {len(byte)}")

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. Важно:
решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

print("-" * 30, "\n")

words = "attribute, класс, функция, type"

for word in words.split(", "):
    try:
        bytes(word, "ascii")
        print(f"Слово {word} возможно записать в байтовом типе.")
    except:
        print(f"{word} невозможно записать в байтовом типе.")

"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

print("-" * 30, "\n")

words = "разработка, администрирование, protocol, standard"

for word in words.split(", "):
    str_to_byte = word.encode("utf-8")
    print(f"{type(str_to_byte)} ===> {str_to_byte}")

    byte_to_str = str_to_byte.decode("utf-8")
    print(f"{type(byte_to_str)} ===> {byte_to_str}")

"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
кириллице.
"""

param = "-n" if platform.system().lower() == "windows" else "-c"
urls = "yandex.ru, yuotube.com"

for url in urls.split(", "):
    args = ["ping", param, "4", url]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        res = chardet.detect(line)
        print(res)
        decode_line = line.decode(res["encoding"]).encode("utf-8")
        print(decode_line.decode("utf-8"))

"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в
неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

txt = "сетевое программирование, сокет, декоратор"
with open("txt.txt", "w") as f:
    for word in txt.split(", "):
        f.write(f"{word},")
f.close()

detector = UniversalDetector()
with open("txt.txt", "rb") as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
code = detector.result["encoding"]

with open("txt.txt", "r", encoding=code) as f:
    print(f.read())
