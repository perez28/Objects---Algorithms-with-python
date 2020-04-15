class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

#Write your code here!

george_padre = Person("Mr. Burdell",53)
george_madre = Person("Mrs. Burdell",53)
george_p = Person( "George P. Burdell",25,george_padre,george_madre)



#The code below will let you test your code. It isn't used
#for grading, so feel free to modify it. As written, it
#should print George P. Burdell, Mrs. Burdell, and Mr.
#Burdell each on a separate line.
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)
