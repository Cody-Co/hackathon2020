from flask import Flask, Response, render_template, request
from wtforms import Form, StringField, SelectField
from threading import Thread
import ast
app = Flask(__name__)



@app.route('/')
def home():
    #query = request.args('search') 
    return render_template("welcome.html")

@app.route('/', methods=['POST'])
def search_bar():
    if request.method == "POST":
        text = request.form['u']
        professor = final_search(text)
        professor = sort_list(professor)
        return render_template('results.html', professors=professor)


def sort_list(dictionary):
    professors = sorted(dictionary, key = lambda i: i['rating'], reverse=True)
    return professors 



def final_search(searchtext):

    search = searchtext
    with open("data.txt", 'r') as f:
        lines = f.readlines()
        professors = lines[0].replace("\n","")
        classes = lines[1]

    professors = ast.literal_eval(professors)
    classes = ast.literal_eval(classes)

    #search = input("Enter class name: ")

    prof_hashes = classes[search]
    profiles = []
    temp = {}
    final_output = []
    for i in prof_hashes:
        profiles.append(professors[i])
    for items in profiles:
        temp["name"] = items[0]
        temp["rating"] = items[1]
        temp["take_again"] = items[2]
        final_output.append(temp)
        temp = {}
    return final_output

if __name__ == '__main__':
    app.run(debug=True) 