from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
import shutil

def ler_arquivo(nome_arquivo, modo='r'):
    caminho = os.path.join(nome_arquivo)
    try:
        with open(caminho, modo) as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado na pasta base.")
        return None
    except PermissionError:
        print(f"Erro de permissão: Não é possível acessar '{caminho}'.")
        return None

def salvar_arquivo(nome_arquivo, conteudo):
    caminho = os.path.join(nome_arquivo)
    if os.path.exists(caminho):
        print(f"Aviso: O arquivo '{nome_arquivo}' já existe. Será substituído.")
    try:
        with open(caminho, 'wb') as arquivo:
            arquivo.write(conteudo)
        print(f"Arquivo salvo em: {nome_arquivo}")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

def mover_arquivo_para_pasta(arquivo, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    destino = os.path.join(pasta_destino, os.path.basename(arquivo))
    shutil.move(arquivo, destino)
    print(f"Arquivo '{arquivo}' movido para '{destino}'.")

# Caminho para o arquivo do texto e a pasta de destino
arquivo_de_texto = "texto_claro.txt"
pasta_destino = 'chaves_alice'

# Lendo o texto
texto = ler_arquivo(arquivo_de_texto, 'r')

if texto:
    texto_em_bytes = texto.encode('utf-8')

    # Caminho para encontrar o arquivo da chave privada
    caminho_chave = os.path.join('chaves_bob', 'chave_privada_bob.pem')

    # Carregando a chave privada de um arquivo PEM
    with open(caminho_chave, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Assinando a mensagem
    assinatura = private_key.sign(
        texto_em_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


    # Salvar a assinatura em um arquivo
    salvar_arquivo('assinatura_bob.bin', assinatura)

    # Mover a assinatura e o texto claro para a pasta de Alice
    mover_arquivo_para_pasta('assinatura_bob.bin', pasta_destino)
    salvar_arquivo(os.path.join(pasta_destino, 'texto_claro.txt'), texto.encode('utf-8'))

else:
    print("Não foi possível ler o texto para assinatura.")
