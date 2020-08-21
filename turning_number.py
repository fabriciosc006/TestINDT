def buscaMinimo(vetor, inferior, superior):
	#variavel min vai receber o menor valor do vetor na posicao inferior (inicialmente 0)
	min = vetor[inferior]
	#variavel i vai receber o valor do inferior (0)
	i = inferior
	#loop para percorrer o vetor(entrada) ate a ultima posicao do vetor e realizar a comparacao de valores
	for i in range(superior-1):
	#comparacao: se o valor do vetor[i] for menor o valor minimo
		if vetor[i] < min:
		#minimo vai receber o valor do vetor[i]
			min = vetor[i]
			#retorna o valor do minimo
	print ("A posicao do menor valor:  %d"%vetor.index(min))
	#caso vetor[i] seja maior que o min, entao sai do loop e imprime a posicao do menor valor
	return min

#vetor recebendo o valor de entrada
vetor = [10,9,8,7,6,1,2,3,4,5]
#variavel recebe o tamanho do vetor
tamanho_vetor = len(vetor)
#imprimir o resultado retornado com chamada da funcao
buscaMinimo(vetor, 0, tamanho_vetor)