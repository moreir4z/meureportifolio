import random

print("🎯 Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("✅ Parabéns! Você acertou o número!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("❌ Errado! Tente de novo. Restam", tentativas, "tentativas.")
        else:
            print("💀 Fim de jogo! O número era:", numero_secreto)