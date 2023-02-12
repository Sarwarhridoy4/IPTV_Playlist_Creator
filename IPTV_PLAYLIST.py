import tkinter as tk
from tkinter import filedialog

def save_list():
    file = filedialog.asksaveasfile(mode ='w', defaultextension=".m3u")
    if file:
        for item in channels_list:
            file.write(f"#EXTINF:-1, {item[0]}\n")
            file.write(f"{item[2]}\n")
        file.close()

def add_channel():
    channel_name = channel_name_entry.get()
    channel_logo = channel_logo_entry.get()
    channel_url = channel_url_entry.get()
    channels_list.append((channel_name, channel_logo, channel_url))
    channels_listbox.insert("end", channel_name)
    channel_name_entry.delete(0, "end")
    channel_logo_entry.delete(0, "end")
    channel_url_entry.delete(0, "end")

root = tk.Tk()
root.title("IPTV Playlist Maker")
root.geometry("400x400")

channels_list = []

channel_name_label = tk.Label(root, text="Channel Name:")
channel_name_label.pack(pady=10)
channel_name_entry = tk.Entry(root)
channel_name_entry.pack(pady=10)

channel_logo_label = tk.Label(root, text="Channel Logo:")
channel_logo_label.pack(pady=10)
channel_logo_entry = tk.Entry(root)
channel_logo_entry.pack(pady=10)

channel_url_label = tk.Label(root, text="Channel URL:")
channel_url_label.pack(pady=10)
channel_url_entry = tk.Entry(root)
channel_url_entry.pack(pady=10)

add_channel_button = tk.Button(root, text="Add Channel", command=add_channel)
add_channel_button.pack(pady=10)

save_list_button = tk.Button(root, text="Save List", command=save_list)
save_list_button.pack(pady=10)

channels_listbox = tk.Listbox(root)
channels_listbox.pack(pady=10)

root.mainloop()
