#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = [int(input(":")) for x in range(10)]
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [str(input(":")) for x in range(2)]
    if sorted(words[0].split())==sorted(words[1].split()):
        return True
    return False


def contains_doubles(items: list) -> bool:
    i = 0
    for x in items:
        for y in items:
            if y==x:
                i+=1
        if i>=2:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    moyenne = lambda liste : sum(liste)/len(liste)
    nom = None
    moy = 0
    for noms, notes in student_grades.items():
        info = moyenne(notes)
        if info > moy:
            nom = noms
            moy = info
    return {nom: moy}


def frequence(sentence: str) -> dict:
    sentence = sentence.lower()
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lettres = {chr(97+x):0 for x in range(26)}
    for lettre in sentence:
        try:
            lettres[lettre]+=1
        except:
            pass
    final = {}
    for lettre, repetition in lettres.items():
        if repetition>5:
            final[lettre] = repetition
    return {x: y for x, y in sorted(final.items(), key=lambda item: item[1])}

class recettes:
    def __init__(self):
        self.recettes = {}
    def get_recipes(self):
        recette = str(input("recette: "))
        ingredients, ingredient = [], str(input("ingredient: "))
        while ingredient != "":
            ingredients.append(ingredient)
            ingredient = str(input("ingredient: "))
        self.recettes[recette] = ingredients

    def print_recipe(self, ingredients) -> None:
        for x,y in self.recettes.items():
            if sorted(y) == sorted(ingredients):
                return x
        return None


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    # print(order())

    print(f"On vérifie les anagrammes...")
    # print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    RECIPIES = recettes()
    recipes = ["eau", "jus", "pomme"]
    print("On enregistre les recettes...")
    RECIPIES.get_recipes()

    print("On affiche une recette au choix...")
    print(RECIPIES.print_recipe(recipes))


if __name__ == '__main__':
    main()
