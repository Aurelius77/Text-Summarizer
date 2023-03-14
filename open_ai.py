import openai
import tkinter as tk
import customtkinter as ct
import json


class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('600x600')
        self.title('Text Summarizer')
        ct.set_appearance_mode('system')
        ct.set_default_color_theme('green')


        #INPUT BOX
        self.entry = ct.StringVar()


        self.entry_space = ct.CTkEntry(master=self,
                          textvariable=self.entry,
                          width=200,
                          height=100,
                          border_width=2,
                          placeholder_text='Enter text...',
                          text_color='white'
                          ).pack(padx=40, pady=20)
        
        #SUBMIT BUTTON
        
        self.button = ct.CTkButton(
            master=self, text='GET SUMMARY', command=self.getSummary)


        self.button.pack(padx=20, pady=10)


        #SUMMARIZED TEXT

        self.label_var = ct.StringVar(value='')


        self.label = ct.CTkLabel(master=self,
                    textvariable=self.label_var,
                    width=120,
                    height=25,
                    fg_color=("white", "gray20"),
                    justify='center',
                    anchor=tk.CENTER,
                    corner_radius=8)
        self.label.pack(padx=20, pady=10)


  #API CALL UNCTION
    def getSummary(self):
     
        text = self.entry.get()
        openai.api_key = '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'
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Summarize this text with the most unique and helpful parts\n\n{text}',
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
        self.label_var.set('Text file with summary succesfully created')
    


if __name__ == '__main__':
    app = App()
    app.mainloop()
