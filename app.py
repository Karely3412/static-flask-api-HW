from flask import Flask , jsonify
# Jsonify is another func that will convert it into a json format


app = Flask(__name__)  # <-- here we are setting our Flask class name.. 
#..(flask needs to be capitalized because it's a class name & we have to use dunder init name as well)


data = [
    {
        "id": "1",
        "name": "Denzel Washington",
        "occupation": "actor",
        "movie": "Man on Fire",
    },
    {
        "id": "2",
        "name": "Angelina Jolie",
        "occupation": "actor",
        "movie": "Tumb Raidor",
    },
    {
        "id": "3",
        "name": "Tom Hardy",
        "occupation": "actor",
        "movie": "Man on Fire",
    },
    {
        "id": "4",
        "name": "Johnny Depp",
        "occupation": "actor",
        "movie": "Public Enemies",
    },
    {
        "id": "5",
        "name": "Keanu Reeves",
        "occupation": "actor",
        "movie": "John Wick",
    },
    {
        "id": "6",
        "name": "Gerard Butler",
        "occupation": "actor",
        "movie": "Phantom of the Opera",
    }


]


@app.route('/my-url')  # <-- try naming the route something that'll make sense.
def test_route(): # <-- try naming the func something that'll make sense.
    return jsonify("hello world")
# TESTED IN BROWSER


@app.route('/all_actors')
def get_all_actors():
    return jsonify(data), 200
# TESTED IN POSTMAN


@app.route('/actor/<id>') # <-- the <id> will generate a variable in your flask request, then pass that into the route func. (the one right below) 
def get_actors_by_id(id):

    # QUESTION? ask about the conditional syntax.
    for actor in data:
        if actor['id'] == id:
            return jsonify(actor), 200
    return jsonify('Actor Not Listed'), 404
# TESTED IN POSTMAN



if __name__ == "__main__":  # <-- why we're doing this if statement w/ __name__, is because.. 
    # ..it's a python system variable that will tell the app where it's running from whether it's locally or remotely tp locate the route.

    # QUESTION? how are these variable names working? Just abit confused.

    app.run(port="8082", host="0.0.0.0")  # <-- here the 1st parameter will set the port number we'd like to use..
    # ..& the 2nd one will allow the computer to listen to any availible IP addresss that the computer has.