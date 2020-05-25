# Clinical Final Project
----------
## Team: 18
## Submitted By:  
Alzahraa Eid Abd El-Fattah

Alzahraa Mahmoud

Amany Bahaa El-Din Mustafa

Esraa Sayed Mustafa

Mustafa Tawfik

-------------
------------



## Pre-Requistics:
1) Create data base with name ***clinicaldatabase***.
2) In data base import file ***clinicaldatabase.sql***.
3) Run file ***server.py***

---------------
# Server Flow
1) Home page:
![picture](images\screen1.png)
----
2) When we choose **Radiology** :
![picture](images\screen2.png)
the department's page appear with:

    1. The department's devices with their serial numbers

    2. Three buttons|:

        1. When we click on **View Devices' Details** , department's devices' details are reviewed
![picture](images\screen3.png)

        2. When we click on **Daily Inspection reporting**, we can add a new daily inspection report for all department's devices
   ![picture](images\screen4.png)
   first, you need to insert date of the day
   then, check each point for each device and write your comment
   ![picture](images\screen5.png)
   after finishing inspection report for all devices, you need to add a signature and click submit to save the results at the data base
        3. When we click on **View Department's Daily inspection Report**, a review report for all devices in the department appears
   ![picture](images\screen6.png)
   ![picture](images\screen7.png)
   ![picture](images\screen8.png)
   ![picture](images\screen9.png)
   ![picture](images\screen10.png)
   while , if you need a report for one device only, you need to enter its serial number in the input box, 
   ![picture](images\screen11.png)
   for an example, if you need to get the report for **Mammography** device , you have to enter its serial number 
   ![picture](images\screen13.png)
   to get its report
   ![picture](images\screen12.png)
   #### Comments:
   We have faced problems during searching for daily inspection for specific devices (Dye Injector , Diagnostic X-Ray , FCR),
   so we couldn't do a report for them, and an error page appears if their serial number is entered.
   for an example, if FCR serial number is entered, this page appears:

   ![picture](images\error.png)





------------------

3) When we choose **Open Heart**:
![picture](images\open1.png)
the department's page appear with:

    1. The department's devices with their serial numbers

    2. The input box for PPM reporting, for applying report for each device by entering its serial number
    ![picture](images\open3.png)
    for an example, if we need to apply report for **Exercise Cardiac Report** 
    ![picture](images\reportPPM.png)
    after filling the report , you need to click submit to save the results at the data base.


    3. The input box for reviewing each device's PPM report by entering its serial number

          ![picture](images\open4.png)

       for an example , if we search for Exercise ECG device's report
       ![picture](images\open6.png)



    4. Two buttons|:

        1. When we click on **View Devices' Details** , department's devices' details are reviewed
![picture](images\open2.png)

        2. When we click on **View Department's PPM Report**, we can add a new daily inspection report for all department's devices
   ![picture](images\report1.png)
   ![picture](images\report2.png)
   ![picture](images\report3.png)
   ![picture](images\report4.png)
   ![picture](images\report5.png)


------------------------------

2) When we choose **Catheter** :
![picture](images\catheter.png)
the department's page appear with:

    1. The department's devices with their serial numbers

    2. Three buttons:

        1. When we click on **View Devices' Details** , department's devices' details are reviewed
![picture](images\catheter1.png)

        2. When we click on **Daily Inspection reporting**, we can add a new daily inspection report for all department's devices
   ![picture](images\cath1.png)
   first, you need to insert date of the day
   then, check each point for each device and write your comment
   ![picture](images\cath2.png)
   after finishing inspection report for all devices, you need to add a signature and click submit to save the results at the data base
        3. When we click on **View Department's Daily inspection Report**, a review report for all devices in the department appears
   ![picture](images\cath3.png)
   ![picture](images\cath4.png)
   ![picture](images\cath5.png)
   ![picture](images\cath6.png)
   ![picture](images\cath7.png)
    while , if you need a report for one device only, you need to enter its serial number in the input box, 
   ![picture](images\screen11.png)
   for an example, if you need to get the report for **Suction Machine** device , you have to enter its serial number 
   ![picture](images\cath8.png)
   to get its report
   ![picture](images\cath9.png)


#### Comments:
  We needed to install:
  - Flask via "pip install flask"
  - "pip install anaconda mysql-connector-python"
  

--------------------