import string

def sao_anagramas(string1, string2):
  #A função remove os espaços e converte as letras para minúsculas, depois reordena os caracteres
  s1 = sorted(string1.replace(" ", "").lower())
  s2 = sorted(string2.replace(" ", "").lower())
  return s1 == s2

def cifra_de_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if char.isalpha():
            #Define base (maiúscula ou minúscula)
            base = ord('A') if char.isupper() else ord('a')
            #Aplica deslocamento circular
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            #Mantém caracteres não alfabéticos
            resultado += char

    return resultado

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    maior = ""
    
    for palavra in palavras:
        #Remove pontuação
        limpa = palavra.strip(string.punctuation)
        
        if len(limpa) > len(maior):
            maior = limpa

    return maior


#Zona de Testes
print(sao_anagramas("amor", "roma"))
print(sao_anagramas("gato", "cabra"))

print(cifra_de_cesar("abc", 2))
print(cifra_de_cesar("Ataque ao Amanhecer!", 5))

print(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma"))
print(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo."))
print(encontrar_maior_palavra("Seja forte e corajoso"))
