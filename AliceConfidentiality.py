from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os
from BobAuthenticity import ler_arquivo, salvar_arquivo, mover_arquivo_para_pasta

# Caminho para o arquivo do texto e a chave pública
arquivo_de_texto = "texto_claro2.txt"
caminho_chave_publica_bob = os.path.join('chaves_alice', 'chave_publica_bob.pem')
arquivo_cifrado = 'texto_cifrado.bin'

# Lendo o texto claro
texto = ler_arquivo(arquivo_de_texto, 'r')

if texto:
    texto_em_bytes = texto.encode('utf-8')

    # Carregar a chave pública de Bob de um arquivo PEM
    with open(caminho_chave_publica_bob, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    try:
        # Cifrar o texto usando a chave pública de Bob
        texto_cifrado = public_key.encrypt(
            texto_em_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Salvar o texto cifrado em um arquivo
        salvar_arquivo(arquivo_cifrado, texto_cifrado)

        pasta_destino_bob = 'chaves_bob'
        mover_arquivo_para_pasta(arquivo_cifrado, pasta_destino_bob)
    
    except ValueError as e:
        print(f"Erro ao cifrar a mensagem: {e} Provavelmente por conta do tamanho do texto")

else:
    print("Não foi possível ler o texto para cifrar.")
