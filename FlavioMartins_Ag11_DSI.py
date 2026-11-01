
# Sistema Simples de Monitoramento de Reservatório de Água
# Objetivo: Mostrar alertas coloridos de acordo com o nível da água


# Recursos da biblioteca colorama
# Fore -> define a cor do texto - # Style -> aplica estilos (ex.: RESET_ALL para voltar ao padrão) - # init -> inicializa o colorama
from colorama import Fore, Style, init

# Inicialização da biblioteca de cores.
init(autoreset=False)


# Dicionário de níveis do reservatório
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo",                 "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio",                 "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto",                  "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)",   "cor": Fore.BLUE},
]

# Função: obter_cor_por_nivel
# Responsável por retornar a cor do colorama de acordo com
# o nível informado. Caso o nível não exista, retorna branco.

def obter_cor_por_nivel(nivel):
    for item in niveis_reservatorio:
        if item["nivel"] == nivel:
            return item["cor"]
    return Fore.WHITE  # fallback seguro


# Função de exibição de "_alerta", exibe a situação do reservatório com a cor correspondente ao nível.

def exibir_alerta(nivel):
    for item in niveis_reservatorio:
        if item["nivel"] == nivel:
            cor = obter_cor_por_nivel(nivel)
            # Monta a mensagem formatada com a cor do nível
            mensagem = f"[NÍVEL {item['nivel']}] {item['situacao']}"
            print(f"{cor}{mensagem}{Style.RESET_ALL}")
            return

    # Caso o nível não exista na lista
    print(f"{Fore.WHITE}[NÍVEL {nivel}] Situação desconhecida{Style.RESET_ALL}")


# Simula a leitura do reservatório exibindo todos os níveis

def simular_monitoramento():
    print("=" * 55)
    print("   SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA")
    print("=" * 55)

    # Percorre a lista e exibe cada situação simulada

    for item in niveis_reservatorio:
        exibir_alerta(item["nivel"])

    print("=" * 55)

    # Boa prática, evita que o terminal fique colorido
    print(Style.RESET_ALL, end="")


# Ponto de entrada do programa

if __name__ == "__main__":
    simular_monitoramento()

















































































