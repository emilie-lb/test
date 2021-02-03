def compter_mots(mots):
    liste_mots = mots.split()
    repeat=0
    mots_vus = set(liste_mots)
    for mot in mots_vus:
        if liste_mots.count(mot) > 1:
            repeat +=1
    return(repeat)

# def safa_count(input):
#   l = []
#   words = input.split()
#   for word in words:
#     if word not in l and words.count(word) > 1 :
#       l.append(word) 
#   return len(l)

def count_repeated_word(n, words):
  # on crée un set, un ensemble d'elements uniques
  s = set()
  # on split words, mot par mot
  words = words.split()
  # pour chaque mot dans la liste de mots
  for word in words:
    # si le mot est plus d'une fois dans la liste de mots
    if words.count(word) > 1:
      # on ajoute le mot dans notre set
      s.add(word)
  # on retourne la taille de s
  return len(s)

def count_repeat(mots):
    liste = mots.split()
    motsvus = []
    compte=0
    for mot in liste:
        if mot not in motsvus:
            motsvus.append(mot)
    for mot in motsvus:
        if liste.count(mot) > 1:
            compte+=1
    return compte

print(count_repeat('hello hello hello lol lol'))
    
print(compter_mots("word word word"))
print(compter_mots("word wqf whrth"))
print(compter_mots("steph", "Emilie", "Emilie","Nico"))