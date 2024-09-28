from Crypto.PublicKey import RSA
import os
#import generateKeysAlice
from config import chaves_bob, chaves_alice

    #Gera um par de chaves RSA 
def gerar_par_chaves_bob(bits=2048): #Tamanho da chave de acordo com a descrição do trabalho
    
    chave = RSA.generate(bits)
    chave_publica = chave.publickey().export_key() #Formato PEM (Privacy-Enhanced Mail) para armazenar a chave
    chave_privada = chave.export_key() #Formato PEM (Privacy-Enhanced Mail) para armazenar a chave

    return chave_publica, chave_privada

# Geração das chaves para Bob
chave_publica_bob, chave_privada_bob = gerar_par_chaves_bob()
    
  
# Aqui é aonde as chaves serão armazenadas
chaves_bob = "chaves_bob"

# Cria a pasta das chaves
if not os.path.exists(chaves_bob):
    os.makedirs(chaves_bob)

# Caminho completo do arquivo
salvar_chave_publica = os.path.join(chaves_bob, "chave_publica_bob.pem")
salvar_chave_publica_bob_pasta_alice = os.path.join(chaves_alice, "chave_publica_bob.pem")
salvar_chave_privada = os.path.join(chaves_bob, "chave_privada_bob.pem")

# Verifica se a pasta existe e tentar salvar o arquivo
if os.path.exists(chaves_bob):
    try:
        with open(salvar_chave_publica, 'wb') as k:
            k.write(chave_publica_bob)
        with open(salvar_chave_privada, 'wb') as k:
            k.write(chave_privada_bob)
        with open(salvar_chave_publica_bob_pasta_alice, 'wb') as k:
            k.write(chave_publica_bob)
        print(f"Chaves salvas em: {chaves_bob}")
    except IOError:
        print(f"Erro ao salvar a chave pública de Alice, execute o arquivo de geração de Alice, depois repita o processo: {IOError}")
else:
    print(f"A pasta {chaves_bob} não existe.")