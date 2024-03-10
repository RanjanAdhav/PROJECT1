# Python Program to create a Simple GUI
# Calculator using Tkinter

#import everything from tkinter module
from tkinter import *

# Globally declare the expression variable
expression = ""

# Funtion to update expression in the text entry box.
def press(num):
    #point out the global expression variable
    global expression 
    # Concatenate String
    expression = expression + str(num) 
#Update the expression by using set method
    equation.set(expression) 

#Function to evaluate the final expression
def equalpress():
        #Try & expect statement is used for handling the error
        #put that code inside the try block which may generate error
    try:
        #Evalute expression & str function convert
        global expression 
        total = str(eval(expression))
        equation.set(total)
        #Expression variable by empty str
        expression = "" 

#if error is generate handle by except block
    except:  
        equation.set("error")
        expression = ""

# Function to clear the contents of text entery box
def clear():
    global expression
    expression = ""
    equation.set("")

#Driver code
if __name__ == "__main__":
    # Create GUI window 
    gui = Tk()  

# set background color of GUI window
    gui.configure(background="light Yellow") 
    #set title of GUI window.
    gui.title("Python Calculator") 
    #set configuration of GUI window.
    gui.geometry("390x270") 
    #We create instance this class
    equation = StringVar() 
    #Create text entry box for showing expression
    expression_field = Entry(gui, textvariable=equation) 
    #Grid method is used for placing widgets at respective positions
    expression_field.grid(columnspan=6, ipadx=90) 

    #Create Buttons & Place at a particular, Location inside the root window.
    #When user press the button, the command or function affiliated to that button executed.
    button1 = Button(gui, text=' 1 ', fg='red', bg='pink',
                     command=lambda: press(1), height=2, width=9)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='red', bg='pink',
                     command=lambda: press(2), height=2, width=9)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='red', bg='pink',
                     command=lambda: press(3), height=2, width=9)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='red', bg='pink',
                     command=lambda: press(4), height=2, width=9)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='red', bg='pink',
                     command=lambda: press(5), height=2, width=9)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='red', bg='pink',
                     command=lambda: press(6), height=2, width=9)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='red', bg='pink', 
                    command=lambda: press(7), height=2, width=9) 
    button7.grid(row=4, column=0) 

    button8 = Button(gui, text=' 8 ', fg='red', bg='pink', 
                    command=lambda: press(8), height=2, width=9) 
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='red', bg='pink', 
                    command=lambda: press(9), height=2, width=9) 
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='red', bg='pink', 
                    command=lambda: press(0), height=2, width=9) 
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='brown', bg='white',
                  command=lambda: press("+"), height=2, width=9)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='brown', bg='white',
                  command=lambda: press("-"), height=2, width=9)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='brown', bg='white',
                  command=lambda: press("*"), height=2, width=9)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='brown', bg='white',
                  command=lambda: press("/"), height=2, width=9)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='brown', bg='white',
                  command=equalpress, height=2, width=9)
    equal.grid(row=5, column=2)

    clear = Button(gui, text=' Clear ', fg='white', bg='black',
                  command=clear, height=2, width=9)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='red', bg='pink',
                    command=lambda: press('.'), height=2, width=9)
    Decimal.grid(row=6, column=0)

    #Start the GUI
    gui.mainloop()
