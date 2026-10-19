from colorama import Fore, Style, init

# Inicializa o colorama para funcionar no terminal do celular
init(autoreset=True)

# Lista com os 5 níveis, situações e cores conforme a tabela do Fichário
niveis_reservatorio = [
    {
        "nivel": "Nível 1",
        "situacao": "Muito baixo (crítico)",
        "cor": Fore.RED,
    },
    {"nivel": "Nível 2", "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": "Nível 3", "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": "Nível 4", "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": "Nível 5", "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def monitorar_reservatorio(lista):
  """Exibe cada nível do reservatório com a cor e situação correspondente."""
  print("=== SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ===")
  print("-" * 55)

  for item in lista:
    print(
        f"{item['cor']}[{item['nivel']}] Situação: {item['situacao']}{Style.RESET_ALL}"
    )

  print("-" * 55)


if __name__ == "__main__":
  monitorar_reservatorio(niveis_reservatorio)
