#usuario insere o salario que recebe
Nome = input("qual o seu nome? ")

#usuario insere o salario que recebe
salario = float(input("Quanto você ganha por mês?: " ))
print()# pular uma linha

#imposto sobre cada quantidade de salario
imposto = float(salario) * 0.0
if salario >= 3000 and salario < 4000:
  imposto = float(salario) * 0.013
  
if salario >= 4000 and salario < 5000:
 imposto = float(salario) * 0.055
 
if salario >= 5000 and salario < 8000:
 imposto = float(salario) * 0.096
 
if salario >= 8000 and salario < 10000:
 imposto = float(salario) * 0.163
 
if salario >= 10000 and salario < 15000:
 imposto = float(salario) * 0.185
 
if salario >= 15000:
 imposto = float(salario) * 0.215

print("_________________________________________")

print("| NOME DE USUÁRIO: " + str(Nome))

#mostrar o salario 
print("| SEU SALÁRIO: " + "R$" + str(salario))
print("|")#pular uma linha

#mostrar o valor do imposto
print("| Valor do imposto: " + "R$" +str(imposto))
print("|")#pular uma linha

#calcular e mostrar o valor do salario pós imposto
print("| Salario final: " + "R$" + str(salario - imposto))
print("|________________________________________")