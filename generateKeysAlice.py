from Crypto.PublicKey import RSA
import os
#import generateKeysBob
from config import chaves_alice, chaves_bob

    #Gerando um par de chaves RSA
def gerar_par_chaves_alice(bits=2048): #Tamanho da chave de acordo com a descrição do trabalho
    
    chave = RSA.generate(bits)
    chave_publica = chave.publickey().export_key() #Formato PEM (Privacy-Enhanced Mail) para armazenar a chave
    chave_privada = chave.export_key() #Formato PEM (Privacy-Enhanced Mail) para armazenar a chave

    return chave_publica, chave_privada

# Geração das chaves para Alice
chave_publica_alice, chave_privada_alice = gerar_par_chaves_alice()
    
  
# Aqui é aonde as chaves serão armazenadas
chaves_alice = "chaves_alice"

# Cria a pasta das chaves
if not os.path.exists(chaves_alice):
    os.makedirs(chaves_alice)


# Caminho completo do arquivo
salvar_chave_publica = os.path.join(chaves_alice, "chave_publica_alice.pem")
salvar_chave_publica_alice_pasta_bob = os.path.join(chaves_bob, "chave_publica_alice.pem")
salvar_chave_privada = os.path.join(chaves_alice, "chave_privada_alice.pem")

# Verifica se a pasta existe e tentar salvar o arquivo
if os.path.exists(chaves_alice):
    try:
        with open(salvar_chave_publica, 'wb') as k:
            k.write(chave_publica_alice)
        with open(salvar_chave_privada, 'wb') as k:
            k.write(chave_privada_alice)
        with open(salvar_chave_publica_alice_pasta_bob, 'wb') as k:
            k.write(chave_publica_alice)
        print(f"Chaves salvas em: {chaves_alice}")
    except IOError:
        print(f"Erro ao salvar a chave pública de Bob, execute o arquivo de geração de Bob, depois repita o processo: {IOError}")
else:
    print(f"A pasta {chaves_alice} não existe.")