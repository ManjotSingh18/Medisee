import tkinter as tk
import time 
import home
from PIL import ImageTk, Image
from collections import defaultdict
class mainapp():
    def __init__(self, master):
        self.window=master
        self.window.geometry("800x800")
        self.data=[]
        self.offset=0
        self.move=defaultdict(list)
        self.frm0=tk.Frame()
        self.frm1=tk.Frame()
        self.frm0.pack()
        self.frm1.pack()
        self.pns=None
        self.icon=None
        self.searcher()
    def searcher(self):
        self.icon=ImageTk.PhotoImage(Image.open("./img/logo.PNG"))
        searchmessage=tk.Label(self.frm0, image=self.icon, height=150)
        searchbox=tk.Text(self.frm0,height="1", font=("Helvetica", 20))
        searchbox.tag_configure("center", justify='center')
        searchbutt=tk.Button(self.frm0,text="Search", width=20, height=3,justify="center", command=lambda: self.drawdata(self.frm1))
        nextbutt=tk.Button(self.frm0,text="Next", justify="center",width=20, height=3, command=lambda: self.next(self.frm1))
        prevbutt=tk.Button(self.frm0,text="Previous", justify="center",width=20, height=3,command=lambda: self.prev(self.frm1))
        self.pns=pagesearch=tk.Entry(self.frm0, width=25)
        self.pns.insert(0, f"Search page number")
        pagesearch.bind("<FocusIn>", self.temp_text)
        pagesearch.bind("<FocusOut>", self.temp_text2)
        pagesearch.bind("<Return>", self.pagesearcher)
        #searchmessage.pack_propagate(True)
        searchmessage.pack(fill="both", expand="True")
        searchbox.pack(fill="x")
        searchbutt.pack(side="left", pady="20", padx=(0, 100))
        nextbutt.pack(side="left", pady="20")
        prevbutt.pack(side="left", pady="20")
        self.pns.pack(side="left", pady="20", padx="30")
    def pagesearcher(self, e):
        if len(self.move) == 0 or not self.pns.get().isdigit() or int(self.pns.get()) > len(self.data)//5 or int(self.pns.get()) <= 0:
            pass
        else:
            self.delete(self.frm1)
            self.offset = int(self.pns.get())-1
            show=self.move[self.offset]
            for n in range(0, len(show)):
                test=tk.Label(self.frm1, text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            page=tk.Label(self.frm1, text=f"Page {self.offset+1}", font=('Helvetica', 15, 'bold'))
            page.pack()
    def temp_text(self, e):
        self.pns.delete(0, "end")
    def temp_text2(self, e):
        self.pns.insert(0, f"Search page number")
    def drawdata(self, frames):
        self.offset=0
        self.data= home.apicall(self.frm0.winfo_children()[1].get("1.0","end-1c"))
        self.move.clear()
        for i in range(0, len(self.data)):
            self.move[i//5].append(self.data[i])
        self.delete(frames)
        x=0
        for case in self.data:
            if x == 5:
                break
            else:
                test=tk.Label(frames, text=f"Age: {case.age}, Sex: {case.sex}, Drugs: {', '.join(case.drugs)}\n Reactions: {', '.join(case.reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            x+=1
        page=tk.Label(frames, text=f"Page 1", font=('Helvetica', 15, 'bold'))
        page.pack()
    def next(self, frames):
        if self.offset < len(self.data)//5:
            self.delete(frames)
            self.offset+=1
            show=self.move[self.offset]
            for n in range(0, len(show)):
                test=tk.Label(frames, text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            page=tk.Label(frames, text=f"Page {self.offset+1}", font=('Helvetica', 15, 'bold'))
            page.pack()
        else:
            pass
        

    def prev(self, frames):
        if self.offset > 0:
            self.delete(frames)
            self.offset-=1
            show=self.move[self.offset]
            for n in range(0, len(show)):
                test=tk.Label(frames, text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700)
                test.pack()
            page=tk.Label(frames, text=f"Page {self.offset+1}", font=('Helvetica', 15, 'bold'))
            page.pack()
        else:
            pass
    def delete(self, frames):
        for w in frames.winfo_children():
            w.destroy()

    def quit(self):
        self.window.destroy()
        quit()

def appy():
    root= tk.Tk()
    app= mainapp(root)
    root.protocol("WM_DELETE_WINDOW", app.quit)
    root.mainloop()
appy()