import tkinter

from regex import search
from wordfreq import top_n_list, random_words
from english_words import get_english_words_set
from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from word import WordGenerator
from bestscore import BestScore
import re

COLOR_1 = "#E5E0D8"
COLOR_2 = "#F8F8F8"

typed_word_list = []

seconds = 60
seconds_to_min = seconds/60

word_count = 0
character_count = 0

word_per_minute = word_count/seconds_to_min
character_per_min = character_count/seconds_to_min








word_generator = WordGenerator()

best_score = BestScore()
score = best_score.read_best_score()[-1]
# best_score.write_best_score(score)

list_of_words = word_generator.generate_list()
copy_list = list_of_words.copy()

word_to_type = ""


for words in list_of_words:
    word_to_type += f"{words} "



formatted_score = score.strip()

#--------------------- Functions Block Begin-----------------------------#

#The trick is to always compare first word in the list
def validator(*args):
    #2
    global list_of_words
    word_to_check = list_of_words[0]

    index = len(user_entry.get()) - 1
    start = "1.0"
    pos = text_t.search(word_to_check, start, stopindex=END)

    word_length = len(word_to_check) - 1
    pos_list = pos.split(".")
    char = int(pos_list[1]) + index
    char_no = f"{pos_list[0]}.0 + {char}c"




    if user_entry.get()[-1] == word_to_check[index]:
        #Count correct Character Here
        # print(char_no)
        text_t.tag_add("blue", str(char_no))
        pos = text_t.search(word_to_check, start, stopindex=END)
        print(pos)
        print(text_t.index(pos))
        #make character and line number truly dynamic
    else:
        print("False")
        text_t.tag_add("red", str(char_no))


    #Recompile the textarea.




def update_text(event):
    global entry
    user_input = user_entry.get()
    word = list_of_words[0]
    if user_input == word:
        typed_word_list.append(user_input)
    print(typed_word_list)
    #Removes first word in list
    list_of_words.pop(0)
    entry.trace_remove("write", trace_adder)
    entry.set("")
    globals()["trace_adder"] = entry.trace_add("write", validator)













def timer():
    pass


















#-------------------- Function Block End --------------------------------#






window = Tk()
window.title("Typing Speed Calculator")
window.wm_maxsize(width=700, height=700)
window.configure(height=700, width=700)

style_1 = ttk.Style()
custom_font = tkfont.Font(family="Calibri", size=16, weight="bold")
style_1.configure("TLabel", foreground="black", font=custom_font)

entry = StringVar()


#---------------------------Frame1-------------------------#
frame_1 = Frame(window, height=50, width=700, background=COLOR_1)
frame_1.grid(column=0, row=0, sticky="ew")



#Prevent shrinking of frame to label size
frame_1.grid_propagate(False)
# frame_1.columnconfigure(0, weight=0)
# frame_1.columnconfigure(1, weight=0)


#-------#
best_label = ttk.Label(frame_1, text="Best:", font=("Calibri", 13), background=COLOR_1)
best_label.grid(column=0, row=0, sticky="ew", padx=(70, 0))

score = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
score.grid(column=1, row=0)
score.create_text(10, 30, text=formatted_score, font=("Calibri", 13))
#-------#

#-------#
cpm_label = ttk.Label(frame_1, text="Corrected CPM:", font=("Calibri", 13), background=COLOR_1)
cpm_label.grid(column=2, row=0, sticky="ew")

cpm = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
cpm.grid(column=3, row=0)
cpm.create_text(10, 30, text="0", font=("Calibri", 13))

#-------#

#-------#
wpm_label = ttk.Label(frame_1, text="WPM:", font=("Calibri", 13), background=COLOR_1)
wpm_label.grid(column=4, row=0, sticky="ew", padx=(90,0))

wpm = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
wpm.grid(column=5, row=0)
wpm.create_text(10, 30, text="0", font=("Calibri", 13))
#-------#

#--------#
time_left_label = ttk.Label(frame_1, text="Time left:", font=("Calibri", 13), background=COLOR_1)
time_left_label.grid(column=6, row=0, sticky="w", padx=(30, 0))

time = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
time.grid(column=7, row=0, padx=(0, 0))
time.create_text(10, 30, text="60", font=("Calibri", 13))
#--------#



"""TEXT"""
#--------------------------Frame2---------------------------#
frame_2 = Frame(window, height=550, width=700, background=COLOR_2)
frame_2.grid(column=0, row=1)
frame_2.grid_propagate(False)
#Explore the use of Textwidget instead of canvas

text_t = Text(frame_2, width=50, height=550, font=("Calibri", 20), wrap="word")

text_t.tag_configure("red", foreground="red")
text_t.tag_configure("blue", foreground="blue")

text_t.insert("end", word_to_type)
text_t.grid(column=0, row=0)

# canvas_text = Canvas(frame_2, width=700, height=550)
# word_on_canvas = canvas_text.create_text(355, 275,
#                         text=f"{word_to_type}",
#                         font=("Calibri", 20),
#                         width=400)
# canvas_text.grid(column=0, row=0)

"""USER ENTRY"""
#-------------------------------Frame3----------------------#
frame_3 = Frame(window, height=100, width=700, background=COLOR_1)
frame_3.grid(column=0, row=2)
frame_3.grid_propagate(False)

user_entry = ttk.Entry(frame_3, textvariable=entry, width=20, font=("Calibri", 20), justify="center")
user_entry.bind("<Return>", update_text)


user_entry.grid(column=0, row=0, padx=(200, 0), pady=(30, 0))

trace_adder = entry.trace_add("write", validator)




window.mainloop()