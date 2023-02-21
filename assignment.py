import PySimpleGUI as sg

sg.theme("GreenTan")

# Frame 
left_frame = [
    [sg.Text("Super Cool Spell Checking NLP Assignment")],
    [sg.HSep()],
    [sg.Multiline(s=(80, 24), key = 'multiline')],
    [sg.Button("Check Spelling", key="check_spelling")],
    [sg.Button("Check Word", key = "check_word")]
]

right_frame = [
    [sg.Text("Corrections", key='label_correction')],
    [sg.Listbox(['Correction 1', 'Correction 2'], no_scrollbar=True,  s=(20, 7), key='listbox')],
    [sg.Button("Correct Word", key='correct_word')],

]

layout = [[sg.Col(left_frame, p=0), sg.VSep(), sg.Col(right_frame, p=0)]]
window = sg.Window("NLP Assignment", layout)

while True:
    event, values = window.read()

    if event == 'check_word':
        selected_text = window['multiline'].Widget.selection_get()
        start = window['multiline'].Widget.index('sel.first')
        end = window['multiline'].Widget.index('sel.last')
        print(f'Selected Text: {selected_text}, Start: {start}, End: {end}')
        window['label_correction'].update(f"Candidate: {selected_text}")
        lb_new_options = []
        for i in range(3):
            s = f"{selected_text[:1]}Correction {i+1}"
            lb_new_options.append(s)
        window['listbox'].update(lb_new_options)

    elif event == 'correct_word':
        input_text = values['multiline']
        start = int(str(start[2:]))
        end = int(str(end[2:]))
        print(f"Start: {start}, End: {end}")
        print(input_text[start:end])
        output_text = input_text[:start] + str(values["listbox"][0]) + input_text[end:]
        print(output_text)
        window['multiline'].update(output_text)

    elif event == 'check_spelling':
        import nltk
        input_text = values['multiline']
        window['multiline'].update('')
        tokens = nltk.tokenize.word_tokenize(input_text)
        sg.cprint_set_output_destination(window, 'multiline')
        for i, elem in enumerate(tokens):
            if i == 2:
                sg.cprint(elem, text_color='red', end=' ')
            elif i == 4: 
                sg.cprint(elem, text_color='red', end=' ')
            else:
                sg.cprint(elem, end=' ')
        




window.close()