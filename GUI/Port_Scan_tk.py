import tkinter as tk
from tkinter import messagebox
from socket import *

def scan_ports():
    target = entry_target.get()
    start_port = entry_start_port.get()
    end_port = entry_end_port.get()
    
    if not target:
        messagebox.showerror("Error", "Please enter a host to scan")
        return
    if not start_port.isdigit() or not end_port.isdigit():
        messagebox.showerror("Error", "Please enter valid port numbers")
        return
    
    start_port = int(start_port)
    end_port = int(end_port)
    
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        messagebox.showerror("Error", "Please enter a valid port range (1-65535)")
        return
    
    try:
        locaIP = gethostbyname(target)
    except Exception as e:
        messagebox.showerror("Error", f"Could not resolve host: {e}")
        return
    
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f'Starting scan on host: {locaIP}\n')
    
    for i in range(start_port, end_port + 1):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((locaIP, i))
        if conn == 0:
            result_text.insert(tk.END, f'Port {i}: OPEN\n')
        s.close()

#main window
root = tk.Tk()
root.title("Port Scanner")


tk.Label(root, text="Target:").pack(pady=5)
entry_target = tk.Entry(root, width=50)
entry_target.pack(pady=5)


tk.Label(root, text="Enter the start port:").pack(pady=5)
entry_start_port = tk.Entry(root, width=10)
entry_start_port.pack(pady=5)

# Create and place the end port label and entry
tk.Label(root, text="Enter the end port:").pack(pady=5)
entry_end_port = tk.Entry(root, width=10)
entry_end_port.pack(pady=5)

# Create and place the scan button
scan_button = tk.Button(root, text="Start Scan", command=scan_ports)
scan_button.pack(pady=5)

# Create and place the result text box
result_text = tk.Text(root, height=20, width=80)
result_text.pack(pady=5)

# Run the GUI event loop
root.mainloop()
