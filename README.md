# COSC310Project

This individual project expands off of Group 23's project on the interactive conversational bot that was based on the current Prime Minister of Canada, Justin Trudeau, who replies to the user's questions based on his past, present, future, and his relationships.

This ChatBot implentation uses deeplearning through tensorflow's and tflearn's APIs. The basic idea is that through tensorflow, we will create a probabilistic function based on our input data (intents.json) and use this to estimate which "tag" most appropriately fits our user's input. Using this "tag", we can simply output a random hardcoded response. For example, if the user is to input "hello", the bot will calculate which tag is most fitting to the user's input. This will be returned as a float, representing a precentage from 0-100. The bot then simply takes the MAX float and says that is the closest matching tag, and then grabs a random response belonging to the same tag, in this case the "greetings" tag. This is a good approach to the problem, as it allows the bot to work with fewer constraints and without handling only hardcoded inputs.

The idea behind using tensorflow is that with a fully inter-connected neural network, passing data through it will give us a probablity gradient for each of our responses and their belonging tags. Using something similar to a one-hot-encoded pattern, tensorflow works based on an array of "0s", representing all the words we have included in our expected inputs. When the user passes in a string, we increment at the index of the matching word in this "0's" array to a "1". Using this we can pass it through our nodes and pop out a response.

Our group also implemented some features to further enhance the user's experience and to improve the flow of conversation with the chat bot. A Graphical User Interfance(GUI) has been used in place of the terminal for input/output, so that the user has a more pleasant experience when talking with the bot. The bot also utilizes Stanford's CoreNLP Toolkit to make use of features such as Sentiment Analysis, which allows the bot to provide appropriate responses to statements that are not present in the question bank, and Part-of-speech(POS) tagging which helps the bot recognize certain key words as parts of speech(useful for performing other functions). Synonym recognition was also be implemented with the use of NLTK's WordNet. This feature helps the bot understand a wider range of vocabulary and sentences while providing the correct response.

For my individual part of the project, I have implemented both the Google Translate API and the Wikipedia API. The Google Translate API gives the user the ability to converse with Justin Trudeau in both English and French. You can change the language by adding the phrase "in French" or "in English" after your question. The Wikipedia API gives you the ability to ask Mr.Trudeau any definitions he knows, and he will response by pulling the Wikipedia definition of the word.

# Downloading Required APIs

install nltk https://www.nltk.org/install.html

install tensorflow https://www.tensorflow.org/install

install tflearn http://tflearn.org/installation/

install numpy https://numpy.org/install/

install pycorenlp https://pypi.org/project/pycorenlp/

install googletrans https://pypi.org/project/googletrans/

install wikipedia https://pypi.org/project/wikipedia/

# Setting up

- Clone the COSC310-Interactive-Conversational-Agent repository
- Open chatbot.py in your prefered Python IDE
- In the terminal enter:
  import nltk
  nltk.download('punkt')
  nltk.download('wordnet')

- Download the Stanford NLP Toolkit (CoreNLP) zip folder https://stanfordnlp.github.io/CoreNLP/
- Extract the zip file to one directory level above this project's folder

For example, if your project folder is located at C:\Users\USER\COSC310-INTERACTIVE-CONVERSATIONAL-AGENT, then extract file to C:\Users\USER\

# Running
- Compile and run stanfordload.py
- Compile and run gui.py

# Files

- chatbot.py Has the chat function that returns bot's response to gui.py and calls load.py to create training data if none exists.
- load.py Loads in intents.json and processes the data into a trained tflearn model for a response based on a probabilty of the corresponding tag to the question asked
- intents.json Database of tags, patterns, and responses.
- data.pickle Pickle file to store the processed files and not have to reprocesses them everytime
- model.tflearn tflearn models that have been stored as not to run the training algorithm everytime
- stanfordload.py Establishes connection to Stanford's CoreNLP Server
- gui.py Comprises of functions that make the GUI for the chat bot
- sentiment.py Contains functions that conduct sentiment analysis on the user's input statement using Stanford's CoreNLP Toolkit
- syn_recognition.py Contains functions that tag parts-of-speech in user's input, and creates different sentences with different combinations of synonyms
- test_chatbot.py Contains unit tests for major functions and classes to validate them

# List of New Features

1. Google Translate API




2. Wikipedia API
