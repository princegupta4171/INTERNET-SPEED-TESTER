from tkinter import *
import speedtest


#it is a function
def speedcheck():
	st = speedtest.Speedtest()
	st.get_servers()
	down = str(round(st.download()/(10**6),3))+"Mbps"
	up = str(round(st.upload()/(10**6),3))+"Mbps"
	lab_down.config(text=down)
	lab_up.config(text=up)



sp = Tk()
sp.title("internet speed tester")
sp.geometry("500x650")
sp.config(bg="Yellow")#background colour



lab = Label(sp,text="INTERNET SPEED TESTER ",font=("Time New Roman",20,"bold"),bg="Red",fg="White")
lab.place(x=50,y=10,height=50,width=380)

lab = Label(sp,text="DOWNLOAD SPEED",font=("Time New Roman",30,"bold"))
lab.place(x=50,y=90,height=50,width=380)

lab_down = Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_down.place(x=50,y=170,height=50,width=380)

lab = Label(sp,text="UPLOAD SPEED",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=250,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_up.place(x=60,y=330,height=50,width=380)
print("prince gupta")
button=Button(sp,text="CHECK SPEED",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)#in this a calling function
button.place(x=60,y=410,height=50,width=380)

sp.mainloop()
