file = open('C:/Users/Esther/OneDrive/Projetos/Bootcamp-python_backend/06-Manipulando_arquivos_em_Python/arquivo.txt', "w")

texto_write = "What is Lorem Ipsum?\n Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

texto_writeLines = ['It ', 'has ', 'survived ', 'not ', 'only', 'five ', 'centuries, ', 'but ', 'also ', 'the ', 'leap ', 'into ', 'electronic ', 'typesetting, ', 'remaining ', 'essentially ', 'unchanged. ', 'It ', 'was ', 'popularised ', 'in ', 'the ', '1960s ', 'with ', 'the ', 'release ', 'of ', 'Letraset ', 'sheets ', 'containing ', 'Lorem ', 'Ipsum ', 'passages, ', 'and ', 'more ', 'recently ', 'with ', 'desktop ', 'publishing ', 'software ', 'like ', 'Aldus ', 'PageMaker ', 'including ', 'versions ', 'of ', 'Lorem ', 'Ipsum.']

file.write(texto_write)
file.writelines(texto_writeLines)

file.close()
