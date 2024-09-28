from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os
from BobAuthenticity import ler_arquivo

# Caminho para o arquivo cifrado e a chave privada
arquivo_cifrado = os.path.join('chaves_bob', 'texto_cifrado.bin')
caminho_chave_privada_bob = os.path.join('chaves_bob', 'chave_privada_bob.pem')

# Ler o arquivo cifrado
mensagem_cifrada = ler_arquivo(arquivo_cifrado, 'rb')

if mensagem_cifrada:
    # Carregar a chave privada de Bob
    with open(caminho_chave_privada_bob, 'rb') as key_file:
        chave_privada = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    try:
        # Decifrar a mensagem
        mensagem_decifrada = chave_privada.decrypt(
            mensagem_cifrada,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Exibir a mensagem decifrada no terminal
        print("Mensagem decifrada:")
        print(mensagem_decifrada.decode('utf-8'))
    
    except Exception as e:
        print(f"Erro ao decifrar a mensagem: {e}")

else:
    print("Não foi possível ler o arquivo cifrado.")
