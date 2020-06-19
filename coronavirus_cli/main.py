
from interface.command import StartCommand
from cleo import Application

app = Application()
app.add(StartCommand())

if __name__ == '__main__': 
    app.run()