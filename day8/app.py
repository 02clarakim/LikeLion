import os
import openai

from flask import Flask, render_template, request
openai.api_key = "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"

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def new_web():
    if request.method == 'POST':
        response = openai.Completion.create(
            engine="davinci",
            prompt=request.form['msg'],
            temperature=0.7,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        user_msg = request.form['msg'] + response["choices"][0]["text"]
    else:
        user_msg = "Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction"
    return render_template('index.html', output_msg=user_msg)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)