# Importar as bibliotecas científias. Chamamos as biliotecas não pelo seu nome original, mas pelo 'apelido'
# que estamos dando a elas('as pd');
# Pandas nos dá ferrmanetas para trabalhar com data frames, um tipo de variável parecida com uma tabela.
import pandas as pd

# Matplot nos dá as ferrmantas para trabalharmos com gráficos, utilizaremos o tema do ggpplot, que nos dará
# gráficos parecidos com os gráficos de R.
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Statmodels faz parte da biblioteca para computação científica scipy. Como usaremos somente a regressão linear, não faz sentido
#importar toda a biblioteca.
import statsmodels.api as sm

# Usaremos o pandas para ler a tabela de excel com os dados e salvaremos esta tabela numa variável 'dados'.
#Substitua o caminho dentro das aspas com a localização do arquivo WAGE1 dentro do seu computador.
dados = pd.read_excel('C:/Users/Thiago/Desktop/Google Drive/R Projects/Econometria 1/WAGE1/WAGE1.xlsx')

# Print mostra algo na tela. Neste caso ele mostrará as 7 primeiras (head) linhas da variável 'dados'.
# Se quisessemos ver as 7 últimas linhas usariámos dados.tail(7).
print(dados.head(7))

# Criamos um modelo de regressão linear simples por meio de OLS (mínimos quadrados). Especificamos que 
# a variável salário será explicada pela variável educ e que as observações nas quais faltam valores serão
# ignoradas.
reg = sm.OLS(endog= dados['salário'], exog= dados['educ'], missing= 'drop')

# Diferentemente do R, que nos retorna um objeto com todas as informações da regressão, temos que construir estas.
# A linha a seguir resolve o modelo e salva numa variável 'resultados'.
resultados = reg.fit()

# Mostra o sumário da regressão
print(resultados.summary())

# Salvamos os valores de  y obtidos a partir dos coeficientes do modelo numa variável 'y_chapeu'. 
y_chapeu = resultados.predict()

# A partir de agora começaremos a construir o gráfico.
# O primeiro e segundo argumentos das funções 'scatter' e 'plot' serão 'x' e 'y' respectivamente.
# Usaremos os argumentos 'label' e 'color' respectivamente para darmos nome e cor ao objeto.
# plt é o método para construirmos o gráfico, e assim como o ggplot no R, este será feito por camadas.
# Expor as observações de salário dado um nível educacional em forma de pontos (scatter)
plt.scatter(dados['educ'],dados['salário'], label = 'Observações', color = 'blue')

# Expor os valores de y obtidos pelo modelo.
plt.plot(dados['educ'], y_chapeu, label = 'Linha de regressão', color = 'green')

# Dar uma string como título do gráfico
plt.title('Salário de acordo com a educação')

# Dar nomes aos eixos x e y:
plt.xlabel('Anos de educação')
plt.ylabel('Salário')

#Utilizar as legendas dadas
plt.legend()

#Printa o gráfico
plt.show()
