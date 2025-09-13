# api_clima.R

args <- commandArgs(trailingOnly = TRUE)
API_KEY <- args[1]

if (is.na(API_KEY)) {
  stop("Erro: A chave da API não foi fornecida como um argumento.")
}

if (!require(httr)) install.packages("httr", repos = "http://cran.us.r-project.org")
if (!require(jsonlite)) install.packages("jsonlite", repos = "http://cran.us.r-project.org")
library(httr)
library(jsonlite)

cidades <- c("Itapetininga", "Itapeva", "Capão Bonito", "Itaberá", "Sao Paulo")

cat("----------------------------------------\n")
cat("  Previsão do Tempo nas Cidades Produtoras\n")
cat("----------------------------------------\n")

for (cidade in cidades) {
  URL <- paste0("http://api.openweathermap.org/data/2.5/weather?q=",
                URLencode(cidade), ",BR&units=metric&appid=", API_KEY, "&lang=pt")
  
  resposta <- GET(URL)
  
  if (http_error(resposta)) {
    cat(paste("Erro ao acessar a API para", cidade, ":", http_status(resposta)$message, "\n"))
  } else {
    dados_clima <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
    
    temperatura <- dados_clima$main$temp
    umidade <- dados_clima$main$humidity
    descricao_clima <- dados_clima$weather$description[1]
    
    cat("Previsão para", dados_clima$name, ":\n")
    cat("  - Temperatura Atual: ", temperatura, "°C\n")
    cat("  - Condição do Tempo: ", descricao_clima, "\n")
    cat("  - Umidade do Ar:     ", umidade, "%\n\n")
  }
}