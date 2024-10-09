import random

# Parâmetros
TAMANHO_POPULACAO = 10
TAMANHO_GENOMA = 8
TAXA_MUTACAO = 0.1
GERACOES = 20
CAPACIDADE_MOCHILA = 15

# Definindo os itens: (peso, valor)
itens = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10), (4, 7), (2, 6), (1, 2)]

# Função de Aptidão (Fitness)
def aptidao(individuo):
    peso_total = sum(individuo[i] * itens[i][0] for i in range(TAMANHO_GENOMA))
    valor_total = sum(individuo[i] * itens[i][1] for i in range(TAMANHO_GENOMA))
    if peso_total > CAPACIDADE_MOCHILA:
        return 0  # Penaliza soluções que excedem a capacidade
    else:
        return valor_total

# Criar um indivíduo (genoma)
def criar_individuo():
    return [random.randint(0, 1) for _ in range(TAMANHO_GENOMA)]

# Criar uma população
def criar_populacao():
    return [criar_individuo() for _ in range(TAMANHO_POPULACAO)]

# Cruzamento
def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, TAMANHO_GENOMA - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

# Mutação
def mutacao(individuo):
    for i in range(TAMANHO_GENOMA):
        if random.random() < TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]
    return individuo

# Seleção
def selecao(populacao):
    populacao_ordenada = sorted(populacao, key=lambda ind: aptidao(ind), reverse=True)
    return populacao_ordenada[:TAMANHO_POPULACAO // 2]

# Evolução
def evoluir(populacao):
    nova_populacao = []
    pais_selecionados = selecao(populacao)
    while len(nova_populacao) < TAMANHO_POPULACAO:
        pai1 = random.choice(pais_selecionados)
        pai2 = random.choice(pais_selecionados)
        filho = cruzamento(pai1, pai2)
        filho = mutacao(filho)
        nova_populacao.append(filho)
    return nova_populacao

# GA
def algoritmo_genetico():
    populacao = criar_populacao()
    melhor_individuo = None
    melhor_fitness = 0

    for geracao in range(GERACOES):
        populacao = evoluir(populacao)
        atual_melhor = max(populacao, key=lambda ind: aptidao(ind))
        atual_fitness = aptidao(atual_melhor)
        
        if atual_fitness > melhor_fitness:
            melhor_fitness = atual_fitness
            melhor_individuo = atual_melhor
        
        print(f"Geração {geracao + 1}: Melhor Aptidão = {atual_fitness}")

    # Melhor solução
    if melhor_individuo:
        itens_selecionados = [i+1 for i in range(TAMANHO_GENOMA) if melhor_individuo[i] == 1]
        peso_total = sum(itens[i][0] for i in range(TAMANHO_GENOMA) if melhor_individuo[i] == 1)
        valor_total = sum(itens[i][1] for i in range(TAMANHO_GENOMA) if melhor_individuo[i] == 1)
        print("\nMelhor solução encontrada:")
        print(f"Itens selecionados: {itens_selecionados}")
        print(f"Peso total: {peso_total}")
        print(f"Valor total: {valor_total}")
    else:
        print("Nenhuma solução válida encontrada.")

# Executar o algoritmo genético
if __name__ == "__main__":
    algoritmo_genetico()
