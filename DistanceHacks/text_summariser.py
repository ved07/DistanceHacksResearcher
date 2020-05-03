
from appJar import gui
import summa
import wikipedia

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        topic = app.getEntry("Research Topic")
        limit = app.getEntry("Words Limit")
        text = wikipedia.page(topic).content
        summary = summa.summarizer.summarize(text, words=int(limit))
        file_new = open(topic+'.txt', 'a+')
        file_new.write(summary)
        file_new.close()
        app.stop()

        newApp= gui("Researched", "400x200")
        newApp.addScrolledTextArea('app', text = summary)
        newApp.go()


# create a GUI variable called app
app = gui("AutoResearcher", "400x200")

app.setFont(size=20, family="Times New Roman", underline=True )
app.setButtonFont(size=14, family="Verdana", underline=False, slant="roman")

app.setBg("light gray")

app.addLabel("title", "Auto-Researcher")



app.setLabelFg("title", "black")

app.addLabelEntry("Research Topic")

app.addLabelEntry("Words Limit")

app.addButtons(["Write Research", "Cancel"], press)

app.setFocus("Research Topic")

app.setBgImage('bgd.jpg')


app.go()

