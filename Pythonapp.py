import requests
def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6eca69341ec64cbe81055f003ef578db.mailgun.org/messages",
        auth=("api", "2dbcea6e515b8c91a9271664618d809f-de7062c6-bb2cb17d"),
        data={"from": "Excited User <mailgun@sandbox6eca69341ec64cbe81055f003ef578db.mailgun.org>",
              "to": email,
              "subject": "Pub Quiz",
              "text": "The correct answers were Kaley Cuoco, Boston, and Ben-Hur! "})

              

from flask import Flask, render_template, request #second one is capitalised, module and then library
app = Flask("MailTestApp")
@app.route("/") #Decorator - telling it where to get it from
def hello():
    return "Quiz --> got to ....../quiz"

@app.route("/EndQuiz", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data
    #problem with all the different forms in html doc
    #the form that redirects to "/EndQuiz" doesnt have an email feild
    #once that is sorted you need to parse <form_data['email']> in to the send_simple_message() funtion
    #print form_data['email']
    send_simple_message(form_data)
    return render_template("finished.html")


#can only display static webpages, cannot do dynamic, can only host locally

@app.route("/quiz")
def hello_someone():
    return render_template("quiz.html")



app.run(debug=True) #doesn't debug the code - just calls you out when you've screwed up
app.run()

response.text
