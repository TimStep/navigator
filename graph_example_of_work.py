from graph_construct import graph_matrix
from graph_visualisation import Visualisate
from tkinter import *
from matplotlib.figure import Figure


app = Tk()

canvas_widget = Canvas(app, width=500, height=500)
canvas_widget.pack()



label_widget1 = Label(app, text="Enter start")
canvas_widget.create_window(150, 160, window=label_widget1)


label_widget2 = Label(app, text="Enter finish")
canvas_widget.create_window(150, 200, window=label_widget2)

label_widget3 = Label(app, text="Enter N")
canvas_widget.create_window(150, 240, window=label_widget3)

entry_widget1 = Entry(app)
canvas_widget.create_window(300, 160, window=entry_widget1)

entry_widget2 = Entry(app)
canvas_widget.create_window(300, 200, window=entry_widget2)

entry_widget3 = Entry(app)
canvas_widget.create_window(300, 240, window=entry_widget3)




b = graph_matrix()


def entry_data():


    start = int(float(entry_widget1.get()))
    finish = int(float(entry_widget2.get()))
    return start,finish
def get_n():
    n=int(float(entry_widget3.get()))
    return  n
def get_matr():
    fig = Figure(figsize=(5, 5),
                 dpi=100)
    n=get_n()

    b.simple_matrix_nn(n)
def plot_graph():


    a = Visualisate(b.matr)
    a.vis_simple_graph()
def plot_shortest_way():


    start,finish = entry_data()


    a = Visualisate(b.matr)
    a.vis_shortest_way(start,finish)









button_matr= Button(master=app,
                     command=get_matr,
                     height=2,
                     width=25,
                     text="Get matrix of graph")



plot_button = Button(master=app,
                     command=plot_graph,
                     height=2,
                     width=15,
                     text="Plot graph")

plot_button_way = Button(master=app,
                     command=plot_shortest_way,
                     height=2,
                     width=20,
                     text="Plot shortest way")


# place the button
# in main window
plot_button.pack()
plot_button_way.pack()
button_matr.pack()
# run the gui
app.mainloop()
