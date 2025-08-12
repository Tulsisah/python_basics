<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Static HTML Page</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
