import requests
def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2d1816a7301044609f33f7ca54f560be.mailgun.org/messages",
        auth=("api", "3018c97283cb2b10930699e29802a5d5-de7062c6-fe66ae0c"),
        data={"from": "Quiz Team <mailgun@sandbox2d1816a7301044609f33f7ca54f560be.mailgun.org>",
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

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

app.run(debug=True) #doesn't debug the code - just calls you out when you've screwed up
app.run()

response.text
