'''import psutil
import time

while True:

   cpu_percent = psutil.cpu_percent(interval=None)
   print(f"CPU 사용량: {cpu_percent}%")

   mem = psutil.virtual_memory()
   mem_percent = mem.percent
   print(f"메모리 사용량: {mem_percent}%")

   net_io_counters = psutil.net_io_counters()
   bytes_sent = net_io_counters.bytes_sent
   bytes_recv = net_io_counters.bytes_recv
   print(F"네트워크 사용량: 송신={bytes_sent}bytes, 수신={bytes_recv}bytes")

   time.sleep(1)'''

import psutil
import tkinter as tk

window = tk.Tk()
window.title("시스템 모니터")

cpu_label = tk.Label(window, text="CPU 사용량: ")
cpu_label.pack()

ram_label = tk.Label(window, text="RAM 사용량: ")
ram_label.pack()

def update_usage():

   cpu_percent = psutil.cpu_percent(interval=None)
   cpu_label.config(text=f"CPU 사용량: {cpu_percent}%")

   mem =psutil.virtual_memory
   mem_percent = mem.percent
   ram_label.config(text=f"RAM 사용량: {mem_percent}%")

   window.after(1000, update_usage)

   update_usage

   window.mainloop()





   