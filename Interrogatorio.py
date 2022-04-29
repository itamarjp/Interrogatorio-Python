respostas = [] 

respostas.append(input("Telefonou para a vítima ? "))
respostas.append(input("Esteve no local do crime ? "))
respostas.append(input("Mora perto da vítima ? "))
respostas.append(input("Tinha dívidas com a vítima ? "))
respostas.append(input("Já trabalhou com a vítima ? "))

quantidade_de_sim = respostas.count("sim")

resultado = "Inocente"

if quantidade_de_sim == 2:
  resultado = "Suspeito"

if quantidade_de_sim == 3:
  resultado = "Cúmplice"

if quantidade_de_sim == 4:
  resultado = "Cúmplice"

if quantidade_de_sim == 5:
  resultado = "Assassino"

print("O Interrogado é considerado " + resultado)
 

