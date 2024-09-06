import urllib.request
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


@app.route("/list")
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {"name": character["name"], "status": character["status"]}
        characters.append(character)

    return {"characters": characters}

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)

    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])

@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)

    data = response.read()
    dict = json.loads(data)

    characters = []
    for character in dict["residents"]:
        character_data = urllib.request.urlopen(character)
        character_data = character_data.read()
        character_dict = json.loads(character_data)
        characters.append({
            "name": character_dict["name"],
            "id": character_dict["id"]
        })
    dict["residents"] = characters

    return render_template("location.html", location=dict)

@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"  
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"])

@app.route("/episodes/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    characters = []
    for character in dict["characters"]:
        character_data = urllib.request.urlopen(character)
        character_data = character_data.read()
        character_dict = json.loads(character_data)
        characters.append({
            "name": character_dict["name"],
            "id": character_dict["id"]
        })
    dict["characters"] = characters
    return render_template("episode.html", episode=dict)


if __name__ == "__main__":
    app.run(debug=True)
