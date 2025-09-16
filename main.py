import tkinter

from regex import search
from wordfreq import top_n_list, random_words
from english_words import get_english_words_set
from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from word import WordGenerator
from bestscore import BestScore


COLOR_1 = "#E5E0D8"
COLOR_2 = "#F8F8F8"

typed_word_list = []

seconds = 60
seconds_to_min = seconds/60

word_count = 0
character_count = 0

time = None
check_length_wrapper = None

# word_per_minute = word_count/seconds_to_min
# character_per_min = character_count/seconds_to_min








word_generator = WordGenerator()

best_score = BestScore()
score = best_score.read_best_score()[-1]
# best_score.write_best_score(score)

list_of_words = word_generator.generate_list()
copy_list = list_of_words.copy()

word_to_type = ""
correct_char = ""
all_char = ""




for words in list_of_words:
    word_to_type += f"{words} "

#set initial value of max val so user will not be able to type more than length of expected word
max_val = len(list_of_words[0])


formatted_score = score.strip()

#--------------------- Functions Block Begin-----------------------------#

"""TODO: Track when a user deletes and then types, update color in real time"""
def validator(*args):
    global list_of_words, typed_word_list, correct_char, all_char, check_length_wrapper
    if len(all_char) == 0:
        #since the validator function runs after every user entry, the conditional block above ensures the timer starts
        #on the first user entry.
        timer(seconds)

  # Do something when user input character longer then whats expected
    #2
    #Execute function, so far we still have words in our list of words
    if len(list_of_words) != 0:
        #get first word rom the list, which we will use for comparison,
        word_to_check = list_of_words[0]

        #character index is always the last character in word the user has already typed in
        index = len(user_entry.get()) - 1


        #gets position of the current word to check in the text widget, the pos always returns the line no and char no
        #in format line.char(e.g 1.0) Note it gives the position of the whole word, so we have to get the position of
        #each character ourselves, hence we add the index no to get the particular character
        start = "1.0"
        pos = text_t.search(word_to_check, start, stopindex=END)

        word_length = len(word_to_check) - 1
        #split the position into line and character cause, pos will always return in format line.character eg 1.7
        pos_list = pos.split(".")

        #cause pos returns the position of the first letter of the current word we are trying to spell in the text widget
        #we can use the index to then get the current character we are trying bto type in the text widget
        char = int(pos_list[1]) + index

        #char_no gives us the current position of the character we are trying to spell or type in at any point in time
        char_no = f"{pos_list[0]}.0 + {char}c"


        current_word = user_entry.get()[-1]
        #If the last word in user entry is equals same word character in word_to_check, color it blue
        if current_word == word_to_check[index]:
            text_t.tag_add("blue", str(char_no))

            correct_char += current_word #keeps track of correct character entered
            #make character and line number truly dynamic
        else:
            #color it red
            text_t.tag_add("red", str(char_no))
        all_char += current_word
    else:
        #pop ups.
        print("game Over")
        print(f"You got {len(typed_word_list)} words correct")
        print(f"You got {len(correct_char)} words correct")


    #Recompile the textarea.

#This Function validates the user entry and ensures the user cannot type characters longer than the allowable number of
#characters
def validate_entry_length(new_value, max_len):
    global word_to_type, max_val
    #subsequent max_val is updated from inside  validate_entry_length since it runs before user input is registered.
    word_to_type = list_of_words[0]
    max_val = len(word_to_type)  #This dynamically defines the maximum allowable words the user can typo in.
    # print(f"word to type {word_to_type}")
    if len(new_value) <= max_len:
        return True
    return False




#This function ensures that we always work with the first word in the list_of_words list. and it keeps track of the words
#That are typed in correctly by appending them in list typed_word_list
def update_text(event):
    global entry
    user_input = user_entry.get()
    word = list_of_words[0]
    if user_input == word:
        typed_word_list.append(user_input)

    #Removes first word in list
    list_of_words.pop(0)
    #disables the trace_adder function, so we can set the entry to an empty string without triggering the trace_adder function.
    entry.trace_remove("write", trace_adder)
    #sets the content of entry to ""...Nothing
    entry.set("")
    #reactivates the trace adder function, so we can track every entry made into the Entry widget.
    globals()["trace_adder"] = entry.trace_add("write", validator)


def timer(count):
    global time, seconds

    if count == 0:
        #pop up
        print("End")
        print(len(typed_word_list))
        window.after_cancel(time)
        user_entry.state(["disabled"])

        time_text.itemconfig(time_count, text=0)
    else:
        time = window.after(1000, timer, count-1)
        time_text.itemconfig(time_count, text=count)

        #records words and characters per minute.
        get_word_and_character_per_min(count, typed_word_list, wpm, wpm_score)
        get_word_and_character_per_min(count, all_char, cpm, cpm_score)

        #write best score to file.





#This function calculates character or words typed per minute
def get_word_and_character_per_min(seco, list_or_string, canvas_item, canvas_var):
    global typed_word_list

    amount_of_c_words = len(list_or_string)
    sec = 60 - seco
    if sec == 0:
        pass
    else:
        sec_to_min = sec/60
        word_p_min = round(amount_of_c_words/sec_to_min)
        canvas_item.itemconfig(canvas_var, text=word_p_min)
























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
cpm_score = cpm.create_text(10, 30, text="0", font=("Calibri", 13))

#-------#

#-------#
wpm_label = ttk.Label(frame_1, text="WPM:", font=("Calibri", 13), background=COLOR_1)
wpm_label.grid(column=4, row=0, sticky="ew", padx=(90,0))

wpm = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
wpm.grid(column=5, row=0)
wpm_score = wpm.create_text(10, 30, text="0", font=("Calibri", 13))
#-------#

#--------#
time_left_label = ttk.Label(frame_1, text="Time left:", font=("Calibri", 13), background=COLOR_1)
time_left_label.grid(column=6, row=0, sticky="w", padx=(30, 0))

time_text = Canvas(frame_1, width=50, height=60, background=COLOR_1, highlightthickness=0)
time_text.grid(column=7, row=0, padx=(0, 0))
time_count = time_text.create_text(10, 30, text="60", font=("Calibri", 13))
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
check_length_wrapper = (window.register(lambda P: validate_entry_length(P, max_val)), "%P")

user_entry = ttk.Entry(frame_3, textvariable=entry, width=20, font=("Calibri", 20), justify="center", validate="key", validatecommand=check_length_wrapper)
user_entry.bind("<Return>", update_text)


user_entry.grid(column=0, row=0, padx=(200, 0), pady=(30, 0))

trace_adder = entry.trace_add("write", validator)





window.mainloop()