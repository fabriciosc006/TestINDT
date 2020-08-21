def bubble_sort(vetor):
	#variavel auxiliar de apoio na logica da troca de posicoes ira receber o valor 0
	aux = 0
	#variavel para apoio como contador ira receber o valor 0
	contador = 0
	#loop enquanto o contador for menor que o tamanho do vetor(entrada)
	while (contador < len(vetor)):
	#loop para percorrer o vetor(entrada) e realizar a comparacao de valores
		for i in range(len(vetor)-1):
		#comparacao: se o valor do vetor[i] for maior que o da direita
			if (vetor[i] > vetor[i+1]):
			#variavel auxiliar vai receber o valor do vetor[i] (maior)
				aux = vetor[i]
				#vetor[i] vai receber o valor do vetor[i] da direita (menor)
				vetor[i] = vetor[i+1]
				#vetor[i+1] (da direita) vai receber o valor do auxiliar(maior)
				vetor[i+1] = aux
				#contador vai incrementar para continuar a lagica para os demais valores
		contador = contador + 1
	#print("Vetor ordenado: \n")
	numeros = str(vetor).replace(',', ' ')
	#ao final das comparacoes quando o contador nao satisfazer o while, ira transformar o vetor em string separando os valores por espaco
	#imprimir a saida
	print(numeros)
	

#vetor = [10,8,2,3,5,1]
#criacao de um vetor
vetor2 = []
#variavel recebendo o  valor de entrada
vetor_string = "10 8 2 3 5 1".split(" ")
#laco de repeticao para adicionar os valores numa lista de inteiros
for i in vetor_string:
	vetor2.append(int(i))

#print(vetor2)
#chamada do programa
bubble_sort(vetor2)