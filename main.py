import time
import tkinter as tk
from tkinter import Button
from tkinter import *
from equation import *


#############################################################################################################!!!!
#############################################################################################################!!!!
#############################################################################################################!!!!
#############################################################################################################!!!!
def mTokm():
    windowM = tk.Toplevel(root)
    windowM.title("Equation Solver.M To Km")
    canvasM = tk.Canvas(windowM, width=700, height=400)
    canvasM.pack()
    frameM = tk.Frame(windowM, bg="gray")
    frameM.place(relx=0.157, rely=0.1, relwidth=0.7, relheight=0.8)
    ansLabelM = tk.Label(frameM, text="Answer :", bg="gray", font=("Courier", 18))
    ansLabelM.place(relx=0.19, rely=0.7, relwidth=0.23, relheight=0.23)
    distLabelM = tk.Label(
        frameM, text="Distance As M:", bg="gray", font=("Courier", 11)
    )
    distLabelM.place(relx=0.12, rely=0.17, relwidth=0.29, relheight=0.23)
    timeLabelM = tk.Label(frameM, text="Time :", bg="gray", font=("Courier", 11))
    timeLabelM.place(relx=0.453, rely=0.17, relwidth=0.23, relheight=0.23)
    timeAmountM = tk.Entry(frameM, bg="white")
    distanceAmountM = tk.Entry(frameM, bg="white")
    distanceAmountM.place(relx=0.43, rely=0.17, relwidth=0.23, relheight=0.23)
    distanceAmountM.insert(tk.END, "{}".format(1000))
    TM = tk.Entry(frameM, bg="white")
    TM.place(relx=0.44, rely=0.7, relwidth=0.23, relheight=0.23)
    solveBtnM = tk.Button(
        frameM,
        text="Solve",
        command=lambda: mTOkmMain(distanceAmountM, timeAmountM, TM),
    )
    solveBtnM.place(relx=0.43, rely=0.44, relwidth=0.23, relheight=0.23)


def KmToM():
    windowKM = tk.Toplevel(root)
    windowKM.title("Equation Solver.Km To M")
    canvasKM = tk.Canvas(windowKM, width=700, height=400)
    canvasKM.pack()
    frameKM = tk.Frame(windowKM, bg="gray")
    frameKM.place(relx=0.157, rely=0.1, relwidth=0.7, relheight=0.8)
    ansLabelKM = tk.Label(frameKM, text="Answer :", bg="gray", font=("Courier", 18))
    ansLabelKM.place(relx=0.19, rely=0.7, relwidth=0.23, relheight=0.23)
    distLabelKM = tk.Label(
        frameKM, text="Distance As Km:", bg="gray", font=("Courier", 11)
    )
    distLabelKM.place(relx=0.12, rely=0.17, relwidth=0.29, relheight=0.23)
    timeLabelKM = tk.Label(frameKM, text="Time :", bg="gray", font=("Courier", 11))
    timeLabelKM.place(relx=0.453, rely=0.17, relwidth=0.23, relheight=0.23)
    timeAmountKM = tk.Entry(frameKM, bg="white")
    distanceAmountKM = tk.Entry(frameKM, bg="white")
    distanceAmountKM.place(relx=0.43, rely=0.17, relwidth=0.23, relheight=0.23)
    distanceAmountKM.insert(tk.END, "{}".format("2"))
    TKM = tk.Entry(frameKM, bg="white")
    TKM.place(relx=0.44, rely=0.7, relwidth=0.23, relheight=0.23)
    solveBtnKM = tk.Button(
        frameKM,
        text="Solve",
        command=lambda: kmTomMain(distanceAmountKM, timeAmountKM, TKM),
    )
    solveBtnKM.place(relx=0.43, rely=0.44, relwidth=0.23, relheight=0.23)


def sToHr():
    windowS = tk.Toplevel(root)
    windowS.title("Equation Solver.Sec To Hr")
    canvasS = tk.Canvas(windowS, width=700, height=400)
    canvasS.pack()
    frameS = tk.Frame(windowS, bg="gray")
    frameS.place(relx=0.157, rely=0.1, relwidth=0.7, relheight=0.8)
    ansLabelS = tk.Label(frameS, text="Answer :", bg="gray", font=("Courier", 18))
    ansLabelS.place(relx=0.19, rely=0.7, relwidth=0.23, relheight=0.23)
    distLabelS = tk.Label(frameS, text="Time As S:", bg="gray", font=("Courier", 11))
    distLabelS.place(relx=0.12, rely=0.17, relwidth=0.23, relheight=0.23)
    distanceAmountS = tk.Entry(frameS, bg="white")
    distanceAmountS.insert(END, "123")
    timeAmountS = tk.Entry(frameS, bg="white")
    timeAmountS.place(relx=0.43, rely=0.17, relwidth=0.23, relheight=0.23)
    timeAmountS.insert(tk.END, "{}".format(7200))
    TS = tk.Entry(frameS, bg="white")
    TS.place(relx=0.44, rely=0.7, relwidth=0.23, relheight=0.23)
    solveBtnS = tk.Button(
        frameS,
        text="Solve",
        command=lambda: sToHrMain(timeAmountS, distanceAmountS, TS),
    )
    solveBtnS.place(relx=0.43, rely=0.44, relwidth=0.23, relheight=0.23)


def HrToS():
    windowHr = tk.Toplevel(root)
    windowHr.title("Equation Solver.Hr To Sec")
    canvasS = tk.Canvas(windowHr, width=700, height=400)
    canvasS.pack()
    frameHr = tk.Frame(windowHr, bg="gray")
    frameHr.place(relx=0.157, rely=0.1, relwidth=0.7, relheight=0.8)
    ansLabelHr = tk.Label(frameHr, text="Answer :", bg="gray", font=("Courier", 18))
    ansLabelHr.place(relx=0.19, rely=0.7, relwidth=0.23, relheight=0.23)
    distLabelHr = tk.Label(frameHr, text="Time As Hr:", bg="gray", font=("Courier", 11))
    distLabelHr.place(relx=0.12, rely=0.17, relwidth=0.23, relheight=0.23)
    distanceAmountHr = tk.Entry(frameHr, bg="white")
    distanceAmountHr.insert(END, "123")
    timeAmountHr = tk.Entry(frameHr, bg="white")
    timeAmountHr.place(relx=0.43, rely=0.17, relwidth=0.23, relheight=0.23)
    timeAmountHr.insert(tk.END, "{}".format(2))
    THr = tk.Entry(frameHr, bg="white")
    THr.place(relx=0.44, rely=0.7, relwidth=0.23, relheight=0.23)
    solveBtnHr = tk.Button(
        frameHr,
        text="Solve",
        command=lambda: HrToSMain(timeAmountHr, distanceAmountHr, THr),
    )
    solveBtnHr.place(relx=0.43, rely=0.44, relwidth=0.23, relheight=0.23)


def HrToSMain(var1, var2, var3):
    var2s = var1.get()
    emptyVeloS = VelocityA(int(var2.get()), var2s)
    AnsS = emptyVeloS.FindTimeAsSecond()
    if var1 != "Hellowordaadadadadad":
        var1.delete(0, END)

        var3.delete(0, END)

        var3.insert(tk.END, float("{}".format(float(AnsS))))
        var3.insert(tk.END, " S")


def sToHrMain(var1, var2, var3):
    var2s = var1.get()
    emptyVeloS = VelocityA(int(var2.get()), var2s)
    AnsS = emptyVeloS.FindTimeAsHr()
    if var1 != "Hellowordaadadadadad":
        var1.delete(0, END)

        var3.delete(0, END)

        var3.insert(tk.END, float("{}".format(float(AnsS))))
        var3.insert(tk.END, " Hr")


def kmTomMain(var1, var2, var3):

    emptyVeloKM = VelocityA(var1.get())
    AnsKM = emptyVeloKM.FindDistanceAsM()
    if var1 != "Helloworadadadgadad":
        var1.delete(0, END)
        var2.delete(0, END)
        var3.delete(0, END)

        var3.insert(tk.END, float("{}".format(float(AnsKM))))
        var3.insert(tk.END, " M")


def mTOkmMain(var1, var2, var3):

    emptyVeloM = VelocityA(var1.get())
    AnsM = emptyVeloM.FindDistanceAsKm()
    if var1 != "Helloworadadadadad":
        var1.delete(0, END)
        var2.delete(0, END)
        var3.delete(0, END)

        var3.insert(tk.END, float("{}".format(float(AnsM))))
        var3.insert(tk.END, " KM")


def main():

    emptyVelo = VelocityA(distanceAmount.get(), timeAmount.get())
    AnsV = emptyVelo.FindVelocity()
    # if distanceAmount
    if distanceAmount != "Helloworadadadadad":
        distanceAmount.delete(0, END)
        timeAmount.delete(0, END)

        T.delete(0, END)
        T.insert(tk.END, float("{}".format(float(AnsV))))
        T.insert(tk.END, " M/S")


#############################################################################################################!!!!
#############################################################################################################!!!!
#############################################################################################################!!!!
#############################################################################################################!!!!


root = tk.Tk()

canvas = tk.Canvas(root, width=700, height=400)
canvas.pack()
root.title("Equation Solver")
frame = tk.Frame(root, bg="gray")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
T = tk.Entry(frame)
T.place(relx=0.44, rely=0.7, relwidth=0.23, relheight=0.23)
timeAmount = tk.Entry(frame, bg="white")
timeAmount.place(relx=0.69, rely=0.17, relwidth=0.15, relheight=0.23)
timeAmount.insert(tk.END, "2")
solveBtn = tk.Button(frame, text="Solve", command=main)
solveBtn.place(relx=0.43, rely=0.44, relwidth=0.23, relheight=0.23)
ansLabel = tk.Label(frame, text="Answer :", bg="gray", font=("Courier", 18))
ansLabel.place(relx=0.19, rely=0.7, relwidth=0.23, relheight=0.23)
distLabel = tk.Label(root, text="Distance As M:", bg="gray", font=("Courier", 11))
distLabel.place(relx=0.099, rely=0.20, relwidth=0.23, relheight=0.23)
timeLabel = tk.Label(frame, text="Time As Sec:", bg="gray", font=("Courier", 11))
timeLabel.place(relx=0.4632, rely=0.17, relwidth=0.23, relheight=0.23)
distanceAmount = tk.Entry(frame, bg="white")
distanceAmount.insert(tk.END, "10")
distanceAmount.place(relx=0.3, rely=0.17, relwidth=0.15, relheight=0.23)


menubar = tk.Menu(root)
menubar.add_command(label="Distance From M to Km", command=mTokm)
menubar.add_command(label="Distance From Km to M", command=KmToM)
menubar.add_command(label="Time From Sec to Hr", command=sToHr)
menubar.add_command(label="Time From Hr to Sec", command=HrToS)

root.config(menu=menubar)
tk.mainloop()
