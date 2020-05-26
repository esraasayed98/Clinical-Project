# Clinical Final Project


## Team: 18

## Submitted By:  

Alzahraa Eid Abd El-Fattah

Alzahraa Mahmoud

Amany Bahaa El-Din Mustafa

Esraa Sayed Mustafa

Mustafa Tawfik

-------------




## Pre-Requistics:

1) Create data base with name ***clinicaldatabase***.
2) In data base import file ***clinicaldatabase.sql***.
3) Run file ***server.py***

---------------

# Server Flow

1) Home page:



![image](images/screen1.PNG)



2) When we choose **Radiology** :

![picture](images/screen2.PNG)



the department's page appear with:

1. The department's devices with their serial numbers

2. Three buttons|:

   1. When we click on **View Devices' Details** , department's devices' details are reviewed

![picture](images/screen3.PNG)

2. When we click on **Daily Inspection reporting**, we can add a new daily inspection report for all department's devices

![picture](images/screen4.PNG)

   first, you need to insert date of the day
   then, check each point for each device and write your comment

   

 ![picture](images/screen5.PNG)

   after finishing inspection report for all devices, you need to add a signature and click submit to save the results at the data base

3. When we click on **View Department's Daily inspection Report**, a review report for all devices in the department appears



![picture](images/screen6.PNG)

![picture](images/screen7.PNG)

![picture](images/screen8.PNG)

![picture](images/screen9.PNG)

![picture](images/screen10.PNG)

while , if you need a report for one device only, you need to enter its serial number in the input box, 
![picture](images/screen11.PNG)

for an example, if you need to get the report for **Mammography** device , you have to enter its serial number.

![picture](images\screen13.PNG)

to get its report
![picture](images/screen12.PNG)

#### Comments:

We have faced problems during searching for daily inspection for specific devices (Dye Injector , Diagnostic X-Ray , FCR),
so we couldn't do a report for them, and an error page appears if their serial number is entered.
for an example, if FCR serial number is entered, this page appears:



![picture](/images/error.PNG)





3) When we choose **Open Heart**: