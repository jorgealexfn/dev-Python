# comando [].append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# comando [].copy

lista2 = [1, "Python", [40, 30, 20]]
l2 = lista2.copy()

print(id(l2), id(lista2))

# comando [].count

colors = ["red", "blue", "green", "blue"]


red = colors.count("red")
print(red)
blue = colors.count("blue")
print(blue)
green = colors.count("green")
print(green)

#comando [].extend

languages = ["python", "js", "java"]

print(languages)

languages.extend(["c", "csharp"])
print(languages)

#comando [].index

languages = ["python", "js", "java"]
                #0      #1      #2
ind = languages.index("java")
print(ind) # 2

#comando [].pop

languages = ["python", "js", "java", "c", "csharp"]

p = languages.pop()

print(p)
p = languages.pop()
print(p)
p = languages.pop()
print(p)

#comando [].remove

languages = ["python", "js", "java", "c", "csharp"]
r = languages.remove("c")

print(r)

#comando [].reverse
languages = ["python", "js", "java", "c", "csharp"]
mirror = languages.reverse

print(mirror)

#comanod [].sort ordenação padrao
languages = ["python", "js", "java", "c", "csharp"]
languages.sort()
print(languages)

languages = ["python", "js", "java", "c", "csharp"]
languages.sort(reverse=True)
print(languages)

languages = ["python", "js", "java", "c", "csharp"]
languages.sort(key=lambda x: len(x)) # por ordem de tamanho de letras
print(languages)

languages = ["python", "js", "java", "c", "csharp"]
languages.sort(key=lambda x: len(x), reverse=True)
print(languages)

#função built-in (inclusa na linguagem)
#len tira tamanho das coisas
#sorted 

sorted(languages, key=lambda x: len(x)) 

