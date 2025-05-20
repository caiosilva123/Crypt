import os
from cryptography.fernet import Fernet
import argparse
from pathlib import Path

def generate_key():
      
    pwd = Path(__file__).parent / "key.key"
    if pwd.exists():
        print(f'Chave ja Existente [{pwd.read_text()}]')
        return pwd
    else:
        key = Fernet.generate_key()
        with open(pwd,"wb") as k:
            k.write(key)
        print(f'Chave Gerada com Sucesso !! [{key.decode()}]')
        return key


def encrypt_file(path_arq:Path, fernet:Fernet):

    with open(path_arq,"rb") as a:
        dados = a.read()
    
    encrypted = fernet.encrypt(dados)

    with open(path_arq+".enc", "wb") as a:
        a.write(encrypted)
       

    print(f'Arquivo [{path_arq}] Criptografado !')
    



#if __file__=="__main__":
#generate_key()
key = (Path(__file__).parent / "key.key").read_bytes()

keyObj = Fernet(key)
encrypt_file("C:\\Users\\USER\Desktop\\Nova pasta\Crypt\\requeriments.txt",keyObj)

