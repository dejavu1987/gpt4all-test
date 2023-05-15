from flask import Flask, render_template, request
from gpt4allj import Model

gptj = Model(
    "./models/ggml-gpt4all-j-v1.3-groovy.bin")

app = Flask(__name__)

print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    prompt = request.form['prompt']
    response = gptj.generate(prompt, reset=False)
    answer = response
    return render_template('index.html', prompt=prompt, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
