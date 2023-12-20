import numpy as np
import tkinter as tk
import math

inf = math.inf

class graph_matrix():
    def __init__(self):
        self.matr=[]

    def simple_matrix_nn(self,n):


        all_entries = []
        def get_data():
            for r, row in enumerate(all_entries):
                for c, entry in enumerate(row):
                    text = entry.get()
                    demand[r, c] = text

            self.matr=demand

        def standart_example():
            if n == 1:
                print('The size is too small!')
            if n == 2:
                self.matr = [
                    [0, 1],
                    [1, 0],
                    ]
            if n == 3:
                self.matr = [
                    [0, 1, 1],
                    [1, 0, inf],
                    [1, inf, 0],
                    ]
            if n == 4:
                self.matr = [
                    [0, 1, 1, 1],
                    [1, 0, inf, 1],
                    [1, inf, 0, 1],
                    [1, 1, 1, 0],
                    ]
            if n == 5:
                self.matr=[
                        [0, 1, 1, 1, inf],
                        [1, 0, inf, 1, 1],
                        [1, inf, 0, 1, inf],
                        [1, 1, 1, 0, 1],
                        [inf, 1, inf, 1, 0]]
            if n > 5:
                print('Notice, standart examples are only avaible in sizes 2 to 5')
        def paradox_graph():

            if n == 3:
                self.matr=[         [0, 8, 5],
                                    [8, 0, 2],
                                    [5, 2, 0]]
            else:
                print('Notice, paradox example are only avaible in size 3')
        demand = np.zeros((n, n))

        window = tk.Tk()


        for r in range(n):
            entries_row = []
            for c in range(n):
                e = tk.Entry(window, width=5)  # 5 chars
                e.insert('end', 0)
                e.grid(row=r, column=c)
                entries_row.append(e)
            all_entries.append(entries_row)



        b = tk.Button(window, text='GET DATA', command=get_data)
        c = tk.Button(window, text='Standart Example', command=standart_example())
        d = tk.Button(window, text='Paradox Example', command=paradox_graph())

        b.grid(row=n + 1, column=0, columnspan=n)
        c.grid(row=n + 2, column=0, columnspan=n)
        d.grid(row=n + 3, column=0, columnspan=n)

        window.mainloop()


