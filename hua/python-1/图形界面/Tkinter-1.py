from tkinter import *
import tkinter.messagebox as messagebox
#Label文本，Button按钮，command绑定按钮点击事件，app.master.title设置窗口标题，Entry文本框，
# messagebox.showinfo弹出面板。


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app=Application()
app.master.title('Hello,World')
app.mainloop()