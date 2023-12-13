import numpy as np
import tkinter as tk



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


        b.grid(row=n + 1, column=0, columnspan=n)

        window.mainloop()


