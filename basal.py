#--------------------------------------------------->
# Script para calcular o seu gasto de caloria BASAL |
# Criado em 31 / 07 / 2024                          |
# Script de autoridade autoral                      |
# By Plastyne | Anarchy Ghost                       |
#--------------------------------------------------->

from colorama import Fore, Style

def calculate_bmr():
    print(Fore.GREEN + "Peso em KG:" + Fore.RED, end='')
    weight = float(input().strip())
    
    print(Fore.GREEN + "Altura em CM sem vírgula:" + Fore.RED, end='')
    height = float(input().strip())
    
    print(Fore.GREEN + "Idade:" + Fore.RED, end='')
    age = int(input().strip())

    BMR = 66 + (14.7 * weight) + (5.0 * height) - (6.8 * age)
    
    print(Fore.YELLOW + "Seu gasto calórico basal é de aproximadamente:" + Fore.RED + " {:.1f} ".format(BMR) + Fore.YELLOW + "calorias por dia." + Style.RESET_ALL)

calculate_bmr()
