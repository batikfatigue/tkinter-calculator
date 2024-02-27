# reference site: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

# import the tkinter module
import tkinter # 'import *' brings all the functions into our namespace

expression = '' # instantiate the math statement

def press(num):
    global expression
    expression += str(num)
    equation.set(expression) # equation here is going to be StringVar() from tk

def equate():
    try: 
        global expression
        total = str(eval(expression)) # eval basically just evaluates a math statement
        equation.set(total)
        expression = ''

    except:
        equation.set('Error!')
        expression = ''

def clear():
    global expression
    expression = ''
    equation.set('')

# ensures that script is ran directly
if __name__ == '__main__':
    gui = tkinter.Tk()

    equation = tkinter.StringVar()

    gui.configure(background='#1460eb')
    gui.title('Justin\'s first calculator')
    gui.geometry('500x500') # sets the size of window

    expression_field = tkinter.Entry(gui, textvariable=equation, font=('Arial', 14))
    expression_field.grid(column=0, row=0, columnspan=4, sticky='ew')

    num = 1
    matrix = [0,0] # matrix for numpad
    for row in range(2,5):
        for column  in range(4):
            if column < 3 and row > 1:
                button = tkinter.Button(gui, text=str(num), fg='white', bg='#555556', height=1, width=7, command=lambda num=num:press(str(num)))
                button.grid(row=row, column=column)
                num += 1
            matrix[1] += 1
        matrix[0] += 1

    buttonClear = tkinter.Button(gui, text='C', fg='white', bg='#555556', height=1, width=7, command=lambda:clear())
    buttonClear.grid(row=1, column=0)
    
    operators = ('/','*','-','+')
    for row in range(1,4):
        operator = operators[row-1]
        button = tkinter.Button(gui, text=operator, fg='white', bg='#555556', height=1, width=7, command=lambda operator=operator:press(operator))
        button.grid(row=row, column=3)

    buttonEquate = tkinter.Button(gui, text='=', fg='white', bg='#555556', height=1, width=7, command=lambda:equate())
    buttonEquate.grid(row=4, column=3)

    gui.mainloop() 