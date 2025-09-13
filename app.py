import csv, math, os, subprocess

talhoes = []

insumos_por_cultura = {
    "soja": [
        {
            "nome": "Herbicida",
            "qtd_por_metro": 0.5,
            "modo_aplicacao": "Pulverização tratorizada"
        },
        {
            "nome": "Fungicida",
            "qtd_por_metro": 0.3,
            "modo_aplicacao": "Pulverização tratorizada"
        },
        {
            "nome": "Fertilizante",
            "qtd_por_metro": 1.2,
            "modo_aplicacao": "Distribuição a lanço tratorizada"
        }
    ],
    "milho": [
        {
            "nome": "Herbicida",
            "qtd_por_metro": 0.4,
            "modo_aplicacao": "Pulverização tratorizada"
        },
        {
            "nome": "Inseticida",
            "qtd_por_metro": 0.2,
            "modo_aplicacao": "Pulverização tratorizada"
        },
        {
            "nome": "Fertilizante",
            "qtd_por_metro": 1.5,
            "modo_aplicacao": "Distribuição a lanço tratorizada"
        }
    ]
}

def main():
    while True:
        print("\n- 🅕🅐🅡🅜🅣🅔🅒🅗 🅢🅞🅛🅤🅣🅘🅞🅝🅢 -")
        print("--- Menu Principal ---")
        print("[1] Gerenciar Plantios (Cadastrar, Ver, Editar, Excluir)")
        print("[2] Calcular Insumos")
        print("[3] Análise Estatística")
        print("[4] Consultar Previsão do Tempo")
        print("[5] Sair")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                break 
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                
        if opcao == 1:
            gerenciar_talhoes()
        elif opcao == 2:
            calcular_insumos()
        elif opcao == 3:
            analisar_e_exibir_dados()
        elif opcao == 4:
            consultar_previsao_tempo_r()
        elif opcao == 5:
            print("Saindo do programa. Obrigado por usar o FarmTech Solutions!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")

def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'sair':
            return None
        try:
            value = float(user_input)
            if value > 0:
                return value
            else:
                print("Valor inválido. Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def gerenciar_talhoes():
    if not talhoes:
        print("\nNenhum talhão cadastrado.")
        input("Pressione Enter para criar um novo talhão...")
        cadastrar_talhao()
        return
    
    while True:
        print("\n--- Gerenciar Plantios ---")
        print("Talhões Cadastrados:")
        for i, talhao in enumerate(talhoes):
            print(f"[{i}] Nome: {talhao["nome"]} | Cultura: {talhao["cultura"]} | Formato: {talhao["formato"]} | Area m²: {talhao["area_m2"]} | Qtd Ruas: {talhao["qtde_ruas"]} | Comprimento Total: {talhao["comprimento_ruas"]}")
        
        print("\nEscolha uma opção:")
        print("[0] Criar um novo talhão")
        print("[1] Editar um talhão existente")
        print("[2] Excluir um talhão existente")
        print("[3] Voltar ao Menu Principal")

        try:
            opcao = int(input("Digite sua opção: "))
            
            if opcao == 0:
                cadastrar_talhao()
            elif opcao == 1:
                editar_talhao()
            elif opcao == 2:
                deletar_talhao()
            elif opcao == 3:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def cadastrar_talhao():
    print("\n--- Cadastro de Talhão ---")
    print("Digite 'sair' a qualquer momento para cancelar.")
    
    novo_talhao = {}
    
    nome_talhao = input("Nome do talhão: ")
    if nome_talhao.lower() == 'sair':
        print("Operação de cadastro cancelada.")
        return
    novo_talhao["nome"] = nome_talhao

    while True:
        cultura = input("Informe a cultura (Soja / Milho): ").capitalize()
        if cultura.lower() == 'sair':
            print("Operação de cadastro cancelada.")
            return
        if cultura in ["Soja", "Milho"]:
            novo_talhao["cultura"] = cultura
            break
        else:
            print("Cultura inválida. Por favor, digite 'Soja' ou 'Milho'.")
            
    while True:
        formato = input("Informe o formato (Retângulo / Trapézio): ").capitalize()
        if formato.lower() == 'sair':
            print("Operação de cadastro cancelada.")
            return
        if formato in ["Retângulo", "Trapézio"]:
            novo_talhao["formato"] = formato
            break
        else:
            print("Formato inválido. Por favor, digite 'Retângulo' ou 'Trapézio'.")

    if novo_talhao["formato"] == "Retângulo":
        comprimento = get_float_input("Comprimento (m): ")
        if comprimento is None:
            print("Operação de cadastro cancelada.")
            return
        novo_talhao["comprimento"] = comprimento
        largura = get_float_input("Largura (m): ")
        if largura is None:
            print("Operação de cadastro cancelada.")
            return
        novo_talhao["largura"] = largura
        novo_talhao["area_m2"] = novo_talhao["comprimento"] * novo_talhao["largura"]

    elif novo_talhao["formato"] == "Trapézio":
        base_menor = get_float_input("Base menor (m): ")
        if base_menor is None:
            print("Operação de cadastro cancelada.")
            return
        novo_talhao["base_menor"] = base_menor
        base_maior = get_float_input("Base maior (m): ")
        if base_maior is None:
            print("Operação de cadastro cancelada.")
            return
        novo_talhao["base_maior"] = base_maior
        altura = get_float_input("Altura (m): ")
        if altura is None:
            print("Operação de cadastro cancelada.")
            return
        novo_talhao["altura"] = altura
        novo_talhao["area_m2"] = (novo_talhao["base_maior"] + novo_talhao["base_menor"]) * novo_talhao["altura"] / 2    
        novo_talhao["media_bases"] = (novo_talhao["base_maior"] + novo_talhao["base_menor"]) / 2

    espaco_ruas = get_float_input("Espaço entre ruas (m): ")
    if espaco_ruas is None:
        print("Operação de cadastro cancelada.")
        return
    novo_talhao["espaco_ruas"] = espaco_ruas

    if novo_talhao["formato"] == "Retângulo":
        novo_talhao["qtde_ruas"] = math.floor(novo_talhao["largura"] / novo_talhao["espaco_ruas"])
        novo_talhao["comprimento_ruas"] = novo_talhao["qtde_ruas"] * novo_talhao["comprimento"]   
    elif novo_talhao["formato"] == "Trapézio":
        novo_talhao["qtde_ruas"] = math.floor(novo_talhao["altura"] / novo_talhao["espaco_ruas"])
        novo_talhao["comprimento_ruas"] = novo_talhao["qtde_ruas"] * novo_talhao["media_bases"]
    
    talhoes.append(novo_talhao)

    print(f"\nO talhão '{novo_talhao['nome']}' foi cadastrado com sucesso!")

    return novo_talhao["nome"], novo_talhao["cultura"]

def editar_talhao():
    if not talhoes:
        print("Nenhum talhão para editar.")
        return
    
    print("\n--- Editar Talhão ---")
    for i, talhao in enumerate(talhoes):
        print(f"[{i}] Nome: {talhao["nome"]} | Cultura: {talhao["cultura"]} | Formato: {talhao["formato"]} | Area m²: {talhao["area_m2"]} | Qtd Ruas: {talhao["qtde_ruas"]} | Comprimento Total: {talhao["comprimento_ruas"]}")

    try:
        indice = int(input("Digite o número do talhão que deseja editar (ou 'sair'): "))
        if 0 <= indice < len(talhoes):
            talhao_a_editar = talhoes[indice]
        else:
            print("Índice inválido.")
            return
    except ValueError:
        print("Operação de edição cancelada.")
        return
    
    while True:
        print(f"\nEditando o talhão '{talhao_a_editar["nome"]}'. O que deseja alterar?")
        print("[1] Nome")
        print("[2] Cultura")
        print("[3] Dimensões e formato")
        print("[4] Cancelar")

        try:
            opcao = int(input("Digite sua opção: "))
            
            if opcao == 1:
                novo_nome = input("Novo nome (ou 'sair'): ")
                if novo_nome.lower() == 'sair':
                    print("Operação de edição cancelada.")
                    return
                talhao_a_editar["nome"] = novo_nome
                print("Nome alterado com sucesso.")
            elif opcao == 2:
                nova_cultura = input("Nova cultura (Soja/Milho, ou 'sair'): ").capitalize()
                if nova_cultura.lower() == 'sair':
                    print("Operação de edição cancelada.")
                    return
                talhao_a_editar["cultura"] = nova_cultura
                print("Cultura alterada com sucesso.")
            elif opcao == 3:
                print("Você precisará reinserir as dimensões e o formato.")
                # Lógica de edição de dimensões com cancelamento
                formato = input(f"Informe o formato (Retângulo / Trapézio): ").capitalize()
                if formato.lower() == 'sair':
                    print("Operação de edição cancelada.")
                    return
                talhao_a_editar["formato"] = formato

                if talhao_a_editar["formato"] == "Retângulo":
                    comprimento = get_float_input("Comprimento (m): ")
                    if comprimento is None: return
                    largura = get_float_input("Largura (m): ")
                    if largura is None: return
                    talhao_a_editar["comprimento"] = comprimento
                    talhao_a_editar["largura"] = largura
                    talhao_a_editar["area_m2"] = talhao_a_editar["comprimento"] * talhao_a_editar["largura"]
                elif talhao_a_editar["formato"] == "Trapézio":
                    base_menor = get_float_input("Base menor (m): ")
                    if base_menor is None: return
                    base_maior = get_float_input("Base maior (m): ")
                    if base_maior is None: return
                    altura = get_float_input("Altura (m): ")
                    if altura is None: return
                    talhao_a_editar["altura"] = altura
                    talhao_a_editar["area_m2"] = (talhao_a_editar["base_maior"] + talhao_a_editar["base_menor"]) * talhao_a_editar["altura"] / 2    
                    talhao_a_editar["media_bases"] = (talhao_a_editar["base_maior"] + talhao_a_editar["base_menor"]) / 2

                espaco_ruas = get_float_input("Espaço entre ruas (m): ")
                if espaco_ruas is None: return
                talhao_a_editar["espaco_ruas"] = espaco_ruas

                if talhao_a_editar["formato"] == "Retângulo":
                    talhao_a_editar["qtde_ruas"] = math.floor(talhao_a_editar["largura"] / talhao_a_editar["espaco_ruas"])
                    talhao_a_editar["comprimento_ruas"] = talhao_a_editar["qtde_ruas"] * talhao_a_editar["comprimento"]   
                elif talhao_a_editar["formato"] == "Trapézio":
                    talhao_a_editar["qtde_ruas"] = math.floor(talhao_a_editar["altura"] / talhao_a_editar["espaco_ruas"])
                    talhao_a_editar["comprimento_ruas"] = talhao_a_editar["qtde_ruas"] * talhao_a_editar["media_bases"]
                print("Dimensões e formato alterados com sucesso.")
            elif opcao == 4:
                print("Operação de edição cancelada.")
                return
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def deletar_talhao():
    if not talhoes:
        print("Nenhum talhão para excluir.")
        return

    print("\n--- Excluir Talhão ---")
    for i, talhao in enumerate(talhoes):
        print(f"[{i}] Nome: {talhao["nome"]} | Cultura: {talhao["cultura"]} | Formato: {talhao["formato"]} | Area m²: {talhao["area_m2"]} | Qtd Ruas: {talhao["qtde_ruas"]} | Comprimento Total: {talhao["comprimento_ruas"]}")
    
    try:
        user_input = input("Digite o número do talhão que deseja excluir (ou 'sair'): ")
        if user_input.lower() == 'sair':
            print("Operação cancelada.")
            return
        indice = int(user_input)

        if 0 <= indice < len(talhoes):
            talhao_a_excluir = talhoes[indice]
            confirmacao = input(f"Tem certeza que deseja excluir '{talhao_a_excluir["nome"]}'? (S/N): ").capitalize()
            if confirmacao == "S":
                talhoes.pop(indice)
                print(f"'{talhao_a_excluir["nome"]}' foi excluído com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
  
def calcular_insumos():
    if not talhoes:
        print("Nenhum talhão cadastrado. Por favor, cadastre um primeiro.")
        return

    print("--- Talhões Cadastrados ---")
    for i, talhao in enumerate(talhoes):
        print(f"[{i}] Nome: {talhao["nome"]} | Cultura: {talhao["cultura"]} | Formato: {talhao["formato"]} | Area m²: {talhao["area_m2"]} | Qtd Ruas: {talhao["qtde_ruas"]} | Comprimento Total: {talhao["comprimento_ruas"]}"
        )

    try:
        user_input = input("Digite o número do talhão desejado (ou 'sair'): ")
        if user_input.lower() == 'sair':
            print("Operação cancelada.")
            return
        indice_talhao = int(user_input)

        if 0 <= indice_talhao < len(talhoes):
            talhao_escolhido = talhoes[indice_talhao]
        else:
            print("Número de talhão inválido. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    cultura_escolhida = talhao_escolhido["cultura"]
    insumos_disponiveis = insumos_por_cultura[cultura_escolhida.lower()]

    print(f"\n--- Insumos para {cultura_escolhida} ---")
    for i, insumo in enumerate(insumos_disponiveis):
        print(f"[{i}] {insumo["nome"]} - Modo de Aplicação: {insumo["modo_aplicacao"]}")

    try:
        user_input = input("Digite o número do insumo desejado (ou 'sair'): ")
        if user_input.lower() == 'sair':
            print("Operação cancelada.")
            return
        indice_insumo = int(user_input)

        if 0 <= indice_insumo < len(insumos_disponiveis):
            insumo_escolhido = insumos_disponiveis[indice_insumo]
        else:
            print("Número de insumo inválido. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    comprimento_total_ruas = talhao_escolhido["comprimento_ruas"]
    qtd_por_metro = insumo_escolhido["qtd_por_metro"]
    
    quantidade_total = comprimento_total_ruas * qtd_por_metro

    print("------------------------------------------")
    print(f"Relatório de Insumos para o talhão '{talhao_escolhido["nome"]}':")
    print(f"Insumo: {insumo_escolhido["nome"]}")
    print(f"Modo de Aplicação: {insumo_escolhido["modo_aplicacao"]}")
    print(f"Quantidade total necessária: {quantidade_total:.2f} litros")
    print("------------------------------------------")
    input("Pressione Enter para voltar ao menu principal.")

def exportar_para_csv():
    nome_arquivo = "dados_agricolas.csv"

    if not talhoes:
        print("Nenhum dado para exportar. Por favor, cadastre um talhão primeiro.")
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"O arquivo '{nome_arquivo}' anterior foi removido.")
        return False

    chaves = [
        "nome", "cultura", "formato", "comprimento", "largura", 
        "base_menor", "base_maior", "altura", "media_bases", 
        "espaco_ruas", "qtde_ruas", "comprimento_ruas", "area_m2"
    ]

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=chaves)
            writer.writeheader()
            writer.writerows(talhoes)

        print(f"\nDados exportados com sucesso para o arquivo '{nome_arquivo}'.")
        return True
    except Exception as e:
        print(f"Erro ao exportar o arquivo CSV: {e}")
        return False

def analisar_e_exibir_dados():
    print("\n--- Analisando Dados com R ---")
    
    exportacao_bem_sucedida = exportar_para_csv()
    
    if not exportacao_bem_sucedida:
        return

    caminho_rscript = "Rscript" 
    caminho_script_r = os.path.abspath("analise_dados.R")
    
    try:
        resultado = subprocess.run(
            [caminho_rscript, caminho_script_r],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
        )
        print(f"\n{resultado.stdout}")
    except FileNotFoundError:
        print("Erro: Rscript não foi encontrado. Verifique se o caminho está correto.")
        print("Ajuste: Adicione a pasta 'bin' do R ao seu PATH do sistema.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script R: {e}")
        print(e.stderr)

    input("Pressione Enter para voltar ao menu principal.")

def consultar_previsao_tempo_r():
    print("\n--- Consultando Previsão do Tempo (via R) ---")

    API_KEY = os.environ.get("OPENWEATHER_API_KEY")
    if not API_KEY:
        print("Erro: A chave da API não foi definida como variável de ambiente.")
        print("A funcionalidade não pode ser executada.")
        input("Pressione Enter para voltar ao menu principal.")
        return
    
    caminho_rscript = "Rscript"
    caminho_script_r = os.path.abspath("api_clima.R")
    
    try:
        resultado = subprocess.run(
            [caminho_rscript, caminho_script_r, API_KEY], 
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
            )
        print(f"\n{resultado.stdout}")
    except FileNotFoundError:
        print(f"Erro: O executável do Rscript não foi encontrado.")
        print("Ajuste: Adicione a pasta 'bin' do R ao seu PATH do sistema.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script R: {e}")
        print(e.stderr)

    input("Pressione Enter para voltar ao menu principal.")

if __name__ == "__main__":
    main()