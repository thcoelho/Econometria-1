# Carregar os pacotes do tidyverse, que acabam por facilitar e deixarem mais bonitas
# algumas das funções do R base, principalmente os gráficos.
library(tidyverse)

# Salvar as informações de salário num data frame chamado WAGE;
# Data frames são a coisa mais perto de uma tabela de excel que temos no R;
# O tibble é um formato ligeiramente melhorado do data frame;
# O pacote wooldridge contém os dados para exercícios do livro, como só utilizaremos 
# as informações de salário, carregamos somente esses dados e não todo o pacote.
# <- salva a informação que a está a sua direita na variável a sua esquerda.
WAGE <- as_tibble(wooldridge::wage1)

# View() abre a variável para melhor visualização:
View(WAGE)

# lm faz uma regressão linear, sendo a variável antes do ~ a explicada e a depois do ~ a explicativa
# wage e educ são colunas do data frame WAGE, por isso explicitamos da onde estamos tirando
# estas duas variáveis com o comando data = wAGE
reg_linear <- lm(wage ~ educ, data = WAGE)


# Inicia um objeto ggplot[gráfico] com os dados de WAGE. O ggplot cria gráficos por camadas,
# por isso o '+' após cada comando que cria uma camada.
ggplot(data = WAGE) +
  
  # Plota as observações contidas no data frame, sendo x educação e y o salário
  # Discernindo os níveis de salário por diferentes tons de azul
  geom_point(mapping = aes(x = educ, y = wage, color = wage)) +
  
  # Gera uma reta com intercepto igual ao encontrado na regressão linear e com 
  # inclinação(slope) igual ao coeficiente beta 1 encontrado para educ(x). Pinta 
  # a reta de verde escuro
  geom_abline(intercept = reg_linear[['coefficients']][['(Intercept)']], 
              slope = reg_linear[["coefficients"]][["educ"]],
              color = 'darkgreen') +
  
  # Usa o tema padrão
  theme_classic() +
  # Coloca as informações do gráfico: Título, eixo X e eixo Y.
  labs(title = "Salário em relação a educação",
       x = "Estudo (Anos)",
       y = "Salário (USD/Hora)") 
  
  
