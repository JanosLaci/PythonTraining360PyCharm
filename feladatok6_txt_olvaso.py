#tablazatos.txt olvasasa, lista soronként
#dupla lista, dupla_tablazatos.txt kiírása

with open('tablazatos.txt', 'r', encoding='utf-8') as opened_txt:
    print(opened_txt.readlines())

