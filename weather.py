
import tkinter as tk
import time
import requests
from datetime import datetime
data=""
code=""




def getweather(city):
    global data
    global code
    key="d058b643eb32c383c2cc8641e0a3a493"
    api=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    r=requests.get(api)
    data=r.json()
    if r.status_code==200 and "json" in r.headers["Content-Type"]:
        code=200
        return True
    else:
        code=r.status_code
        return False

def showweather():
    d={}
    #print(data)
    d['city']=data["name"]
    d['time']=str(datetime.now()).split(".")[0]
    d['description']=data["weather"][0]["description"]
    d['temp']=str(data['main']['temp'])+" °C"
    d['feels like']=str(data["main"]["feels_like"])+" °C"
    d['pressure']=str(data["main"]["pressure"])+" hectopascal"
    d['humidity']=str(data["main"]["humidity"])+" %"
    d['sunrise']=time.ctime(data["sys"]["sunrise"]).split(" ")[3]
    d['sunset']=time.ctime(data["sys"]["sunset"]).split(" ")[3]
    top=tk.Toplevel(bg="wheat")
    
    for i in d:
        l={}
        left=i
        right=d[i]
        l[i]=tk.Label(top,font=("Angelina",13,"bold"),text=f'{left} : {right}'.title(),fg="#123456",bg="wheat",width=50)
        l[i].pack()
    
    bw1=tk.Button(font=("Angelina",16,"bold"),bg="#123456",fg="wheat",master=top,width=15,relief="groove",borderwidth=3,text="Exit",command=top.destroy)
    bw1.pack(pady=15,ipadx=4,ipady=10)
    def exit_top(event):
        top.destroy()
        
    

    
    top.grab_set()
    top.lift()
    #top.focus_force()
    top.title("Info")
    top.iconbitmap("Icons\\weather.ico")
    top.bind("<Escape>", exit_top)
    top.resizable(0,0)
    top.maxsize(310,310)
    top.minsize(310,310)

def showerror():
    top=tk.Toplevel(bg="wheat")
   
    
    le1=tk.Label(top,font=("Angelina",25,"bold"),text=f"Error {code} !!!",bg="#123456",fg="wheat")
    le1.pack(pady=30,ipadx=4,ipady=2)
    msg=data["message"].title()
    le2=tk.Label(top,font=("Angelina",15,"bold"),text=f"{msg}",bg="#123456",fg="wheat")
    le2.pack(pady=20,ipadx=4,ipady=2)
    
    be1=tk.Button(font=("Angelina",16,"bold"),bg="#123456",fg="wheat",master=top,width=15,relief="groove",borderwidth=3,text="Exit",command=top.destroy)
    be1.pack(pady=30,ipadx=4,ipady=10)
    def exit_top(event):
        top.destroy()
    
    top.grab_set()
    top.lift()
#     top.focus_force()
    top.title("Error")
    top.iconbitmap("Icons\\weather.ico")
    top.bind("<Escape>", exit_top)
    top.resizable(0,0)
    top.maxsize(310,310)
    top.minsize(310,310)
    
def fetch(e='e'):
    city=eb.get()
    eb.delete(0,last=len(city))
    x=getweather(str(city))
    if x:
        showweather()
    else:
        showerror()
        
root=tk.Tk()

city=tk.StringVar


x1=tk.Label(root,bg="#123456")
x1.grid(row=0,column=0,columnspan=7,ipady=10)


l1=tk.Label(root,text="  Enter City:   ",font=("Angelina",30,"bold"),fg="wheat",bg="#123456")
l1.grid(row=5,column=10,columnspan=3,rowspan=1,ipady=6)

y1=tk.Label(root)#,bg="#123456")
y1.grid(row=5,column=13,columnspan=12,ipady=10)


eb=tk.Entry(font=("Angelina",30,"bold"),bg="#C4BEAA",fg="#166C8E",master=root,width=15,relief="groove",borderwidth=3)
eb.focus()
eb.grid(row=5,column=13,columnspan=3,rowspan=1,ipady=5)


x2=tk.Label(root,bg="#123456")
x2.grid(row=6,column=16,columnspan=1,ipady=40)

b1=tk.Button(font=("Angelina",20,"bold"),bg="wheat",fg="#123456",master=root,width=15,relief="groove",borderwidth=3,text="Fetch Weather Info",command=fetch)

b2=tk.Button(font=("Angelina",20,"bold"),bg="wheat",fg="#123456",master=root,width=15,relief="groove",borderwidth=3,text="Exit",command=root.destroy)

b1.grid(row=7,column=15,ipady=2)

b2.grid(row=7,column=10,columnspan=2,rowspan=1,ipady=2)



x3=tk.Label(master=root,bg="#123456")
x3.grid(row=9,column=10,columnspan=7,ipady=10)

root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.title("Weather Info")
root.iconbitmap("Icons\\weather.ico")
root.bind("<Return>",fetch)
root.resizable(0,0)
root.maxsize(615,310)
root.minsize(615,310)
root.config(bg="#123456")
root.mainloop()
