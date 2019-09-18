from flask import Flask, request, jsonify

app = Flask(__name__)

responses = []

@app.route('/submit/<message>')
def handleClueRequest(message):
    responses.append(message)
    return "submitted"

@app.route('/responses')
def showResponses():
    html = "".join(map(lambda response: '<div class="message-wrapper">' + response + '</div>', responses))
    return '<h1>Responses</h1> <div class="container">' + html + '</div>' + '''
        <style>
            .container {
                margin: 20px;
                max-width: 800px;
            }

            .message-wrapper:nth-child(odd) {
                background: #c4c4c4;
            }

            .message-wrapper:nth-child(even) {
                background: #f2f2f2;
            }

            .message-wrapper {
                padding: 5px;
                font-size: 20px;
                font-family: Geneva;
            }
        </style>
    '''

@app.route('/')
def showInputPage():
    return '''
        <head>
            <title>SIGNLL</title>
            <link rel="shortcut icon" type="image/png"
                href="https://icon-library.net/images/icon-pencil/icon-pencil-27.jpg"/>
        </head>
        <textarea
            autofocus
            style="margin: 20px; width:500px; height:150px; resize:none"
            placeholder="Type a response here and hit Enter to submit :)"></textarea>
        <script>
            document.querySelector("textarea").addEventListener("keydown", function(e) {
                if (e.key === "Enter") {
                    fetch(window.location.href + 'submit/' + e.currentTarget.value)
                    document.body.innerHTML = "Your response has been submitted! Refresh to submit another response."
                }
            })
        </script>
    '''

if __name__ == '__main__':
   app.run(host='0.0.0.0')