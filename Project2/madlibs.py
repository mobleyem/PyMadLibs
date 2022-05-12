from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_1.html", madlib=[1,2])

@app.route("/madlib/1", methods=["post"])
def madlib_1():
    adj = str(request.form["adjective"])
    verb1 = str(request.form["verb1"])
    verb2 = str(request.form["verb2"])
    famous_person = str(request.form["famous person"])

    madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    return(madlib)   

@app.route("/madlib/2", methods=["post"]) 
def madlib_2():
    adj2 = str(request.form["adjective"])
    noun = str(request.form["noun"])
    bodypart = str(request.form["bodypart"])

    madlib2 = f"I'm obsessed with my new tattoo, its so {adj2}! I can't wait to get another, it's going to be a {noun}. I'm \
going to get it on my {bodypart}!"

    return(madlib2)

if __name__ == '__main__':
    app.run(debug=True)







#adj = input("adjective: ")
#verb1 = input("verb: ")
#verb2 = input("verb: ")
#famous_person = input("Famous person: ")

#madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
#I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

#print(madlib)   

#adj= input("adjective: ")
#noun1= input("noun: ")
#bodypart= input("bodypart: ")

#madlib2 = f"I'm obsessed with my new tattoo, its so {adj}! I can't wait to get another, it's going to be a {noun1}. I'm \
#going to get it on my {bodypart}!"

#print(madlib2)