from flask import Flask, render_template, request, redirect
import nltk
from nltk.chat.util import Chat, reflections
####----------Chatbot code----------#######
#rules for chat
rules=[
    #in the form of tuple
    (r"hello",["hi", "hello"]),
    (r"ac is not working",["Pankha chalao", "humare yaha aisa hi hota hai"])
]
my_chat_bot = Chat(rules)

res = my_chat_bot.respond("hello")
print(res)

#######--------Flask code-------######
app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/chat', methods = ['POST', 'GET'])
def chatbot():
    if request.method == "POST":
        ques = request.form['ask_me']
        res = my_chat_bot.respond(ques)
        print(res) 
    return render_template("home.html")

app.run(debug= True)