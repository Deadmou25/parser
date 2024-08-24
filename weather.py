from tkinter import Frame, Tk,Label,Button
from parser2 import Weather


class UI:
    def __init__(self):
        self.window=Tk()
        self.window.title("weather")
        self.create_frames()
               
        self.weather = Weather()
        self.weather.add_link_in_dict()

        self.links = self.weather.main_block_tag
        self.total_links = len(self.links)

        self.column = 5

        self.create_all_btn(self.links)
        self.create_home_btn(self.links)

        self.start()

    def create_frames(self):
        self.top_frame = Frame(self.window)
        self.top_frame.grid(row=0, column=0)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.grid(row=1, column=0)


    def recreate_top_frame(self):
        self.top_frame.destroy()
        self.top_frame = Frame(self.window)
        self.top_frame.grid(row=0, column=0)

    def recreate_bottom_frame(self):
        self.bottom_frame.destroy()
        self.bottom_frame = Frame(self.window)
        self.bottom_frame.grid(row=1, column=0)


    def button_handler(self, link): 
        self.recreate_top_frame()

        two = self.weather.parse_next(link)

        if isinstance(two, dict):
            self.create_all_btn(two)
            self.create_home_btn(self.links)
        else:

            text = str(self.weather.parse_next(link))
            label = Label(self.top_frame, text=text)
            label.grid(row=0,column=0)


    def create_all_btn(self, links: dict):
        dict_links = links
        for i, (name, link) in enumerate(dict_links.items()):
            row = i // self.column
            col = i % self.column
            button = Button(self.top_frame, text=name, command=lambda c=link: self.button_handler(c))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


    def create_home_btn(self, link):
        hom_btn = Button(self.bottom_frame, text="Home", command=lambda a=link:self.create_all_btn(a))
        hom_btn.grid(row=0, column=0)

    def start(self):
        self.window.mainloop()

UI()
