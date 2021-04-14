#translating parts of the conversation from English to French
import googletrans 
from googletrans import Translator

translator = Translator()

def myTranslator(text):
    output = translator.translate(text, dest = 'fr')
    return output.text

#general questions
#question 1: 1)what is your name? 2)what should I call you 3)whats your name? 4)name 5)title
name1 = translator.translate("My name is Justin Trudeau", dest = 'fr')
name2 = translator.translate("I'm Justin Trudeau or just Justin", dest = 'fr')
name3 = translator.translate("You can call me Justin", dest = 'fr')
#print(name1.text)
#print(name2.text)
#print(name3.text)

#question 2: 1)how old are you? 2) how old is justin 3)how old is trudeau 3) what is your age 4) how old are you 5)age? 6)age 7)old
age1 = translator.translate("I am 49 years old!", dest = 'fr')
age2 = translator.translate("I just turned 49!", dest = 'fr')


#print(googletrans.LANGUAGES)