from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
from BobAuthenticity import ler_arquivo

#Função para verificar se todos os arquivos necessários estão presentes.
def verificar_pre_requisitos():
    
    arquivos_necessarios = [
        os.path.join('chaves_bob', 'chave_publica_bob.pem'),
        os.path.join('chaves_alice', 'assinatura_bob.bin'),
        os.path.join('chaves_alice', 'texto_claro.txt')
    ]
    
    for arquivo in arquivos_necessarios:
        if not os.path.exists(arquivo):
            print(f"Arquivo necessário não encontrado: {arquivo}")
            return False #return: True se todos os arquivos necessários estiverem presentes, caso contrário, False.
    return True


# Verificar se todos os pré-requisitos estão atendidos
if not verificar_pre_requisitos():
    print("Os pré-requisitos não foram atendidos. Certifique-se de que Bob tenha executado suas ações primeiro.")
    exit(1)

# Caminho da chave pública que será usada para verificar a assinatura
caminho_chave_publica = os.path.join('chaves_alice', 'chave_publica_bob.pem')

# Carregar a chave pública de Bob
with open(caminho_chave_publica, 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Caminhos para a assinatura e o texto claro
assinatura_path = os.path.join('chaves_alice', 'assinatura_bob.bin')
mensagem_path = os.path.join('chaves_alice', 'texto_claro.txt')

# Carregar a assinatura e o texto claro
assinatura = ler_arquivo(assinatura_path, 'rb')
texto_em_bytes = ler_arquivo(mensagem_path, 'rb')

# Verificar se a assinatura e o texto foram carregados com sucesso
if not assinatura:
    print(f"Erro ao carregar a assinatura de {assinatura_path}")
    exit(1)

if not texto_em_bytes:
    print(f"Erro ao carregar a mensagem original de {mensagem_path}")
    exit(1)

# Verificar a assinatura
try:
    public_key.verify(
        assinatura,
        texto_em_bytes,  # Texto original em bytes
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("A assinatura é válida, foi Bob quem enviou a mensagem. Foi autenticado.")
except Exception as e:
    print(f"Falha na verificação da assinatura: {e}")

#Função para ler o conteúdo de um arquivo de texto com codificação UTF-8.
def ler_mensagem(nome_arquivo):
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: #nome_arquivo: Caminho do arquivo a ser lido.
            return arquivo.read() #return: Conteúdo do arquivo como string.
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None

# Lendo e imprimindo a mensagem original
mensagem_original = ler_mensagem(mensagem_path)

if mensagem_original:
    print("Mensagem Original:")
    print(mensagem_original)
else:
    print("Não foi possível ler a mensagem original.")
