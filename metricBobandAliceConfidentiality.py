import time
import subprocess
import seaborn as sns
import matplotlib.pyplot as plt

# Quantidade de execuções para cada processo
num_execucoes = 10

# Listas para armazenar os tempos de execução em milissegundos
tempos_alice = []
tempos_bob = []

# Executar a cifração de Alice múltiplas vezes para medir o tempo
for i in range(num_execucoes):
    # Registrar o tempo de início
    start_time_alice = time.time()  # Início da medição de Alice
    # Executar o script de cifração de Alice usando subprocess
    subprocess.run(['python', 'AliceConfidentiality.py'])
    end_time_alice = time.time()  # Fim da medição de Alice
    
    # Acrescenta o tempo de execução no vetor em milissegundos
    tempos_alice.append((end_time_alice - start_time_alice) * 1000)

# Executar a decifração de Bob múltiplas vezes para medir o tempo
for i in range(num_execucoes):
    # Registrar o tempo de início
    start_time_bob = time.time()  # Início da medição de Bob
    # Executar o script de decifração de Bob usando subprocess
    subprocess.run(['python', 'BobConfidentiality.py'])
    end_time_bob = time.time()  # Fim da medição de Bob
    
    # Acrescenta o tempo de execução no vetor em milissegundos
    tempos_bob.append((end_time_bob - start_time_bob) * 1000)

# Calcular a média dos tempos de execução em milissegundos
tempo_medio_alice = sum(tempos_alice) / num_execucoes
tempo_medio_bob = sum(tempos_bob) / num_execucoes

# Exibir os tempos no terminal
print(f"Tempo médio necessário para cifrar a mensagem com a chave pública de Bob (em {num_execucoes} execuções): {tempo_medio_alice:.4f} milissegundos")
print(f"Tempo médio necessário para Bob decifrar a mensagem com sua chave privada (em {num_execucoes} execuções): {tempo_medio_bob:.3f} milissegundos")

# Exibir o tempo em um gráfico usando Seaborn
tempos_medio = [tempo_medio_alice, tempo_medio_bob]
label = ['Cifrar a mensagem com a chave pública de Bob', 'Decifrar a mensagem com a chave privada de Bob']

# Exibição do gráfico de barras
sns.barplot(x=label, y=tempos_medio)
plt.xlabel('Processo')
plt.ylabel('Tempo Médio de Execução (ms)')
plt.title(f'Tempo Médio de Execução (em {num_execucoes} execuções)')
plt.show()
