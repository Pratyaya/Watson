from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from watson_developer_cloud import AssistantV1
import json

# watson object with authentication parameters.

assistant = AssistantV1(
    version='2018-02-16',
    username='0d872469-cae6-4e25-8af5-d4422934861d',
    password='zAgDleevRDIJ'
)


app = Flask(__name__)

# To Handle default webpage.
 
@app.route("/")
def index():
    quote = "'Mathematics is the key and door to the sciences.' -- Galileo Galilei"
    return render_template('index.html',**locals())


# This is to handle incoming messages, sending message to watson assistant and sending response back to chat window.

@app.route("/sendMsg", methods=['POST'])
def sendMsg():
    msg =  request.form['msg'];

    response = assistant.message(
    workspace_id='22fe096a-bf73-47ee-b14b-5d109f6c905d',
    input={
        'text': msg
	    }
    )
    res = response["output"]["text"][0]
    return json.dumps({'status':'OK','msg':msg,'res':res});

# This is to open the chat page.
 
@app.route("/chat")
def chat():
    quote = "'To understand recursion you must first understand recursion..' -- Unknown"
    return render_template('chat.html',**locals())

# This is AJAX call for quotes - Example of Ajax.
@app.route("/quotes.txt")
def quote():
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    return quote

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

