import openai
import customtkinter as ct
import json


def getSummary():
    text = entry.get()
    openai.api_key = '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'
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Summarize this text with the most unique and helpful points\n\n{text}',
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # text_var.set(str(response))
    json_data = str(response)
    data_dict = json.loads(json_data)
    sum_text = (data_dict['choices'][0]['text'])
    with open("summary.txt", "w") as file:
        file.write(sum_text)
    label_var.set('Text file with summary succesfully created')


root = ct.CTk()
root.geometry('400x400')
root.title('Text Summarizer')
ct.set_appearance_mode('system')
# ct.set_default_color_theme('dark-blue')


entry = ct.StringVar()
emtry_space = ct.CTkEntry(master=root,
                          textvariable=entry,
                          width=200,
                          height=20,
                          border_width=2,
                          corner_radius=10,
                          placeholder_text='Enter text...',
                          text_color='white'
                          ).pack(padx=40, pady=20)


button = ct.CTkButton(master=root, text='GET SUMMARY', command=getSummary)
button.pack(padx=20, pady=10)


label_var = ct.StringVar(value='')

label = ct.CTkLabel(master=root,
                    textvariable=label_var,
                    width=120,
                    height=25,
                    fg_color=("white", "gray20"),
                    corner_radius=8)
label.pack(padx=20, pady=10)


root.mainloop()
