from flask import Flask, request
import operations


app = Flask(__name__)


@app.route("/add")
def add_nums():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a, b)

    return str(result)


@app.route("/sub")
def subtract_nums():
    """Subtract a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a, b)

    return str(result)


@app.route("/mult")
def multiply_nums():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a, b)

    return str(result)


@app.route("/div")
def divide_nums():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a, b)

    return str(result)


OPERATIONS = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}


@app.route("/math/<operation>")
def calc(operation):
    """Do math on a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    operator = OPERATIONS.get(operation)
    result = operator(a, b)

    return str(result)
