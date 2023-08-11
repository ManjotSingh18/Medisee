import tkinter as tk
import time 
import home
class mainapp():
    def __init__(self, master):
        self.window=master
        self.window.geometry("720x720")
        self.frm0=tk.Frame()
        self.frm1=tk.Frame()
        self.frm0.pack()
        self.frm1.pack()
        self.searcher()
    def searcher(self):
        searchmessage=tk.Label(self.frm0, text="Enter Medicine", font=('Helvetica', 20, 'bold'))
        searchbox=tk.Text(self.frm0,height="2", font=("Helvetica", 20))
        searchbox.tag_configure("center", justify='center')
        searchbutt=tk.Button(self.frm0,text="Search", width=20, height=3, command=lambda: self.drawdata(self.frm1))
        searchmessage.pack_propagate(True)
        searchmessage.pack()
        searchbox.pack(fill="x", pady="10")
        searchbutt.pack()
        


    def drawdata(self, frames):
        data= home.apicall(self.frm0.winfo_children()[1].get("1.0","end-1c"))
        self.delete(frames)
        for case in data:
            test=tk.Label(frames, text=f"Age: {case.age}, Sex: {case.sex}, Drugs: {', '.join(case.drugs)}\n, Reactions: {', '.join(case.reactions)}\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
            test.pack()
        myscrollbar=tk.Scrollbar(frames,orient="vertical")
        myscrollbar.pack(side="right",fill="y")
        frames.pack()
    def delete(self, frames):
        for w in frames.winfo_children():
            w.destroy()
def appy():
    root= tk.Tk()
    app= mainapp(root)
    root.mainloop()
appy()