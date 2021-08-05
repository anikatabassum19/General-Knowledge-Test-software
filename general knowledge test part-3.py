Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@anikatabassum19 
anikatabassum19
/
general-knowledge-software-part-3
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
general-knowledge-software-part-3/general knowledge tester 2.py /
@anikatabassum19
anikatabassum19 Add files via upload
Latest commit 00f3a5f on Jun 24, 2020
 History
 1 contributor
141 lines (100 sloc)  3.85 KB
  
import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x600')
window.title("GK tester tutorial")
window.configure(background = '#000000')
window.resizable(0,0)

number = random.randrange(0,11,1)

score = 0

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
def default_ques():
    global questions,number,answer
    number = random.randrange(0,11,1)
    label.config(text = questions[number])        


def check_answer(event = None):
    global questions,answer,number,score
    answer_input = display.get()
    if answer_input == answer[number]:
        score += 1
        messagebox.showinfo("Correct!",'You scored ' + str(score) + ' point')
        score_widget.config(text = 'Score: ' + str(score))
        default_ques()
        
        
    else:
        messagebox.showinfo("Wrong!",'The answer is ' + str(answer[number]))
    display.delete(0,tk.END)
    
def reset_ques():
    global questions,answer,number
    number = random.randrange(0,11)
    label.config(text = questions[number])
    display.delete(0,tk.END)    


score_widget= tk.Label(window,
                       font = ('Comics an sms',15),
                       text = 'Score: ' + str(score),
                       bg = '#000000',
                       fg = '#ffffff',
                       )

score_widget.pack()

label = tk.Label(window,
                 text = 'Enter Answer Here',
                 font = ('Comics an sms',15,'bold'),
                 bg = '#000000',
                 fg = '#ffffff',
                 )
label.pack(pady = 30)

display = tk.Entry(window,
                 font = ('Arial',20),
                 width = 25,
                 bg = 'powder blue',
                 insertwidth = 5,
                 )

display.pack()



check_button = tk.Button(window,
                         text = 'Check',
                         width = 16,
                         font = ('Comic sans ms',20,'bold'),
                         bg = '#4C4B4B',
                         fg = '#6ab04c',
                         relief = tk.RAISED,
                         cursor = 'hand2',
                         command = check_answer,
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
                         command = reset_ques,
                        )

reset_button.pack(pady = 30)


default_ques()

window.bind("<Return>",check_answer)
window.mainloop()

