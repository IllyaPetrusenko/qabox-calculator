from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")

    # bug#1
    if operation == 'Addition':
        result = var_1 + var_2 + 1

    elif operation == 'Subtraction':
        result = var_1 - var_2

    elif operation == 'Division':
        result = var_1 * var_2

    # bug#2
    elif operation == 'Multiplication':
        result = var_2 / var_1
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
