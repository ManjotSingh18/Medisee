import tkinter as tk
import time 
import home
class mainapp():
    def __init__(self, master):
        self.window=master
        self.window.geometry("1000x1000")
        self.data=[]
        self.offset=0
        self.frm0=tk.Frame()
        self.frm1=tk.Frame()
        self.window.geometry()
        self.frm0.pack()
        self.frm1.pack(expand=True)
        self.searcher()
    def searcher(self):
        searchmessage=tk.Label(self.frm0, text="Enter Medicine", font=('Helvetica', 20, 'bold'))
        searchbox=tk.Text(self.frm0,height="1", font=("Helvetica", 20))
        searchbox.tag_configure("center", justify='center')
        searchbutt=tk.Button(self.frm0,text="Search", width=20, height=3,justify="center", command=lambda: self.drawdata(self.frm1))
        nextbutt=tk.Button(self.frm0,text="Next", justify="center",width=20, height=3, command=lambda: self.next(self.frm1))
        prevbutt=tk.Button(self.frm0,text="Previous", justify="center",width=20, height=3,command=lambda: self.prev(self.frm1))
        searchmessage.pack_propagate(True)
        searchmessage.pack()
        searchbox.pack(fill="x", pady="3")
        searchbutt.pack(side="left")
        nextbutt.pack(side="left")
        prevbutt.pack(side="left")
        
    def drawdata(self, frames):
        self.offset=0
        self.data= home.apicall(self.frm0.winfo_children()[1].get("1.0","end-1c"))
        self.delete(frames)
        x=0
        for case in self.data:
            if x == 5:
                break
            else:
                test=tk.Label(frames, text=f"Age: {case.age}, Sex: {case.sex}, Drugs: {', '.join(case.drugs)}\n, Reactions: {', '.join(case.reactions)}\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            x+=1
    def next(self, frames):
        if len(self.data) <=5:
            pass
        else:
            if 5+self.offset < len(self.data):
                




    def prev(self, frames):
        if len(self.data) <=5:
            pass
        else:            
            self.offset-=5
            self.delete(frames)
            for n in range(0+self.offset, 5+self.offset):
                if n <= 0:
                    self.offset+=5
                    break
                test=tk.Label(frames, text=f"Age: {self.data[n].age}, Sex: {self.data[n].sex}, Drugs: {', '.join(self.data[n].drugs)}\n, Reactions: {', '.join(self.data[n].reactions)}\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            print(self.offset)
    def delete(self, frames):
        for w in frames.winfo_children():
            w.destroy()

def appy():
    root= tk.Tk()
    app= mainapp(root)
    root.mainloop()
appy()