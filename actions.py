import requests
import datetime

def get_swansoned():

    response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")
    remove_chars = ["[", "\"", "]"]
    clean_string = response.text
    for char in remove_chars:
        clean_string = clean_string.replace(char, "")
    clean_string +=  "\n -Ron Swanson"
    return clean_string


def cat_me():
    url = "https://cat-fact.herokuapp.com/facts/random?amount=1"
    response = requests.get(url)
    fact = response.json()
    fact = fact["text"]
    return fact

def random_cat():
    url = "https://aws.random.cat/meow"
    response = requests.get(url)
    url = response.json()["file"]
    return url

def random_dog():
    url = "https://random.dog/woof.json"
    response = requests.get(url)
    return response.json()["url"]

def random_chuck():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    return response.json()["value"]

def foaas(args):
    url = "http://foaas.com/"
    for arg in args:
        url += arg + "/"
    url = url.rstrip("/")
    response = requests.get(url, headers={"Accept":"application/json"})
    if response.status_code != 200:
        return "Invalid"
    try:
        dic = response.json()
        fstring = ''
        for k, v in dic.items():
            fstring += v +"\n"
        fstring.rstrip("\n")
        return fstring
    except Exception as e:
        return "You broke the bot good job"


def steam_chart():
    url = "https://steamcharts.com/app/976730/chart-data.json"
    response = requests.get(url)
    data = response.json()

    ts_epoch = data[-1][0]/1000 #fromtimestamp() method expects argument in seconds, but javascript uses milliseconds doi
    ts = datetime.datetime.fromtimestamp(ts_epoch)
    return ts.time(), data[-1][1]

if __name__ == "__main__":
    steam_chart()