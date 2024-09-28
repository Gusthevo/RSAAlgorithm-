import time
from generateKeysBob import gerar_par_chaves_bob  # Importando a função de geração de chaves de Bob
from generateKeysAlice import gerar_par_chaves_alice  # Importando a função de geração de chaves de Alice
import seaborn as sns
import matplotlib.pyplot as plt

# Quantidade de execuções para cada processo
num_execucoes = 10

# Listas para armazenar os tempos de execução em milissegundos
tempos_bob = []
tempos_alice = []

# Executar a geração de chaves de Bob múltiplas vezes para medir o tempo
for i in range(num_execucoes):
    start_time_bob = time.time()  # Início da medição de Bob
    gerar_par_chaves_bob()  # Chamar a função que gera as chaves de Bob
    end_time_bob = time.time()  # Fim da medição de Bob
    
    # Acrescenta o tempo de execução no vetor (convertido para milissegundos)
    tempos_bob.append((end_time_bob - start_time_bob) * 1000)

# Executar a geração de chaves de Alice múltiplas vezes para medir o tempo
for i in range(num_execucoes):
    start_time_alice = time.time()  # Início da medição de Alice
    gerar_par_chaves_alice()  # Chamar a função que gera as chaves de Alice
    end_time_alice = time.time()  # Fim da medição de Alice
    
    # Acrescenta o tempo de execução no vetor (convertido para milissegundos)
    tempos_alice.append((end_time_alice - start_time_alice) * 1000)

# Calcular a média dos tempos de execução em milissegundos
tempo_medio_bob = sum(tempos_bob) / num_execucoes
tempo_medio_alice = sum(tempos_alice) / num_execucoes

# Exibir os tempos no terminal
print(f"Tempo médio de geração das chaves de Bob (após {num_execucoes} execuções): {tempo_medio_bob:.2f} milissegundos")
print(f"Tempo médio de geração das chaves de Alice (após {num_execucoes} execuções): {tempo_medio_alice:.2f} milissegundos")

# Exibir o tempo em um gráfico usando Seaborn
tempos_medios = [tempo_medio_bob, tempo_medio_alice]
label = ['Geração de Chaves Bob', 'Geração de Chaves Alice']

# Exibição do gráfico de barras
sns.barplot(x=label, y=tempos_medios)
plt.xlabel('Processo')
plt.ylabel('Tempo Médio de Execução (ms)')
plt.title(f'Tempo Médio de Geração dos Pares de Chaves de Bob e Alice (em {num_execucoes} execuções)')
plt.show()
