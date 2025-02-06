num = [4,1,7,3,9,2]
num.sort()
print(num)
print(f"{len(num)}")
num.sort(reverse=True)
print(num)
soma = sum (num)
print(soma)

media = soma/len(num)
print(media)

num.insert(3, 30)
print(num)
num.insert(4, 7)
print(num)
num.remove(7) #remove procura o primeiro elemento da lista para eliminar
print(num)