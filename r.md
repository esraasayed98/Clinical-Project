### Server Flow

1) Home page:



![image](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen1.PNG)



2) When we choose **Radiology** :

![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen2.PNG)

the department's page appear with:

1. The department's devices with their serial numbers

2. Three buttons|:

   1. When we click on **View Devices' Details** , department's devices' details are reviewed

![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen3.PNG)

2. When we click on **Daily Inspection reporting**, we can add a new daily inspection report for all department's devices



   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen4.PNG)

   first, you need to insert date of the day
   then, check each point for each device and write your comment

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen5.PNG)

   after finishing inspection report for all devices, you need to add a signature and click submit to save the results at the data base

3. When we click on **View Department's Daily inspection Report**, a review report for all devices in the department appears

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen6.PNG)

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen7.PNG)

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen8.PNG)

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen9.PNG)

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen10.PNG)

   while , if you need a report for one device only, you need to enter its serial number in the input box, 
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen11.PNG)
   for an example, if you need to get the report for **Mammography** device , you have to enter its serial number 
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen13.PNG)
   to get its report
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen12.PNG)

   #### Comments:

   We have faced problems during searching for daily inspection for specific devices (Dye Injector , Diagnostic X-Ray , FCR),
   so we couldn't do a report for them, and an error page appears if their serial number is entered.
   for an example, if FCR serial number is entered, this page appears:

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/error.PNG)






3) When we choose **Open Heart**:
![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/open1.PNG)
the department's page appear with:

1. The department's devices with their serial numbers

2. The input box for PPM reporting, for applying report for each device by entering its serial number
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/open3.PNG)
   for an example, if we need to apply report for **Exercise Cardiac Report** 
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/reportPPM.PNG)
   after filling the report , you need to click submit to save the results at the data base.



3. The input box for reviewing each device's PPM report by entering its serial number

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/open4.PNG)

   for an example , if we search for Exercise ECG device's report
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/open6.PNG)



4. Two buttons|:

   1. When we click on **View Devices' Details** , department's devices' details are reviewed

![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/open2.PNG)

2. When we click on **View Department's PPM Report**, we can add a new daily inspection report for all department's devices

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/report1.PNG)
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/report2.PNG)
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/report3.PNG)
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/report4.PNG)
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/report5.PNG)



4) When we choose **Catheter** :
![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/catheter.PNG)
the department's page appear with:

1. The department's devices with their serial numbers

2. Three buttons:

   1. When we click on **View Devices' Details** , department's devices' details are reviewed



![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/catheter1.PNG)

2. When we click on **Daily Inspection reporting**, we can add a new daily inspection report for all department's devices

   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath1.PNG)
   first, you need to insert date of the day
   then, check each point for each device and write your comment
   ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath2.PNG)
   after finishing inspection report for all devices, you need to add a signature and click submit to save the results at the data base
        3. When we click on **View Department's Daily inspection Report**, a review report for all devices in the department appears
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath3.PNG)
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath4.PNG)
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath5.PNG)
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath6.PNG)
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath7.PNG)
        while , if you need a report for one device only, you need to enter its serial number in the input box, 
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/screen11.PNG)
      for an example, if you need to get the report for **Suction Machine** device , you have to enter its serial number 
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath8.PNG)
      to get its report
      ![picture](C:/Users/GEHAD/Desktop/Clinical-Project/Clinical-Project/images/cath9.PNG)


#### Comments:

  We needed to install:

  - Flask via "pip install flask"
  - "pip install anaconda mysql-connector-python"