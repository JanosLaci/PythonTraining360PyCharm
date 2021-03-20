# with nélkül: tablazatos.txt olvasasa, lista soronként
#dupla lista, dupla_tablazatos.txt kiírása


opened_txt = open('tablazatos.txt', 'r', encoding='utf-8')

list_by_readlines_method = opened_txt.readlines()
print(list_by_readlines_method)

list_by_readlines_method_without_first_line = list_by_readlines_method[1:]

tablazatos_list = []

for txt_line in list_by_readlines_method:
    print(txt_line)
    tablazatos_list.append(txt_line.split('|'))
    print(txt_line.split('|'))


opened_txt.close()
