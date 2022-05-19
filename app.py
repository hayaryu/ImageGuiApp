# inspired by https://daeudaeu.com/image_rotate/

# standard library
import tkinter

# external library


# my module
from model import Model
from view import View
from controller import Controller

############
### Main ###
############

def main():
    
    app = tkinter.Tk()

    app.geometry("1280x640")
    app.title("Image App")

    model = Model()
    view = View(app)
    controller = Controller(app, model, view)

    app.mainloop()
    
    
if __name__ == '__main__':
    main()
