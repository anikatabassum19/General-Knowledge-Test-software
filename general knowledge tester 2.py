import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x600')
window.title("GK tester tutorial")
window.configure(background = '#000000')
window.resizable(0,0)

number = random.randrange(0,11)

questions = ['Who was the first prime minister of Bangladesh?',
             'In which year Issac Newton was born?',
             'In which year did bangladesh became\n an independent country?',
             'Which district of Bangladesh\n was part of Asam?',
             'Hitler party which came into power\n in 1933 is known as (one word)',
             'Epsom in England is the place associated with?',
             'First human heart transplant operation\n conducted by Dr. Christiaan Barnard was\n conducted in which year?',
             'Golf player Vijay Singh is a \ncitizen of which country?',
             'First Afghan War took place in which year?',
             'During World War II, in which year\n did Germany attack France?',
             'Which animal caused Filaria?',
             'Coral reefs in India can be found in??']

answer = ['tajuddin ahmed',
          '1642',
          '1971',
          'sylhet',
          'nazi',
          'horse racing',
          '1967',
          'fiji',
          '1839',
          '1940',
          'mosquito',
          'rameshwaram',]


    

label = tk.Label(window,
                 text = 'Enter Answer Here',
                 font = ('Comics an sms',15,'bold'),
                 bg = '#000000',
                 fg = '#ffffff',
                 )
label.pack(pady = 30)

entry = tk.Entry(window,
                 font = ('Arial',20),
                 width = 25,
                 bg = 'powder blue',
                 insertwidth = 5,
                 )

entry.pack()



check_button = tk.Button(window,
                         text = 'Check',
                         width = 16,
                         font = ('Comic sans ms',20,'bold'),
                         bg = '#4C4B4B',
                         fg = '#6ab04c',
                         relief = tk.RAISED,
                         cursor = 'hand2',
                         )
check_button.pack(pady = 30)

reset_button = tk.Button(window,
                         text = 'Reset',
                         width = 16,
                         font = ('Comic sans ms',20,'bold'),
                         bg = '#4C4B4B',
                         fg = '#EA425C',
                         relief = tk.RAISED,
                         cursor = 'hand2',
                        )

reset_button.pack(pady = 30)




















