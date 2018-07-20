import numpy as np
import datetime
import requests
import time
import random

# Sunshine to Kanchi ITI route MAP.
id = 382056

x=np.array([[80.2095853,12.9738521],
		 [80.2095853,12.9738521],
		 [80.20842330000001,12.9747705],
		 [80.20772,12.9752998],
		 [80.20667950000001,12.9760827],
		 [80.20676690000001,12.9762001],
		 [80.2066358,12.9763036],
		 [80.2059958,12.9767689],
		 [80.2053032,12.9774211],
		 [80.2047544,12.977848],
		 [80.2042905,12.9781311],
		 [80.2041596,12.9782043],
		 [80.20419370000001,12.9785727],
		 [80.20421620000001,12.9788636],
		 [80.20426260000001,12.9792498],
		 [80.2042682,12.9792972],
		 [80.2043193,12.9796289],
		 [80.2043882,12.980053],
		 [80.2044708,12.9804651],
		 [80.2045437,12.9808577],
		 [80.2045969,12.9812036],
		 [80.2046484,12.9815817],
		 [80.2051312,12.9815204],
		 [80.20514660000001,12.9817148],
		 [80.2051774,12.9820136],
		 [80.2055409,12.9819773],
		 [80.2055857,12.9819731],
		 [80.2061616,12.9819185],
		 [80.2063076,12.9819046],
		 [80.20684900000001,12.9818557],
		 [80.2069082,12.9821994],
		 [80.2069449,12.9826453],
		 [80.20698400000001,12.9830678],
		 [80.20782989999999,12.9830208],
		 [80.2086381,12.982981],
		 [80.20886210000001,12.9829481],
		 [80.2090477,12.982925],
		 [80.20918039999999,12.9829179],
		 [80.2094441,12.9829005],
		 [80.2098432,12.9828972],
		 [80.2098945,12.9828944],
		 [80.21029919999999,12.9828671],
		 [80.2103012,12.9827335],
		 [80.2107218,12.9827543],
		 [80.2109766,12.9827602],
		 [80.211291,12.982768],
		 [80.21131730000001,12.9827688],
		 [80.21182469999999,12.9828146],
		 [80.2118655,12.9825004]] )
     
for len in range (0 , x.shape[0]):
     longx = str(x[len,0])
     latx  = str(x[len,1])
     utc_datetime = datetime.datetime.utcnow()
     timex =utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(id))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(random.randint(10,40)),headers={'Connection':'close'})
     delay_time = random.randint(20,50) 
     time.sleep(delay_time)
for loop in range (0,4):
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(id))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0),headers={'Connection':'close'})
     delay_time = random.randint(20,50)  
     time.sleep(delay_time)      
     
time.sleep(300)

for len in range (x.shape[0],0,-1):
     longx = str(x[len-1,0])
     latx  = str(x[len-1,1])
     utc_datetime = datetime.datetime.utcnow()
     timex =utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(id))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(random.randint(10,40)),headers={'Connection':'close'})
     delay_time = random.randint(20,50)  
     time.sleep(delay_time)
for loop in range (0,4):
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(id))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0),headers={'Connection':'close'})
     delay_time = random.randint(20,50)  
     time.sleep(delay_time)   

