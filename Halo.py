import keyboard
import tkinter as tk
import pygame
import pymem.exception
import webbrowser
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from time import *
from tkinter import *

# Password
while True:
    password = input("Enter password ")
    if password == "117":
        print("Welcome John-117")
        break
    else:
        print("Try again retard")

# Game were hacking
mem = Pymem("MCC-Win64-Shipping")

# DLL of said game
module1 = module_from_name(mem.process_handle, "halo1.dll").lpBaseOfDll

# New graphics
primary_offsets = [0X28A]
fire_rate_offsets = [0X23A]
shield_offsets = [0XA0]
plasma_fire_rate_offsets = [0X204]
plasma_ammo_offsets = [0X208]
trig_offsets = [0X22C]  # 01C38880
shotgun_trig_offsets = [0X280]

# These fucking sucked to find
noclip_offsets = [0X4D8]
melee1_offsets = [0X512]
melee2_offsets = [0X513]
player_speed_offsets = [0X10C]
bullet_spread_offsets = [0X1B]
bullet_spread_offsets_2 = [0X1F]  # 01C38880/0x434800c8
scared = [0X34]  # 01C40480
pause = [0X38]  # 01C40480
animation = [0x0]  # 02D9CD90  

# Old graphics 01C38900 this game is janky as fuck
primary_offsets2 = [0X28A]
shield_offsets2 = [0XA0]
fire_rate_offsets2 = [0X23A]
plasma_ammo_offsets2 = []
noclip_offsets2 = [0X4D8]
X_offsets = [0X1C]  # 01C35950
Y_offsets = [0X18]  # 01C35950
Z_offsets = [0X20]
health2 = [0X68, 0X9C]


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


# Threads
def multi_run_117():
    new_thread = Thread(target=John117, daemon=True)
    new_thread.start()


def multi_run_0ld_117():
    new_thread = Thread(target=oldJohn117, daemon=True)
    new_thread.start()


def multi_run_gravity2():
    new_thread = Thread(target=fuck_gravity2, daemon=True)
    new_thread.start()


def multi_run_clip2():
    new_thread = Thread(target=fuck_walls2, daemon=True)
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


def multi_run_hands():
    new_thread = Thread(target=hands, daemon=True)
    new_thread.start()


def multi_run_speed():
    new_thread = Thread(target=speed, daemon=True)
    new_thread.start()


def multi_run_stats():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_nospread():
    new_thread = Thread(target=no_spread, daemon=True)
    new_thread.start()


def multi_run_bullet():
    new_thread = Thread(target=stats, daemon=True)
    new_thread.start()


def multi_run_pause():
    new_thread = Thread(target=pause_game, daemon=True)
    new_thread.start()


def multi_run_haha():
    new_thread = Thread(target=haha_number_go_brrr, daemon=True)
    new_thread.start()


def multi_run_shotgun():
    new_thread = Thread(target=shotgun, daemon=True)
    new_thread.start()


# Functions
def John117():
    addr1 = getpointeraddress(module1 + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module1 + 0x01C38880, fire_rate_offsets)
    addr3 = getpointeraddress(module1 + 0x01C35AB0, shield_offsets)
    addr4 = getpointeraddress(module1 + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x47960000)
            mem.write_int(addr4, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            mem.write_int(addr3, 0x3f800000)
            break


def shotgun():
    addr1 = getpointeraddress(module1 + 0x01C38880, primary_offsets)
    addr2 = getpointeraddress(module1 + 0x01C38880, shotgun_trig_offsets)
    addr3 = getpointeraddress(module1 + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0x0)
            mem.write_int(addr3, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def no_spread():
    addr1 = getpointeraddress(module1 + 0x01C38880, bullet_spread_offsets_2)
    addr2 = getpointeraddress(module1 + 0x01C38880, trig_offsets)
    addr3 = getpointeraddress(module1 + 0x01C38880, shotgun_trig_offsets)
    addr4 = getpointeraddress(module1 + 0x01C38880, fire_rate_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x000000c8)
            mem.write_int(addr2, 0x1)
            mem.write_int(addr3, 0x0)
            mem.write_int(addr4, 0xFFFFFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def wall_pierce():
    addr1 = getpointeraddress(module1 + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            break


def oldJohn117():
    addr1 = getpointeraddress(module1 + 0x01C38900, primary_offsets2)
    addr2 = getpointeraddress(module1 + 0x01C38900, fire_rate_offsets2)
    addr3 = getpointeraddress(module1 + 0x01C35950, shield_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x47960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr2, 0x3f800000)
            mem.write_int(addr3, 0x3f800000)
            break


def speed():
    addr1 = getpointeraddress(module1 + 0x01C40480, player_speed_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x41700000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x3f800000)
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
    addr1 = getpointeraddress(module1 + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_walls2():
    addr1 = getpointeraddress(module1 + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFF)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def fuck_gravity2():
    addr1 = getpointeraddress(module1 + 0x01C35950, noclip_offsets2)

    while 1:
        try:
            mem.write_int(addr1, 0x244)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("C"):
            mem.write_int(addr1, 0x0)
            break


def pause_game():
    addr1 = getpointeraddress(module1 + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def haha_number_go_brrr():
    addr1 = getpointeraddress(module1 + 0x01C40480, pause)
    addr2 = getpointeraddress(module1 + 0x01C40480, pause)

    while 1:
        try:
            mem.write_int(addr1, 0x00000000)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x1)
            break


def hands():
    addr1 = getpointeraddress(module1 + 0x01C35AB0, melee1_offsets)
    addr2 = getpointeraddress(module1 + 0x01C35AB0, melee2_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x1)
            mem.write_int(addr2, 0x1)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x30)
            break


def plasma():
    addr1 = getpointeraddress(module1 + 0x01C38880, plasma_fire_rate_offsets)
    addr2 = getpointeraddress(module1 + 0x01C38880, fire_rate_offsets)
    addr3 = getpointeraddress(module1 + 0x01C38880, plasma_ammo_offsets)
    addr4 = getpointeraddress(module1 + 0x01C38880, bullet_spread_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0xFFFFFFFF)
            mem.write_int(addr2, 0xFFFFFFFF)
            mem.write_int(addr3, 0x3f4ccccd)
            mem.write_int(addr4, 0x00000164)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


#  Tele functions

def tele_up():
    addr = getpointeraddress(module1 + 0x01C35950, Z_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_halo():
    addr = getpointeraddress(module1 + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module1 + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module1 + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x0)
            mem.write_int(addr1, 0x0)
            mem.write_int(addr2, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def tele_keys():
    addr = getpointeraddress(module1 + 0x01C35950, Z_offsets)
    addr1 = getpointeraddress(module1 + 0x01C35950, Y_offsets)
    addr2 = getpointeraddress(module1 + 0x01C35950, X_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0xbaf40305)
            mem.write_int(addr1, 0xe3860117)
            mem.write_int(addr2, 0x3f8fd600)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def stats():
    Reader = getpointeraddress(module1 + 0x01C35950, Z_offsets)
    Reader1 = getpointeraddress(module1 + 0x01C35950, Y_offsets)
    Reader2 = getpointeraddress(module1 + 0x01C35950, X_offsets)

    while 1:
        try:
            mem.read_float(Reader)
            mem.read_float(Reader1)
            mem.read_float(Reader2)
            print(Reader, Reader1, Reader2)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def clock():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    root.after(1000, clock)


# Are GUI
pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)

root = tk.Tk()
photo = tk.PhotoImage(file="back/155.png")
root.wm_iconphoto(False, photo)
root.attributes("-topmost", True)
root.title("Fragging Terminal")
root.configure(background='dark red')
root.geometry("350x275")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# New graphics
button1 = tk.Button(root, text="Bullet go brrr", bg='black', fg='white', command=multi_run_117)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="No Clip", bg='black', fg='white', command=multi_run_clip)
button2.grid(row=3, column=0)

button3 = tk.Button(root, text="Plasma go brrr", bg='black', fg='white', command=multi_run_plasma)
button3.grid(row=2, column=0)

button3 = tk.Button(root, text="Fuck Gravity", bg='black', fg='white', command=multi_run_gravity)
button3.grid(row=4, column=0)

button4 = tk.Button(root, text="Throw Hands", bg='black', fg='white', command=multi_run_hands)
button4.grid(row=5, column=0)

button5 = tk.Button(root, text="Speed", bg='black', fg='white', command=multi_run_speed)
button5.grid(row=6, column=0)

button6 = tk.Button(root, text="No Spread", bg='black', fg='white', command=multi_run_nospread)
button6.grid(row=7, column=0)

button7 = tk.Button(root, text="Shotgun", bg='black', fg='white', command=multi_run_shotgun)
button7.grid(row=8, column=0)

button8 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button8.grid(row=9, column=0)

# old graphics
button1 = tk.Button(root, text="Bullet go brrr", bg='black', fg='white', command=multi_run_0ld_117)
button1.grid(row=1, column=1)

button2 = tk.Button(root, text="Speed", bg='black', fg='white', command=multi_run_speed)
button2.grid(row=2, column=1)

button3 = tk.Button(root, text="Fuck Gravity", bg='black', fg='white', command=multi_run_gravity2)
button3.grid(row=3, column=1)

button4 = tk.Button(root, text="No Clip", bg='black', fg='white', command=multi_run_clip2)
button4.grid(row=4, column=1)

button5 = tk.Button(root, text="Tele up", bg='black', fg='white', command=tele_up)
button5.grid(row=5, column=1)

button6 = tk.Button(root, text="XYZ Stats", bg='black', fg='white', command=multi_run_stats)
button6.grid(row=6, column=1)

button7 = tk.Button(root, text="Pause", bg='black', fg='white', command=multi_run_pause)
button7.grid(row=7, column=1)

button8 = tk.Button(root, text="Confuse NPC", bg='black', fg='white', command=multi_run_haha)
button8.grid(row=8, column=1)

# Labels
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

label6 = tk.Label(master=root, text='New graphics', bg='red', fg='black')
label6.grid(row=0, column=0)

label7 = tk.Label(master=root, text='Old graphics', bg='red', fg='black')
label7.grid(row=0, column=1)
# Clock
time_label = Label(root, font=("Arial", 10), fg="Black", bg="Red")
time_label.grid(row=8, column=3)

day_label = Label(root, font=("Arial", 10), fg="Black", bg="Red")
day_label.grid(row=9, column=3)

date_label = Label(root, font=("Arial", 10), fg="Black", bg="Red")
date_label.grid(row=7, column=3)

clock()

# Links
link1 = tk.Label(root, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="hand2")
link1.grid(row=10, column=0)
link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))

# Hot keys
keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("5", multi_run_117)
keyboard.add_hotkey("6", multi_run_plasma)
keyboard.add_hotkey("V", multi_run_clip)
keyboard.add_hotkey("G", multi_run_gravity)
keyboard.add_hotkey("K", root.destroy)
root.mainloop()
