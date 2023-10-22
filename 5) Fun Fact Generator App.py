import requests
import tkinter


def get_fact():
    parameters = {
        "language": "en"
    }

    response = requests.get(
        "https://uselessfacts.jsph.pl/api/v2/facts/random", params=parameters)

    data = response.json()
    return data["text"]


def display_fact():
    canvas.itemconfig(fact, text=get_fact())


window = tkinter.Tk()

window.title("Fun Fact Generator APP")
window.geometry("400x400")


canvas = tkinter.Canvas(height=300, width=300)
background_image = tkinter.PhotoImage(file="./images/card_back.png")
canvas.create_image(150, 207, image=background_image)
canvas.pack()
fact = canvas.create_text(150, 150, text=get_fact(),
                          width=300, font=("Roboto", 18))


button = tkinter.Button(text="New Fact", command=display_fact)
button.pack()

window.mainloop()
