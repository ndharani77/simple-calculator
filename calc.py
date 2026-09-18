import tkinter as tk
import math

BG_COLOR="#121212"
BG=BG_COLOR
DISPLAY="#303134"
BUTTON="#3C4043"
OPERATOR="#5F6368"
BLUE="#1A73E8"
WHITE="#FFFFFF"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("500x650")
        self.window.configure(bg=BG)
        self.expression=""
        self.history=[]
        
        self.display=tk.Entry(self.window,font=("Arial",30,"bold"),bg=DISPLAY,fg=WHITE,justify="right",border=0)
        self.display.pack(fill="x",padx=15,pady=20,ipady=15)
        
        history_header=tk.Frame(self.window,bg=BG)
        history_header.pack(fill="x",padx=15)

        self.history_label=tk.Label(history_header,text="History",font=("Arial",14,"bold"),bg=BG,fg=WHITE)
        self.history_label.pack(side="left")

        tk.Button(history_header,text="Clear history",font=("Arial",10,"bold"),bg=OPERATOR,fg=WHITE,border=0,command=self.clear_history).pack(side="right")
        
        self.history_box=tk.Listbox(self.window,height=4,bg=DISPLAY,fg=WHITE,font=("Arial",11),border=0)
        self.history_box.pack(fill="x",padx=15,pady=5)
        
        frame=tk.Frame(self.window,bg=BG)
        frame.pack(expand=True,fill="both",padx=10,pady=10)
        
        buttons=[
            ["sin","cos","tan","log","√"],
            ["x²","%","+/-","⌫","C"],
            ["7","8","9","÷","("],
            ["4","5","6","×",")"],
            ["1","2","3","−","="],
            ["0",".","+","",""]
        ]
        
        for r,row in enumerate(buttons):
            for c,text in enumerate(row):
                if text=="":
                    continue
                if text=="=":
                    command=self.calculate
                    color=BLUE
                elif text=="C":
                    command=self.clear
                    color=OPERATOR
                elif text=="⌫":
                    command=self.backspace
                    color=OPERATOR
                elif text in ["+","−","×","÷"]:
                    command=lambda x=text:self.add_operator(x)
                    color=OPERATOR
                elif text in ["sin","cos","tan","log","√","x²","%","+/-"]:
                    command=lambda x=text:self.scientific(x)
                    color=OPERATOR
                else:
                    command=lambda x=text:self.add(x)
                    color=BUTTON
                tk.Button(frame,text=text,font=("Arial",16,"bold"),bg=color,fg=WHITE,border=0,command=command).grid(row=r,column=c,sticky="nsew",padx=3,pady=3)
        
        for i in range(6):
            frame.rowconfigure(i,weight=1)
        for i in range(5):
            frame.columnconfigure(i,weight=1)
        
        self.window.bind("<Return>",lambda e:self.calculate())
        self.window.bind("<BackSpace>",lambda e:self.backspace())
        self.window.bind("<Escape>",lambda e:self.clear())
        
        for key in "0123456789.":
            self.window.bind(key,lambda e,x=key:self.add(x))
        
        self.window.bind("+",lambda e:self.add_operator("+"))
        self.window.bind("-",lambda e:self.add_operator("−"))
        self.window.bind("*",lambda e:self.add_operator("×"))
        self.window.bind("/",lambda e:self.add_operator("÷"))

    def add(self,value):
        self.expression+=value
        self.display.delete(0,tk.END)
        self.display.insert(0,self.expression)

    def add_operator(self,operator):
        if self.expression and self.expression[-1] not in "+−×÷":
            self.expression+=operator
            self.display.delete(0,tk.END)
            self.display.insert(0,self.expression)

    def clear(self):
        self.expression=""
        self.display.delete(0,tk.END)

    def clear_history(self):
        self.history.clear()
        self.history_box.delete(0,tk.END)

    def backspace(self):
        self.expression=self.expression[:-1]
        self.display.delete(0,tk.END)
        self.display.insert(0,self.expression)

    def scientific(self,function):
        try:
            value=float(self.expression)
            if function=="sin":
                result=math.sin(math.radians(value))
            elif function=="cos":
                result=math.cos(math.radians(value))
            elif function=="tan":
                result=math.tan(math.radians(value))
            elif function=="log":
                result=math.log10(value)
            elif function=="√":
                result=math.sqrt(value)
            elif function=="x²":
                result=value**2
            elif function=="%":
                result=value/100
            elif function=="+/-":
                result=-value
            self.expression=str(round(result,10))
            self.display.delete(0,tk.END)
            self.display.insert(0,self.expression)
        except:
            self.display.delete(0,tk.END)
            self.display.insert(0,"Error")
            self.expression=""

    def calculate(self):
        try:
            expression=self.expression.replace("÷","/").replace("×","*").replace("−","-")
            result=eval(expression)
            result=round(result,10)
            item=self.expression+" = "+str(result)
            self.history.append(item)
            self.history_box.insert(tk.END,item)
            self.expression=str(result)
            self.display.delete(0,tk.END)
            self.display.insert(0,self.expression)
        except:
            self.display.delete(0,tk.END)
            self.display.insert(0,"Error")
            self.expression=""

if __name__=="__main__":
    Calculator().window.mainloop()