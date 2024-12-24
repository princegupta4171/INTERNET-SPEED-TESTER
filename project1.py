from tkinter import *
import speedtest
import threading
import mysql.connector
from tkinter import messagebox

# MySQL connection setup
def create_connection():
    return mysql.connector.connect(
        host="localhost",   # Change this to your MySQL server host
        user="root",              # Corrected user format
        password="Prince@2006",   # Consider using environment variables for sensitive data
        database="speedtest_db"
    )

def insert_speed_results(download, upload):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        # Store speeds as numeric values
        cursor.execute("INSERT INTO speed_results (download_speed, upload_speed) VALUES (%s, %s)", (float(download[:-5]), float(upload[:-5])))
        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {str(err)}")
    finally:
        cursor.close()
        conn.close()
        print("succesfuly connection created to mysql")

def speedcheck():
    button.config(state=DISABLED)  # Disable the button during the test
    lab_down.config(text="Testing...")
    lab_up.config(text="Testing...")
    
    def run_speedtest():
        try:
            st = speedtest.Speedtest()
            st.get_best_server()  # Get the best server
            down = round(st.download() / (10**6), 3)  # Store as float
            up = round(st.upload() / (10**6), 3)      # Store as float
            lab_down.config(text=f"{down} Mbps")
            lab_up.config(text=f"{up} Mbps")
            insert_speed_results(down, up)  # Insert results into MySQL
        except Exception as e:
            messagebox.showerror("Error", f"Speed test failed: {str(e)}")
            lab_down.config(text="Error")
            lab_up.config(text="Error")
        finally:
            button.config(state=NORMAL)  # Re-enable the button

    # Run the speed test in a separate thread
    threading.Thread(target=run_speedtest).start()
4
# GUI setup
sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("500x650")
sp.config(bg="pink")

lab_title = Label(sp, text="INTERNET SPEED TESTER", font=("Times New Roman", 20, "bold"), bg="black", fg="white")
lab_title.place(x=50, y=10, height=50, width=380)

lab_download = Label(sp, text="DOWNLOAD SPEED", font=("Times New Roman", 30, "bold"), bg="aqua", fg="chocolate")
lab_download.place(x=50, y=90, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="cyan", fg="chocolate")
lab_down.place(x=50, y=170, height=50, width=380)

lab_upload = Label(sp, text="UPLOAD SPEED", font=("Times New Roman", 30, "bold"), bg="aqua", fg="chocolate")
lab_upload.place(x=60, y=250, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"), bg="cyan", fg="chocolate")
lab_up.place(x=60, y=330, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="Red", command=speedcheck)
button.place(x=60, y=410, height=50, width=380)

lab = Label(sp,text="MADE IT BY PRINCE GUPTA  ",font=("Time New Roman",10,"bold"),bg="PINK",fg="white")
lab.place(x=200,y=550,height=50,width=380)

lab = Label(sp,text="Rollno.=2305251530041(AKTU)  ",font=("Time New Roman",10,"bold"),bg="PINk",fg="white")
lab.place(x=200,y=600,height=50,width=380)


sp.mainloop()
