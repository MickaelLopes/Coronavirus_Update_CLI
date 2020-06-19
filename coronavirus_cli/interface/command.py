from cleo import Command

class StartCommand(Command):
    """
    Start Command 

    start
    """ 
    def handle(self):
        
        self.line("Greetings and Welcome")