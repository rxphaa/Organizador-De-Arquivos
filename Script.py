from pathlib import Path 
import shutil
import os
import re



pasta_atual = Path(__file__).parent


for arquivo in pasta_atual.glob('*'):
    if arquivo.is_file():

        resultado = re.search(r"(.*)[. ]S(\d+)", str(arquivo.name))

        if resultado:   
            nome = resultado.group(1)
            temporada = resultado.group(2)


            nome_corrigido = nome.replace(".", " ")


            nome_pasta = nome_corrigido

            nome_subpasta = 'Temporada ' + temporada.zfill((2))
            caminho_pasta_destino = pasta_atual / nome_pasta / nome_subpasta

            caminho_pasta_destino.mkdir(parents=True, exist_ok= True)
                
            arquivo_destino = caminho_pasta_destino / arquivo.name

            if arquivo_destino.exists():
                print(f"O Arquivo : {arquivo.name} ja exite na pasta final")
            else:
                shutil.move(arquivo, caminho_pasta_destino)


            print(nome_corrigido)
            print(temporada)














#Pega a pasta atual do arquivo .py

# se o resultado for true, salvo a variavel nome e a temporada, depois aplico a correção no nome e crio a pasta destino dos arquivos.

#informa o caminho do arquivo
#camiho_arquivo = pasta_atual / 'Chicago.Fire.S4E08.1080p.WEB.h264-ETHEL[EZTVx.to].mkv'


#regex
#resultado = re.search(r"(.*)\.S(\d+)", str(camiho_arquivo.name))
