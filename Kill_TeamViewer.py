import subprocess, tkinter


proc_list = subprocess.Popen('ps -A -o comm', shell=True, stdout=subprocess.PIPE).communicate()[0]

print(proc_list)
for i in proc_list:
    print(i)
# .communicate()[0].split('\n')[1:]



