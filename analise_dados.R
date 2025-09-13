# analise_dados.R

# Carrega os dados do arquivo CSV
dados <- read.csv("dados_agricolas.csv")

# Calcula a média e o desvio padrão da área plantada
media_area <- mean(dados$area_m2)
desvio_area <- sd(dados$area_m2)

# Exibe os resultados no terminal
print("--- Análise Estatística da Área Plantada ---")
print(paste("Média da Área (m²):", round(media_area, 2)))
print(paste("Desvio Padrão da Área (m²):", round(desvio_area, 2)))

# Você pode fazer o mesmo para outras colunas
media_ruas <- mean(dados$comprimento_ruas)
desvio_ruas <- sd(dados$comprimento_ruas)

print("--- Análise Estatística do Comprimento Total das Ruas ---")
print(paste("Média do Comprimento das Ruas (m):", round(media_ruas, 2)))
print(paste("Desvio Padrão do Comprimento das Ruas (m):", round(desvio_ruas, 2)))