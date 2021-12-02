import os
import shutil

caminho_original = r'D:\Documentos\Exames Marco'
caminho_novo = r'D:\Documentos\Exames Marco\serie'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):  # alterar os.walk(caminho_novo) para os.walk(caminho original) para
    # mover e copíar
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.pdf' in file:
            os.remove(new_file_path)
    print('Arquivo(s) apagado(s)')


"""
         if '.pdf' in file:
             shutil.copy(old_file_path, new_file_path)    # copia arquivo
             print(f'Arquivo {file} copiado com sucesso!')
   
             shutil.move(old_file_path, new_file_path)      # move arquivo
             print(f'Arquivo {file} movido com sucesso!')
"""
