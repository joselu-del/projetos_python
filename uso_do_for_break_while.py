ingressos_livres = 50
tentativas = 0

print("🎬 Sistema de Vendas de Ingressos do Cinema")
print("Digite quantos ingressos deseja vender por vez (mínimo 1).")

while ingressos_livres > 0:
    tentativas += 1

    try:
        vendas = int(input(f"\nTentativa {tentativas} - Ingressos restantes: {ingressos_livres} >> "))
    except ValueError:
        print("⛔ Entrada inválida. Digite um número inteiro.")
        continue

    if vendas < 1:
        print("⛔ Você deve vender pelo menos 1 ingresso.")
    

    if vendas > ingressos_livres:
        print(f"⚠️ Só restam {ingressos_livres} ingressos. Tente novamente.")
        

    # Simula venda com um loop for (requisito obrigatório)
    for i in range(vendas):
        ingressos_livres -= 1

    print(f"✅ Venda de {vendas} ingresso(s) realizada com sucesso.")

    if ingressos_livres == 0:
        print("\n🎉 Todos os ingressos foram vendidos. Sessão esgotada!")
        break  # encerra o laço principal
