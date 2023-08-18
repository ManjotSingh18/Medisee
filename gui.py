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
        self.miniumum=0
        self.maximum = 200
        self.sexes={0, 1,2}
        self.creator = tk.Toplevel(self.window)
        self.creator.protocol("WM_DELETE_WINDOW", lambda: None)
        self.creator.grab_set()
        self.creator.wm_attributes("-topmost", True)
        self.creator.geometry("400x400")
        agree=tk.Button(self.creator,text="Agree", width=20, height=3,justify="center", command=self.agreed,bg="lightgrey")
        disagree=tk.Button(self.creator,text="Disagree", width=20, height=3,justify="center", command=self.disagreed,bg="lightgrey")
        disclaimer=tk.Label(self.creator, text="Medisee is provided for educational and informational purposes only and does not constitute providing medical advice or professional services. The information provided should not be used for diagnosing or treating a health problem or disease, and those seeking personal medical advice should consult with a licensed physician", height=10, wraplength=400, font=('Helvetica', 10, 'bold'))
        disclaimer.pack()
        agree.pack()
        disagree.pack()
        self.limits=100
        self.searcher()
    def searcher(self):
        self.icon=ImageTk.PhotoImage(Image.open("./img/logo.PNG"))
        searchmessage=tk.Label(self.frm0, image=self.icon, height=150)
        searchbox=tk.Text(self.frm0,height="1", font=("Helvetica", 20), bg="lightgrey")
        searchbox.tag_configure("center", justify='center')
        searchbutt=tk.Button(self.frm0,text="Search", width=20, height=3,justify="center", command=lambda: self.drawdata(self.frm1),bg="lightgrey")
        nextbutt=tk.Button(self.frm0,text="Next", justify="center",width=20, height=3, command=lambda: self.next(self.frm1),bg="lightgrey")
        prevbutt=tk.Button(self.frm0,text="Previous", justify="center",width=20, height=3,command=lambda: self.prev(self.frm1), bg="lightgrey")
        filterbutt=tk.Button(self.frm0,text="Filter", command=self.params, justify="center",width=10, height=3, bg="lightgrey")
        self.pns=pagesearch=tk.Entry(self.frm0, width=25, bg="lightgrey")
        self.pns.insert(0, f"Search page number")
        pagesearch.bind("<FocusIn>", self.temp_text)
        pagesearch.bind("<FocusOut>", self.temp_text2)
        pagesearch.bind("<Return>", self.pagesearcher)
        #searchmessage.pack_propagate(True)
        searchmessage.pack(fill="both", expand="True")
        searchbox.pack(fill="x")
        searchbutt.pack(side="left", pady="20", padx=(0, 50))
        nextbutt.pack(side="left", pady="20")
        prevbutt.pack(side="left", pady="20")
        filterbutt.pack(side="left")
        self.pns.pack(side="left", pady="20", padx="30")
    def pagesearcher(self, e):
        if len(self.move) == 0 or not self.pns.get().isdigit() or int(self.pns.get()) > len(self.data)//5 or int(self.pns.get()) <= 0:
            pass
        else:
            self.delete(self.frm1)
            self.offset = int(self.pns.get())-1
            show=self.move[self.offset]
            for n in range(0, len(show)):
                    test=tk.Label(self.frm1,highlightcolor="white",text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700, bg="#358797")
                    test.pack(pady=10)
            page=tk.Label(self.frm1, text=f"Page {self.offset+1}", font=('Helvetica', 15, 'bold'))
            page.pack()
    def temp_text(self, e):
        self.pns.delete(0, "end")
    def temp_text2(self, e):
        self.pns.insert(0, f"Search page number")
    def params(self):
        self.filterpop=tk.Toplevel()
        self.filterpop.title("Filters")
        self.filterpop.geometry("400x300")
        ageminmessage=tk.Label(self.filterpop, text="Minimum Age")
        self.minentry=tk.Entry(self.filterpop,bg="lightgrey")
        self.maxentry=tk.Entry(self.filterpop, bg="lightgrey")
        agemaxmessage=tk.Label(self.filterpop, text='Maximum Age')
        limitmessage=tk.Label(self.filterpop, text="Amount of entries to search (max 1000)")
        self.limitamount=tk.Entry(self.filterpop, bg="lightgrey")
        sexmessage=tk.Label(self.filterpop, text="Sexes to display")
        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.s1 = tk.Checkbutton(self.filterpop, text='Undefined', onvalue=1, offvalue=0, variable=self.CheckVar1)
        self.s2 = tk.Checkbutton(self.filterpop, text='Male',onvalue=1, offvalue=0, variable=self.CheckVar2)
        self.s3 = tk.Checkbutton(self.filterpop, text='Female', onvalue=1, offvalue=0, variable=self.CheckVar3)
        self.s1.select()
        self.s2.select()
        self.s3.select()
        applybutt=tk.Button(self.filterpop,text="Apply", command=self.filapply, justify="center",width=10, height=3, bg="lightgrey")
        reset=tk.Button(self.filterpop,text="Reset", command=self.default, justify="center",width=10, height=3, bg="lightgrey")
        limitmessage.pack()
        self.limitamount.pack()
        ageminmessage.pack()
        self.minentry.pack()
        agemaxmessage.pack()
        self.maxentry.pack()
        sexmessage.pack()
        self.s1.pack()
        self.s2.pack()
        self.s3.pack()
        applybutt.pack()
        reset.pack(side="left")

    def drawdata(self, frames):
        self.offset=0
        self.data= home.apicall(self.frm0.winfo_children()[1].get("1.0","end-1c"), self.limits)
        self.move.clear()
        counter=0
        for i in range(0, len(self.data)):
            if self.maximum>= int(self.data[i].age) >= self.miniumum and int(self.data[i].sex) in self.sexes:
                self.move[counter//3].append(self.data[i])
                counter+=1
        self.delete(frames)
        x=0
        for case in self.data:
            if self.maximum>= int(case.age) >= self.miniumum and int(case.sex) in self.sexes:
                if x == 3:
                    break
                else:
                    test=tk.Label(frames, highlightcolor="white", text=f"Age: {case.age}, Sex: {case.sex}, Drugs: {', '.join(case.drugs)}\n\n Reactions: {', '.join(case.reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700, bg="#358797")
                    test.pack(pady=10)
                x+=1
        page=tk.Label(frames, text=f"Page 1", font=('Helvetica', 15, 'bold'))
        page.pack()
    def next(self, frames):
        if self.offset < len(self.data)//3:
            self.delete(frames)
            self.offset+=1
            show=self.move[self.offset]
            for n in range(0, len(show)):
                    test=tk.Label(frames, highlightcolor="white", text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700, bg="#358797")
                    test.pack(pady=10)
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
                    test=tk.Label(frames, highlightcolor="white", text=f"Age: {show[n].age}, Sex: {show[n].sex}, Drugs: {', '.join(show[n].drugs)}\n\n Reactions: {', '.join(show[n].reactions)}\n\n", font=('Helvetica', 10, 'bold'), justify='center', wraplength=700, bg="#358797")
                    test.pack(pady=10)
            page=tk.Label(frames, text=f"Page {self.offset+1}", font=('Helvetica', 15, 'bold'))
            page.pack()
        else:
            pass
    def delete(self, frames):
        for w in frames.winfo_children():
            w.destroy()
    def agreed(self):
        self.creator.destroy()
    def disagreed(self):
        self.creator.destroy()
        self.window.destroy()
        quit()
    def filapply(self):
        if self.limitamount.get().isdigit() and int(self.limitamount.get()) <=1000 and self.limitamount.get() != "":
            self.limits=int(self.limitamount.get())
        else:
            pass
        if self.minentry.get().isdigit():
            self.miniumum=int(self.minentry.get())
        if self.maxentry.get().isdigit():
            self.maximum=int(self.maxentry.get())
        try:
            if self.CheckVar1.get():
                self.sexes.add(0)
            else:
                self.sexes.remove(0)
            if self.CheckVar2.get():
                self.sexes.add(1)
            else:
                self.sexes.remove(1)
            if self.CheckVar3.get():
                self.sexes.add(2)
            else:
                self.sexes.remove(2)
        except:
            pass
        self.filterpop.destroy()
    def default(self):
        self.miniumum=0
        self.maximum=200
        self.limits=100
        self.sexes={0, 1, 2}
        self.filterpop.destroy()
    def quit(self):
        self.window.destroy()
        quit()

def appy():
    root= tk.Tk()
    app= mainapp(root)
    root.protocol("WM_DELETE_WINDOW", app.quit)
    root.mainloop()
appy()