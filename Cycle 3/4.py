import numpy as np
import matplotlib.pyplot as plt
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")

product=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
affordable_segment=[173,153,195,147,120,144,148,109,174,130,172,131]
luxuary_segment=[189,189,105,112,173,109,151,197,174,145,177,161]
super_luxuary=[185,185,126,134,196,153,112,133,200,145,167,110]
plt.plot(product,affordable_segment,'r--',label='Affordable Segment')
plt.plot(product,luxuary_segment, 'g-.',label='Luxuary Segment')
plt.plot(product,super_luxuary,'b-',label='Super luxuary segment')
plt.xlabel('Months of year')
plt.ylabel('Sales of segments')
plt.title('Sales data')
plt.legend(loc='upper right')
plt.show()