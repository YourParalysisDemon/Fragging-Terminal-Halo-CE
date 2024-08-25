import keyboard
import tkinter as tk
import pygame
import pymem.exception
import webbrowser
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer

while True:
    password = input("Enter password ")
    if password == "117":
        print("Welcome John-117")
        break
    else:
        print("Try again retard")

mem = Pymem("MCC-Win64-Shipping")

module1 = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll

primary_offsets = [0X28A]
fire_rate_offsets = [0X23A]
shield_offsets = [0XA0]
plasma_fire_rate_offsets = [0X204]
grenade_offsets = [0X2FC]
flashlight_offsets = [0X10, 0X10, 0X35C]
# This fucking sucked to find
noclip_offsets = [0X4D8]


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def multi_run_117():
    new_thread = Thread(target=John117, daemon=True)
    new_thread.start()


def multi_run_clip():
    new_thread = Thread(target=fuck_walls, daemon=True)
    new_thread.start()


def multi_run_gravity():
    new_thread = Thread(target=fuck_gravity, daemon=True)
    new_thread.start()


def multi_run_plasma():
    new_thread = Thread(target=plasma, daemon=True)
    new_thread.start()


def John117():  
    addr1 = getpointeraddress(module1 + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module1 + 0x01C38880, fire_rate_offsets)
    addr3 = getpointeraddress(module1 + 0x01C35AB0, shield_offsets)
    addr4 = getpointeraddress(module1 + 0x01C35AB0, grenade_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x47960000)
            mem.write_int(addr4, 0x100)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def fuck_walls():
    addr1 = getpointeraddress(module1 + 0x01C35AB0, noclip_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity():
    addr1 = getpointeraddress(module1 + 0x01C35AB0, noclip_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def plasma():
    addr1 = getpointeraddress(module1 + 0x01C38880, plasma_fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)

root = tk.Tk()
photo = tk.PhotoImage(file="back/155.png")
root.wm_iconphoto(False, photo)
root.attributes("-topmost", True)
root.title("Fragging Terminal")
root.configure(background='dark red')
root.geometry("265x175")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


button1 = tk.Button(root, text="Haha gun go brrr", bg='black', fg='white', command=multi_run_117)
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="No Clip", bg='black', fg='white', command=multi_run_clip)
button2.grid(row=3, column=0)
button3 = tk.Button(root, text="Plasma Firerate", bg='black', fg='white', command=multi_run_plasma)
button3.grid(row=2, column=0)
button3 = tk.Button(root, text="Fuck Gravity", bg='black', fg='white', command=multi_run_gravity)
button3.grid(row=4, column=0)
button4 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button4.grid(row=5, column=0)
label1 = tk.Label(master=root, text='- Show GUI', bg='red', fg='black')
label1.grid(row=0, column=3)
label2 = tk.Label(master=root, text='+ Hide GUI', bg='red', fg='black')
label2.grid(row=1, column=3)
label3 = tk.Label(master=root, text='F1 KILLS LOOPS', bg='red', fg='black')
label3.grid(row=2, column=3)
label4 = tk.Label(master=root, text='5 Gun go brrr', bg='red', fg='black')
label4.grid(row=3, column=3)
label5 = tk.Label(master=root, text='K KILL EXE', bg='red', fg='black')
label5.grid(row=4, column=3)
label5 = tk.Label(master=root, text='V No Clip', bg='red', fg='black')
label5.grid(row=5, column=3)
label5 = tk.Label(master=root, text='C turn on gravity', bg='red', fg='black')
label5.grid(row=6, column=3)
label6 = tk.Label(master=root, text='Main Loops', bg='red', fg='black')
label6.grid(row=0, column=0)
link1 = tk.Label(root, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="hand2")
link1.grid(row=6, column=0)
link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))

keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("5", multi_run_117)
keyboard.add_hotkey("V", multi_run_clip)
keyboard.add_hotkey("G", multi_run_gravity)
keyboard.add_hotkey("K", root.destroy)
root.mainloop()
