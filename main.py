
from cgitb import text
from email.mime import image
from tkinter import *
import random
from pygame import mixer
import time
import pygame
#============================================================================
#____________________________________________________________________________
theme_list = [['#15202b', '#192734'], ['#121212', '#181818']]
#darkblue, dark
#____________________________________________________________________________
current_bg = theme_list[0]
fg_current = '#0eff62'
#============================================================================
mixer.init()

music_on = False
sound_on = True

def play_music():
    global music_on
    mixer.music.load(random.choice(["3.mp3"]))
    mixer.music.set_volume(0.1)
    music_on = not music_on
    mixer.music.play() if music_on else mixer.music.stop()
    

def play_SFX(case):
    if sound_on:
        if case == 'win':
            sound_effect = pygame.mixer.Sound('win.wav')
            sound_effect.set_volume(0.2)
            sound_effect.play()
        elif case == 'draw':
            sound_effect = pygame.mixer.Sound('draw.wav')
            sound_effect.set_volume(0.2)
            sound_effect.play()
        elif case == 'keypress':
            sound_effect = pygame.mixer.Sound('kp.wav')
            sound_effect.set_volume(0.3)
            sound_effect.play()
def sound_switch():
    global sound_on
    sound_on = not sound_on 

#=============================================================================
window = Tk()
window.title('Tic Tac Toe')
window.minsize(930,600)
window.state('zoomed')
#bg_image = PhotoImage(file = "sunset.png")
#image_label = Label(window, image = bg_image)
#window.wm_attributes("-transparent", 'grey')
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
#window.geometry("%dx%d"%(width, height))
#window.attributes('-fullscreen', True)
icon = PhotoImage(file = "ttt.png")
window.iconphoto(False, icon)
#==========================================================================================

def switch_theme():
    global current_bg, theme_list, cells
    xs_turn_indicator.config(bg = current_bg[1])
    os_turn_indicator.config(bg = current_bg[1])
    os_turn_indicator.config(fg = current_bg[0]) if x_turn else xs_turn_indicator.config(fg = current_bg[0])
    for cell in cells:
        cell.config(bg = current_bg[0] if cells.index(cell)%2==0 else current_bg[1])
    if current_bg != theme_list[2]:
        window.config(bg = current_bg[0])    
def switch_theme_to_dark():
    global current_bg,image_label,bg_image
    current_bg = theme_list[1]
    switch_theme()
    image_label.destroy()  
def switch_theme_to_darkblue():
    global current_bg,image_label,bg_image
    current_bg = theme_list[0]
    switch_theme()
    image_label.destroy()
'''
def switch_theme_to_ss():
    global current_bg,xs_turn_indicator,os_turn_indicator,cells
    current_bg = theme_list[2]

    #xs_turn_indicator.attributes('-trasparentcolor', current_bg[1])
    #os_turn_indicator.attributes('-trasparentcolor', current_bg[1])
    #os_turn_indicator.config(fg = current_bg[0]) if x_turn else xs_turn_indicator.config(fg = current_bg[0])
    #for cell in cells:
    #    cell.attributes('-trasparentcolor', current_bg[0]) if cells.index(cell)%2==0 else cell.wm_attributes('trasparentcolor', current_bg[0])
    #window.config(bg = current_bg[0])
    switch_theme()
    

    image_label.place(x=0,y=0)'''
#===========================================================================================


def restart():
    global cells, count, x_turn, won,draw, popped_up
    if won or draw:
        top.destroy()
    for cell in cells:
        cell.config(text = '', fg = fg_current)
    count = 0
    x_turn = False
    indicate_turn()
    won = False
    draw = False
    popped_up = False




menubar = Menu(window)

optionmenu = Menu(menubar, tearoff=0, fg = 'azure', bg=current_bg[1])
optionmenu.add_command(label="Restart", command=restart)
optionmenu.add_command(label="Sound", command=sound_switch)
optionmenu.add_command(label="Music", command=play_music)
optionmenu.add_separator()
optionmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Options", menu=optionmenu)

thememenu = Menu(menubar, tearoff=0, fg = 'azure' , bg=current_bg[1])
#thememenu.add_command(label="Undo", command=donothing)
thememenu.add_command(label="dark", command=switch_theme_to_dark)
thememenu.add_command(label="darkblue", command=switch_theme_to_darkblue)
menubar.add_cascade(label="theme", menu=thememenu)
window.config(menu = menubar)
window.config(bg = current_bg[0])

game_board = Frame(window)
game_board.pack()
count = 0
x_turn = True
won = False
draw = False
popped_up = False

xs_turn_indicator = Label(window, text = 'X',font=('Comic Sans MS', 25), height = 2, width = 6, bg= current_bg[1])
xs_turn_indicator.place(x = 10, y = 60)

os_turn_indicator = Label(window, text = 'O', font=('Comic Sans MS', 25), height = 2, width = 6, bg= current_bg[1])
os_turn_indicator.pack(fill='both', expand= True)

os_turn_indicator.place(x = window.winfo_reqwidth() - 60 , y = 60)
def indicate_turn():
    if x_turn:
        xs_turn_indicator.config(fg = fg_current)
        os_turn_indicator.config(fg = current_bg[0])
    else:
        os_turn_indicator.config(fg = fg_current)
        xs_turn_indicator.config(fg = current_bg[0])
indicate_turn()

#=================================================================
#current_bg = 
#current_fg =
    
#_____________________________________________________________________________________________________________________________
#=============================================================================================================================
#=============================================================================================================================
def popupbind(event):
    if popped_up:
        restart()
window.bind('<Return>', popupbind)
def popup(case):
    def blink():
        alt = True
        num_alt = 1
        blink_count = 0
        while popped_up and blink_count <= 12:
            if not won:
                result.config(bg = 'red') if alt else result.config(bg = None)
                alt = not alt
            else:
                instyle = '>'
                enstyle = '<'

                result['text'] = instyle*(num_alt%4) + ' ' + winner + ' ' + enstyle(num_alt%4)
                num_alt += 1
            blink_count += 1
            time.sleep(1)

    #time.sleep(2)
    global top, window, popped_up,draw
    def close():
        global popped_up
        popped_up = False
        top.quit()
    popped_up = True
    top = Toplevel(window, bg = current_bg[1])
    top.geometry("250x250")
    top.bind('<Return>', popupbind)
    if case == 'win':
        winner = 'X' if x_turn else 'O'
        result = Label(top, text= "|>>> " + winner +" Won <<<|", font=('Mistral 18 bold'))
        result.place(x=30,y=80)
    else:
        draw = True
        result = Label(top, text= "Draw", font=('Comic Sans MS',40))
        result.place(x=30,y=20)
    #blink()
    button_frame = Frame(top, bg = current_bg[1])
    button_frame.place(x=30,y=120)
    
    restart_button = Button(button_frame, text = 'Restart', fg = fg_current , bg = current_bg[1], command = restart)
    restart_button.grid(row = 0, column = 0)
    
    exit_button = Button(button_frame, text = 'Exit', fg = fg_current , bg = current_bg[1], command = close)
    exit_button.grid(row=0,column=1)
    
    info_label = Label(top, text = 'Press Enter to Restart...', fg = 'yellow',bg = current_bg[1])
    info_label.place(x=30, y = 180)
#===========================================================================================================================
#===========================================================================================================================
#__________________________________________________________________________________________________________________________
def on_click(event):
    global x_turn, count, won, draw
    w = event.widget
    if w['text'] == '' and count < 9 and not won and not draw:
        play_SFX('keypress')
        w['text'] = 'X' if x_turn else 'O'
        check_if_won()
        
        x_turn = not x_turn
        count += 1
        indicate_turn()
    if count == 9 and not won and not draw:
        draw = True
        play_SFX('draw')
        popup('draw')
#_________________________________________________________________________________________________________________________
c1 = Label(game_board, text = '')
c2 = Label(game_board, text = '')
c3 = Label(game_board, text = '')
c4 = Label(game_board, text = '')
c5 = Label(game_board, text = '')
c6 = Label(game_board, text = '')
c7 = Label(game_board, text = '')
c8 = Label(game_board, text = '')
c9 = Label(game_board, text = '')
#_________________________________________________________________________________________________________________________
cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
fonts = ['Chiller', 'MV Boli', 'Matura MT Script Capitals', 'Mistral']

for cell in cells:
    cell.config(font=('Mistral', 55), height = 2, width = 6, fg = fg_current, bg = current_bg[0] if cells.index(cell)%2==0 else current_bg[1])
    cell.bind('<Button>', on_click)   
#_________________________________________________________________________________________________________________________
cell_index = 0
for i in range(3):
    for j in range(3):
        cells[cell_index].grid(row=i, column=j)
        cell_index += 1
#=========================================================================================================================


def check_if_won():
    global won
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
      
    if '' != c1['text'] == c2['text'] == c3['text']:
        c1.config(fg= 'yellow')
        c2.config(fg= 'yellow')
        c3.config(fg= 'yellow')
        won = True
    elif '' != c4['text'] == c5['text'] == c6['text']:
        c4.config(fg= 'yellow')
        c5.config(fg= 'yellow')
        c6.config(fg= 'yellow')
        won = True
    elif '' != c7['text'] ==  c8['text'] == c9['text']:
        c7.config(fg= 'yellow')
        c8.config(fg= 'yellow')
        c9.config(fg= 'yellow')
        won = True

    elif '' != c1['text'] == c4['text'] == c7['text']:
        c1.config(fg= 'yellow')
        c4.config(fg= 'yellow')
        c7.config(fg= 'yellow')
        won = True
    elif '' != c2['text'] == c5['text'] == c8['text']:
        c2.config(fg= 'yellow')
        c5.config(fg= 'yellow')
        c8.config(fg= 'yellow')
        won = True
    elif '' != c3['text'] == c6['text'] == c9['text']:
        c3.config(fg= 'yellow')
        c6.config(fg= 'yellow')
        c9.config(fg= 'yellow')
        won = True

    elif '' != c1['text'] == c5['text'] == c9['text']:
        c1.config(fg= 'yellow')
        c5.config(fg= 'yellow')
        c9.config(fg= 'yellow')
        won = True
    elif '' != c3['text'] == c5['text'] == c7['text']:
        c3.config(fg= 'yellow')
        c5.config(fg= 'yellow')
        c7.config(fg= 'yellow')
        won = True
    if won:
        play_SFX('win')
        popup('win')
    
'''___________________________________________________________________________'''
def on_press(event):
    global cells, x_turn, count
    
    keypad = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
    c = cells[keypad.index(event.keysym)]
    event.widget = c 
    on_click(event)

for key in range(1,10):
    window.bind(str(key), on_press)
'''____________________________________________________________________________'''


window.mainloop()















