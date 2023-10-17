import tkinter as tk
import tkinter.ttk as ttk
import os
from setuptools import Command

f1 = open("C:\\Users\\user\\Documents\\投票用紙.txt",'a')
kaityouval=[]
hukukaityouval=[]
kaikeival=[]
syokival=[]


def kaityou():
    global frame_1
    frame.destroy()

    frame_1 = ttk.Frame(root)
    frame_1.pack(fill = tk.BOTH, pady=20)
    lab = tk.Label(frame_1,text = '会長\n' )
    lab.pack(anchor=tk.CENTER)

    button_change = ttk.Button(frame_1, text="ウィンドウ変更", command=hukukaityou)
    
    for x in range(kaityoukazu):
        check_val[x] = tk.BooleanVar()
        check_btn[x] = tk.Checkbutton(frame_1,text=datalist[4+x], variable=check_val[x])
        check_btn[x].pack(anchor=tk.CENTER) 

    button_change.pack(side=tk.RIGHT,anchor=tk.SE, ipadx = 20, ipady = 10)
    root.mainloop()
    #f1 = open("C:\\Users\\user\\Documents\\投票用紙.txt",'a')
    for i in range(0,kaityoukazu,1):
        if  check_val[i].get():
            f1.write(datalist[4+i]+'1\n')
        else:
            f1.write(datalist[4+i]+'0\n')
    f1.close

def hukukaityou():
    global frame_2
    frame_1.destroy()

    frame_2 = ttk.Frame(root)
    frame_2.pack(fill = tk.BOTH, pady=20)

    lab = tk.Label(frame_2,text = '副会長\n' )
    lab.pack(anchor=tk.CENTER)
    next = tk.Button(frame_2,text="次",command=fin)

    for x in range(hukukaityoukazu):
        check_val[x] = tk.BooleanVar()
        check_btn[x] = tk.Checkbutton(frame_2,text=datalist[4+kaityoukazu+x], variable=check_val[x])
        check_btn[x].pack(anchor=tk.CENTER) 

    next.pack(side=tk.RIGHT,anchor=tk.S,ipadx = 20, ipady = 10)
    root.mainloop()

    #f1=open("C:\\Users\\user\\Documents\\投票用紙.txt",'a')
    for i in range(0,hukukaityoukazu,1):
        if  check_val[i].get():
            f1.write(datalist[4+kaityoukazu+i]+'1\n')
        else:
            f1.write(datalist[4+kaityoukazu+i]+'0\n')
    f1.close
    

def fin():
    root.destroy()

if __name__ == "__main__":
    #GUI設定
    root = tk.Tk()
    root.title("テスト用ウィンドウ")
    root.geometry("400x300")
    label = {}
    check_val = {}
    check_btn = {}

    #ファイルの操作
    f = open(r"C:\Users\user\Documents\生徒会候補.txt",encoding="utf-8")
    datalist = f.readlines()
    f.close()
    kaityoukazu=int(datalist[0])
    hukukaityoukazu=int(datalist[1])
    kaikeikazu=int(datalist[2])
    syokikazu=int(datalist[3])

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)
    button_change = ttk.Button(frame, text="投票開始",command=kaityou)

    button_change.pack()
    root.mainloop()