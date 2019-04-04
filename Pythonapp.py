import requests
def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox702a91bc2cda4ccfa9b34ec392ec97c6.mailgun.org/messages",
        auth=("api", "0ba03e8b82436321a1ad545f8e874089-2416cf28-d0808bd0"),
        data={"from": "Quiz Team <mailgun@sandbox702a91bc2cda4ccfa9b34ec392ec97c6.mailgun.org>",
              "to": email,
              "subject": "Pub Quiz",
              "text": "The correct answers were Kaley Cuoco, Boston, and Ben-Hur! "})


from flask import Flask, render_template, request #second one is capitalised, module and then library
app = Flask("MailTestApp")
@app.route("/") #Decorator - telling it where to get it from
def hello():
    return "Quiz --> got to ....../quiz"

@app.route("/EndQuiz", methods=["POST"])
def save_form():
    form_data = request.form
    print form_data
#    email = form_data["email"]
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
