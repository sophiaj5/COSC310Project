#this API takes 10 summary pages from Wikipedia and extracts the first sentence to give a definition of the word
import wikipedia

def myWikipedia(word):
    output = wikipedia.summary(word, sentences = 1)
    return output

#extracting the definition of politics
#politics = (wikipedia.summary("Politics", sentences = 1))
#print(politics)

#extracting the definition of family 
#family = (wikipedia.summary("Family", sentences = 1))
#print(family)

#extracting the definition of leader
#leadership = (wikipedia.summary("Leadership", sentences = 1))
#print(leadership)

#extracting the definition of Canada
canada = (wikipedia.summary("Canada", sentences = 1))
#print(canada)

#extracting the definition of parliament
parliament = (wikipedia.summary("Parliament", sentences = 1))
#print(parliament)

#extracting the definition of school
school = (wikipedia.summary("School", sentences = 1))
#print(school)

#extracting the definition of Prime Minister
prime_minister = (wikipedia.summary("Prime minister", sentences = 1))
#print(prime_minister)

#extracting the definition of world
world = (wikipedia.summary("World", sentences = 1))
#print(world)

#extracting the definition of history
history = (wikipedia.summary("History", sentences = 1))
#print(history)

#extracting the definition of government
government = (wikipedia.summary("Government", sentences = 1))
#print(government)