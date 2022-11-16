import time 
import glob 
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = 'sys/bus/w1/devices/'
device_dir = glob.glob(base_dir + "28*")[0]
device_file = device_dir + 'w1_slave'
logging_file = "Path_of_media"


def read_temp_script () :
    f = open(device_file,'r')
    lines = f.readlines()
    f.close()
    return lines 

def read_temp ():
    lines = read_temp_script()
    while (lines[0].strip()[-3:]) != "YES") :
        lines = read_temp_script()
        time.sleep(1)
    
    position = lines[1].find('t=')
    if(position != -1):
        temp = lines[1][position+2:]
        temp_c = float(temp)/1000.0
        temp_f = 9.0*temp_c/5.0 + 32
        return temp_c, temp_f

def read ():
    while True :
        print (read_temp())
        time.sleep(1)
         
def log_temp():
    c,f = read_temp()
    f = open(logging_file, 'a')
    f.write(str(c)+ " " +str(f))
    f.close()
    


