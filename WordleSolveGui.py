import PySimpleGUI as sg
import WordleSolve as ws
from collections import OrderedDict
import re

    # Column layout      
col = [[sg.Text('I suggest you try NOTES or RESIN', text_color='white', font='Console 16', key='-OUTPUT-')]]   

gcl = [(None,None)] *25
# Define the window's contents
layout = [[sg.Text("Enter your guesses in the boxes below. Check the boxes based on received clues.", font='Console 16')], 
          [sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT00_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT00_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT01_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT01_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT02_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT02_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT03_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT03_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT04_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT04_GCHK-')],
          [sg.Input(size=(2,2), font=('Console 26'), pad=(3,0),      justification='center', enable_events=True, key='-INPUT00-'), 
           sg.Input(size=(2,2), font=('Console 26'), pad=((9,0),0),  justification='center', enable_events=True, key='-INPUT01-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT02-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT03-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT04-'), sg.Column(col)],
          [sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT10_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT10_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT11_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT11_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT12_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT12_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT13_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT13_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT14_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT14_GCHK-')],
          [sg.Input(size=(2,2), font=('Console 26'), pad=(3,0),      justification='center', enable_events=True, key='-INPUT10-'), 
           sg.Input(size=(2,2), font=('Console 26'), pad=((9,0),0),  justification='center', enable_events=True, key='-INPUT11-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT12-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT13-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT14-')],
            [sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT20_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT20_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT21_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT21_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT22_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT22_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT23_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT23_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT24_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT24_GCHK-')],
          [sg.Input(size=(2,2), font=('Console 26'), pad=(3,0),      justification='center', enable_events=True, key='-INPUT20-'), 
           sg.Input(size=(2,2), font=('Console 26'), pad=((9,0),0),  justification='center', enable_events=True, key='-INPUT21-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT22-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT23-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT24-')],
            [sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT30_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT30_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT31_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT31_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT32_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT32_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT33_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT33_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT34_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT34_GCHK-')],
          [sg.Input(size=(2,2), font=('Console 26'), pad=(3,0),      justification='center', enable_events=True, key='-INPUT30-'), 
           sg.Input(size=(2,2), font=('Console 26'), pad=((9,0),0),  justification='center', enable_events=True, key='-INPUT31-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT32-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT33-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT34-')],
            [sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT40_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT40_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT41_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT41_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT42_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT42_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT43_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0),  enable_events=True, key='-INPUT43_GCHK-'),
           sg.Checkbox(text='', checkbox_color='yellow', text_color='black', enable_events=True, pad=(0,0), key='-INPUT44_YCHK-'),
           sg.Checkbox(text='', checkbox_color='green', pad=(0,0), enable_events=True, key='-INPUT44_GCHK-')],
          [sg.Input(size=(2,2), font=('Console 26'), pad=(3,0),      justification='center', enable_events=True, key='-INPUT40-'), 
           sg.Input(size=(2,2), font=('Console 26'), pad=((9,0),0),  justification='center', enable_events=True, key='-INPUT41-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT42-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT43-'),
           sg.Input(size=(2,2), font=('Console 26'), pad=((12,0),0), justification='center', enable_events=True, key='-INPUT44-')],
          [sg.Button('Reset'), sg.Button('Quit')]]

# Create the window
window = sg.Window('WordleSolve by Mark', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Reset':
        for key in values:
            window.Element(key).Update('')
            if (re.match('.*CHK-',key) != None):
                window[key].Update(False)
            if (re.match('-INPUT\d\d-',key) != None):
                window.Element(key).Update(background_color='white')
    #read the word list
    if (len(ws.wordle_list) == 0):
        ws.wordle_list = ws.read_words()

    line_set = [2]*5
    for key in values:
        check_key = re.match('-INPUT\d\d-',key)
        if (check_key != None):
            input_key = check_key.group()
            gcl_index = int(input_key[6])*5 + int(input_key[7])
            #Prevent user from adding more than one letter to entry box
            if len(values[input_key]) > 1:
                window.Element(input_key).Update(values[input_key][:-1].lower()) 
                values[input_key] = values[input_key][:-1]

#Assign clue letters to list       
    for key in values:
        check_key = re.match('-INPUT\d0-',key)
        if (check_key != None):
            input_key = check_key.group()
            gcl_index = int(input_key[6])*5 + int(input_key[7])
            if (len(values[input_key]) != 0 and
                len(values[input_key[0:7]+str(int(input_key[7])+1)+'-']) != 0 and
                len(values[input_key[0:7]+str(int(input_key[7])+2)+'-']) != 0 and
                len(values[input_key[0:7]+str(int(input_key[7])+3)+'-']) != 0 and
                len(values[input_key[0:7]+str(int(input_key[7])+4)+'-']) != 0):

                line_set[int(input_key[6])] = 1
                gcl[gcl_index]   = (values[input_key].lower(), 'white')
                gcl[gcl_index+1] = (values[input_key[0:7]+str(int(input_key[7])+1)+'-'].lower(), 'white')
                gcl[gcl_index+2] = (values[input_key[0:7]+str(int(input_key[7])+2)+'-'].lower(), 'white')
                gcl[gcl_index+3] = (values[input_key[0:7]+str(int(input_key[7])+3)+'-'].lower(), 'white')
                gcl[gcl_index+4] = (values[input_key[0:7]+str(int(input_key[7])+4)+'-'].lower(), 'white')

            elif (len(values[input_key]) == 1 or
                  len(values[input_key[0:7]+str(int(input_key[7])+1)+'-']) == 1 or
                  len(values[input_key[0:7]+str(int(input_key[7])+2)+'-']) == 1 or
                  len(values[input_key[0:7]+str(int(input_key[7])+3)+'-']) == 1 or
                  len(values[input_key[0:7]+str(int(input_key[7])+4)+'-']) == 1):
                line_set[int(input_key[6])] = 0
            else:
                line_set[int(input_key[6])] = 2

#Apply checkmark boxes to clue colors
    for key in values:
        check_key = re.match('-INPUT\d\d-',key)
        if (check_key != None):
            input_key = check_key.group()
            gcl_index = int(input_key[6])*5 + int(input_key[7])

            if (values[input_key[0:8]+'_GCHK-'] == True):
                window.Element(input_key).Update(background_color='green')
                window.Element(input_key[0:8]+'_YCHK-').Update(disabled=True)     
                gcl[gcl_index]= (values[input_key].lower(),'green')
            if (values[input_key[0:8]+'_YCHK-'] == True):
                window.Element(input_key).Update(background_color='yellow')
                window.Element(input_key[0:8]+'_GCHK-').Update(disabled=True)  
                gcl[gcl_index]= (values[input_key].lower(),'yellow')
            if ((values[input_key[0:8]+'_YCHK-'] == False) and (values[input_key[0:8]+'_GCHK-'] == False)):
                window.Element(input_key).Update(background_color='white')
                window.Element(input_key[0:8]+'_GCHK-').Update(disabled=False)  
                window.Element(input_key[0:8]+'_YCHK-').Update(disabled=False)  
                gcl[gcl_index]= (values[input_key].lower(),'white')

    print(gcl)
    ws.clues = gcl
    print(ws.clues)
    choice_words = ws.retrieve_viable_words()
    if (len(choice_words) < 50):
        print(choice_words)

    if (line_set[0] != 0 and line_set[1] != 0 and
        line_set[2] != 0 and line_set[3] != 0 and
        line_set[4] == 2):

        if len(choice_words) > 4:
            window['-OUTPUT-'].update('Try guessing ' + list(choice_words)[0] + ', ' + list(choice_words)[1] + ", " 
                                     + list(choice_words)[2] + ', ' + list(choice_words)[3] + ', or '+ list(choice_words)[4]+ "!")  
        elif len(choice_words) > 3:
            window['-OUTPUT-'].update('Try guessing ' + list(choice_words)[0] + ', ' + list(choice_words)[1] + ", " 
                                     + list(choice_words)[2] + ', or' + list(choice_words)[3] +"!")   
        elif len(choice_words) > 2:
            window['-OUTPUT-'].update('Try guessing ' + list(choice_words)[0] + ', ' + list(choice_words)[1] + ", or " + list(choice_words)[2] +"!")
        elif len(choice_words) > 1:
            window['-OUTPUT-'].update('Last guess, try ' + list(choice_words)[0] + ' or ' +list(choice_words)[1])
        elif len(choice_words) > 0:
            window['-OUTPUT-'].update('Last guess, try ' + list(choice_words)[0])
        else:
            window['-OUTPUT-'].update('Wordle Solver failed! :(')

    #Output different message if we are on the last clue
    elif (line_set[0] == 1 and line_set[1] == 1 and
          line_set[2] == 1 and line_set[3] == 1 and
          line_set[4] == 1):
        if len(choice_words) > 2:
            window['-OUTPUT-'].update('Last guess, try ' + list(choice_words)[0] + ', ' +list(choice_words)[1] + ", or " + list(choice_words)[2] )
        elif len(choice_words) > 1:
            window['-OUTPUT-'].update('Last guess, try ' + list(choice_words)[0] + ' or ' +list(choice_words)[1])
        elif len(choice_words) > 0:
            window['-OUTPUT-'].update('The answer is ' + list(choice_words)[0]  +'!')
        else:
            window['-OUTPUT-'].update('Wordle Solver failed! :(')
        
# Finish up by removing from the screen
window.close()