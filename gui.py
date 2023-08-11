import tkinter as tk

ws=tk.Tk()
ws.geometry("720x720")
searchmessage=tk.Label(text="Enter Medicine", font=('Helvetica', 20, 'bold'))
searchbox=tk.Text(height="2", font=("Helvetica", 20))
searchbox.tag_configure("center", justify='center')
searchbutt=tk.Button(text="Search", width=20, height=3)
searchmessage.pack_propagate(True)
searchmessage.pack()
searchbox.pack(fill="x", pady="10")
searchbutt.pack()
ws.mainloop()