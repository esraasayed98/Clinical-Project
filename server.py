import mysql.connector
from flask import Flask, redirect, url_for, request,render_template

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="clinicaldatabase"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

#open heart department code

@app.route('/OpenHeartDepartment')
def OpenHeartDepartment():
    
      mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         
         'rec':myresult,
         'header':row_headers
      }
      return render_template('open_heart.html',data=data)


@app.route('/getppmdevice',methods =['POST'])
def getppmdevice():
    serial1 = request.form['serial1']
    if serial1 == '070-12242':
        mycursor.execute("SELECT * FROM PPM_ECG")
        mes='PPM_ECG'
    elif serial1 == '135224798':
        mycursor.execute("SELECT * FROM PPM_Syringe_Pump")
        mes='PPM_Syringe_Pump'
    elif serial1 == '1387-111678':
         mycursor.execute("SELECT * FROM PPM_Monitor")
         mes='PPM_Monitor'
    elif serial1 == '182447':
         mycursor.execute("SELECT * FROM PPM_Suction_unit")
         mes='PPM_Suction_unit'
    elif serial1 == 'FN000060':
         mycursor.execute("SELECT * FROM PPM_ECG_Ultrasound")
         mes='PPM_ECG_Ultrasound'
    elif serial1 == 'Fv-12133':
         mycursor.execute("SELECT * FROM PPM_Exercise_ECG")
         mes='PPM_Exercise_ECG'
    elif serial1 == 'T8135':
         mycursor.execute("SELECT * FROM PPM_Mobile_X_ray")
         mes='PPM_Mobile_X_ray'
    elif serial1 == 'TV01405054F':
         mycursor.execute("SELECT * FROM PPM_Ventilator")
         mes='PPM_Ventilator'
    elif serial1 == 'US71514674':
         mycursor.execute("SELECT * FROM PPM_Defibrillator")
         mes='PPM_Defibrillator'
    elif serial1 == '14037475':
         mycursor.execute("SELECT * FROM PPM_Measure_blood_gas")
         mes='PPM_Measure_blood_gas'
    else:
        mes="No matching device ...."
        return render_template('error.html',message=mes)
    
    
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         'message':mes,
         'rec':myresult,
         'header':row_headers
    }
    return render_template('ppmdevice.html',data=data)
    
    
@app.route('/getppmdepartment')
def getppmdepartment():
    
    mycursor.execute("SELECT * FROM PPM_Suction_unit")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data1={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Ventilator")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data2={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Mobile_X_ray")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data3={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_ECG_Ultrasound")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data4={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Monitor")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data5={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_ECG")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data6={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Syringe_Pump")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data7={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Defibrillator")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data8={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Measure_blood_gas")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data9={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT * FROM PPM_Exercise_ECG")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data10={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('Totalppmreport.html',data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9,data10=data10)

    
@app.route('/PPMform',methods =['POST'])
def PPMform():
    serial2 = request.form['serial2']
    if serial2 == '070-12242':
        return render_template('ECG.html')
    elif serial2 == '135224798':
        
        return render_template('pump_syringe.html')
    elif serial2 == '1387-111678':
         
        return render_template('monitor.html')
    elif serial2 == '182447':
         return render_template('suction_unit.html')
        
    elif serial2 == 'FN000060':
         return render_template('ECG_ultrasound.html')
    elif serial2 == 'Fv-12133':
         return render_template('exercise.html')
    elif serial2 == 'T8135':
         return render_template('X_ray.html')
    elif serial2 == 'TV01405054F':
         return render_template('vent.html')
    elif serial2 == 'US71514674':
         return render_template('defibrillator.html')
    elif serial2 == '14037475':
         return render_template('blood_gas.html')
    else:
        mes="No matching device ...."
        return render_template('error.html',message=mes)
    

@app.route('/suctionunit',methods =['POST'])
def suctionunit():    
    date = request.form['date']
    tubing = request.form['tubing']
    collection = request.form['collection']
    Filter = request.form['filter']
    battery = request.form['battery']
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Suction_unit (`PPM_Date`,`Tubing`,`collection bottle`,`filter`,`Battery`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (date,tubing,collection,Filter,battery,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/monitor',methods =['POST'])
def monitor():    
    date = request.form['date']
    hardware = request.form['hardware']
    screws = request.form['screws']
    case = request.form['case']
    panel = request.form['panel']
    power = request.form['power']
    pswitch = request.form['pswitch']
    touch = request.form['touch']
    parameters = request.form['parameters']
    alarm = request.form['alarm']
    check = request.form['check']
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Monitor (`PPM_Date`,`Mounting hard Ware`,`screws`,`Case and cables connector`,`Flat panel display frame`,`Power supply`,`Power switch`,`Touch screen in the event`,`Functional test`,`Alarm limits`,`Network`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date,hardware,screws,case,panel,power,pswitch,touch,parameters,alarm,check,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)


@app.route('/ecg_ult',methods =['POST'])
def ecg_ult():    
    date = request.form['date']
    VS = request.form['VS']
    SD = request.form['SD']
    SC = request.form['SC']
    Sda = request.form['Sda']
    SR = request.form['SR']
    DI = request.form['DI']
    FPC = request.form['FPC']
    LT = request.form['LT']
    
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_ECG_Ultrasound (`PPM_Date`,`Visual inspection`,`System diagnostic`,`System cleaning`,`system disassembly`,`System reassembly`,`Diagnostic imaging`,`Fall pass criteria`,`Leakage testing`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date,VS,SD,SC,Sda,SR,DI,FPC,LT,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)


@app.route('/vent',methods =['POST'])
def vent():    
    date = request.form['date']
    IF = request.form['IF']
    OC = request.form['OC']
    DH = request.form['DH']
    LM = request.form['LM']
    connectors = request.form['connectors']
    FD = request.form['FD']
    PC = request.form['PC']
    external = request.form['external']
    
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Ventilator (`PPM_Date`,`Inlet filter`,`Outer closure`,`Door hinge`,`Latch mechanism`,`Connectors`,`Handle`,`Power cord`,`External tubing`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date,IF,OC,DH,LM,connectors,FD,PC,external,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)


@app.route('/xray',methods =['POST'])
def xray():    
    date = request.form['date']
    XP = request.form['XP']
    IA = request.form['IA']
    IC = request.form['IC']
    SI = request.form['SI']
    WL = request.form['WL']
    CS = request.form['CS']
    CI = request.form['CI']
     
    
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Mobile_X_ray (`PPM_Date`,`X_ray production`,`Image Acquisition`,`Interior cleaning`,`Safety interlock`,`Warning lamp`,`Sensors`,`Future issues`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date,XP,IA,IC,SI,WL,CS,CI,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/bloodgas',methods =['POST'])
def bloodgas():    
    date = request.form['date']
    CAP = request.form['CAP']
    CEHP = request.form['CEHP']
    CSP = request.form['CSP']
        
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Measure_blood_gas (`PPM_Date`,`Analyzer performance`,`Electronic hardware performance`,`Soft ware performance`,`Signature`) VALUES (%s, %s, %s, %s, %s)"
    val = (date,CAP,CEHP,CSP,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/defrillator',methods =['POST'])
def defrillator():    
    date = request.form['date']
    CSAC = request.form['CSAC']
    CSB = request.form['CSB']
    disarm = request.form['disarm']
    AR = request.form['AR'] 
    PS = request.form['PS']
    RP = request.form['RP']
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Defibrillator (`PPM_Date`,`Check the shock powered by AC only`,`Check the shock powered by battery only`,`Check disarm while pressing disarm key`,`Check analyzer readings after delivering 200J shock`,`Check printed strip`,`Repeat the test using paddles`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date,CSAC,CSB,disarm,AR,PS,RP,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/ecg',methods =['POST'])
def ecg():    
    date = request.form['date']
    CP = request.form['CP']
    CLCD = request.form['CLCD']
    CR = request.form['CR']
    AS = request.form['AS'] 
     
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_ECG (`PPM_Date`,`Power`,`LCD main menu`,`ECG Room`,`Adequate supplies`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (date,CP,CLCD,CR,AS,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/exercise',methods =['POST'])
def exercise():    
    date = request.form['date']
    CPN = request.form['CPN']
    CCC = request.form['CCC']
    CM = request.form['CM']
    PCC = request.form['PCC']
    TP = request.form['TP']
     
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Exercise_ECG (`PPM_Date`,`power and cables`,`Cords and connectors`,`missing screws cracks or broken areas`,`printers condition and clean it`,`Test printer`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (date,CPN,CCC,CM,PCC,TP,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)

@app.route('/pump',methods =['POST'])
def pump():    
    date = request.form['date']
    CCES = request.form['CCES']
    ACPC = request.form['ACPC']
    CKP = request.form['CKP']
    SUTP = request.form['SUTP']
    
     
    sig = request.form['sig']
    
    sql = "INSERT INTO PPM_Syringe_Pump (`PPM_Date`,`condition of the external surface`,`AC Power supply and cables`,`case keyboard and plunger`,`start up self test operation`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (date,CCES,ACPC,CKP,SUTP,sig)
    mycursor.execute(sql, val)
    mydb.commit() 
    
    mycursor.execute("SELECT DeviceName, SerialNumber FROM OpenHeart_ICU")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         
         'rec':myresult,
         'header':row_headers
    }
    return render_template('open_heart.html',data=data)




@app.route('/devicesdetailsOP')
def devicesdetailsOP():
    
      mycursor.execute("SELECT * FROM OpenHeart_ICU")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         'message':"Open_Heart ICU department devices",
         'rec':myresult,
         'header':row_headers
      }
      return render_template('detailsOP.html',data=data)
    
    
 #Radiology department code   
    
@app.route('/Radiology')
def Radiology():
    
      mycursor.execute("SELECT DeviceName, SerialNumber FROM Radiology")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         
         'rec':myresult,
         'header':row_headers
      }
      return render_template('radiology.html',data=data)
    
    

@app.route('/devicesdetailsR')
def devicesdetailsR():
    
      mycursor.execute("SELECT * FROM Radiology")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         'message':"Radiology department devices",
         'rec':myresult,
         'header':row_headers
      }
      return render_template('detailsR.html',data=data)
    


@app.route('/makedailyR',methods = ['POST', 'GET'])
def makedailyR():
    if request.method == 'POST':
        date = request.form['date']
        DDP1 = request.form.get('DDP1')
        DDP2 = request.form.get('DDP2')
        DDP3 = request.form.get('DDP3')
        DDP4 = request.form.get('DDP4')
        DDP5 = request.form.get('DDP5')
        DDP6 = request.form.get('DDP6')
        DDP7 = request.form.get('DDP7')
        DDP8 = request.form.get('DDP8')
        DDP9 = request.form['DDP9']
        
        DU1 = request.form.get('DU1')
        DU2 = request.form.get('DU2')
        DU3 = request.form.get('DU3')
        DU4 = request.form.get('DU4')
        DU5 = request.form.get('DU5')
        DU6 = request.form.get('DU6')
        DU7 = request.form['DU7']
        
        XRF1 = request.form.get('XRF1')
        XRF2 = request.form.get('XRF2')
        XRF3 = request.form.get('XRF3')
        XRF4 = request.form.get('XRF4')
        XRF5 = request.form.get('XRF5')
        XRF6 = request.form.get('XRF6')
        XRF7 = request.form.get('XRF7')
        XRF8 = request.form.get('XRF8')
        XRF9 = request.form['XRF9']
        
        BXR1 = request.form.get('BXR1')
        BXR2 = request.form.get('BXR2')
        BXR3 = request.form.get('BXR3')
        BXR4 = request.form.get('BXR4')
        BXR5 = request.form.get('BXR5')
        BXR6 = request.form.get('BXR6')
        BXR7 = request.form.get('BXR7')
        BXR8 = request.form.get('BXR8')
        BXR9 = request.form.get('BXR9')
        BXR10 = request.form.get('BXR10')
        BXR11 = request.form.get('BXR11')
        BXR12 = request.form['BXR12']
        
        DUS1 = request.form.get('DUS1')
        DUS2 = request.form.get('DUS2')
        DUS3 = request.form.get('DUS3')
        DUS4 = request.form.get('DUS4')
        DUS5 = request.form.get('DUS5')
        DUS6 = request.form.get('DUS6')
        DUS7 = request.form.get('DUS7')
        DUS8 = request.form['DUS8']
        
        AM1 = request.form.get('AM1')
        AM2 = request.form.get('AM2')
        AM3 = request.form.get('AM3')
        AM4 = request.form.get('AM4')
        AM5 = request.form.get('AM5')
        AM6 = request.form.get('AM6')
        AM7 = request.form.get('AM7')
        AM8 = request.form.get('AM8')
        AM9 = request.form.get('AM9')
        AM10 = request.form.get('AM10')
        AM11 = request.form['AM11']
        
        MMM1 = request.form.get('MMM1')
        MMM2 = request.form.get('MMM2')
        MMM3 = request.form.get('MMM3')
        MMM4 = request.form.get('MMM4')
        MMM5 = request.form.get('MMM5')
        MMM6 = request.form['MMM6']
        
        MRI1 = request.form.get('MRI1')
        MRI2 = request.form.get('MRI2')
        MRI3 = request.form.get('MRI3')
        MRI4 = request.form.get('MRI4')
        MRI5 = request.form.get('MRI5')
        MRI6 = request.form.get('MRI6')
        MRI7 = request.form['MRI7']
        
        CT1 = request.form.get('CT1')
        CT2 = request.form.get('CT2')
        CT3 = request.form.get('CT3')
        CT4 = request.form['CT4']
        
        sig = request.form['sig']
        
        sql = "INSERT INTO Radiology_DailyI (`DATE`,`Equipment cleaning`,`Damages Or Abnormalities`,`preparation of protection apron` ,`Switches Presetting And Dials`,`Power ON and confirm self test pass`,`X_ray exposure is available on the desired setting`,`Abnormasound vibration or smell`,`Cleaning Of Equipment And Accessories`,`Dental Degital Panorama Comments`,`Cleaning equipment and detector`,`damage or abnormalities`,`Accessories ready to use`,`Switches`,`FHR`,`Cleaning equipment and Accessories After Operation` ,`Doppler Comments`,`Cleaning equipment`,`Remove Racks And Wash It`,`Damages or abnormality`,`Switches maps and dials`,`Power on abnormal sound vibration smell or leak of liquid`,`Temperature`,`sound movement and vibration when feeding test films`,`equipment and accessories cleaning after any operation`,`X_Ray_Film Developer Comments`,`equipment clean`,`damages on cables and unit`,`movement of X_ray tube holder bucky table and bucky stand`,`Locking mechanism`,`movement of collimator`,`switches and dials`,`unit energized After power on`,`value for kVA and mA`,`X_ray exposure`,`sound vibration or smell`,`equipment accessories cleaning after operation`,`Bone X_Ray Comments`,`EquipmentCleaning`,`abnormalities and damages`,`Ultrasound jell`,`switches dials and keyboard`,`Power`,`Operation of the equipment`,`accessories cleaning after operation`,`Diagnostic Ultrasound Comments`,`Machine cleaning`,`Abnormalities`,`accessories`,`CO2 Color`,`flow meters`,`pop off valve switches and knob`,`abnormal sound vibration and gas leak sound`,`flow meter N2O flows`,`alarm sound`,`Accessories Cleaning`,`Anesthesia machine comments`,`equipment clean free of cracks loose parts`,`hoses and cables`,`cleaning solution for the breast`,`Monitor viewing conditions`,`accessories are clean and no damage after any operation`,`Mammography comments`,`free of cracks loose parts clean equipment`,`Monitor system performance`,`Image artifacts`,`abnormal sound`,`Resonance`,`Low contrast detectability`,`MRI Comments`,`Cleaning`,`noise and field Uniformity`,`image quality`,`CT Comments`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (date,DDP1,DDP2,DDP3,DDP4,DDP5,DDP6,DDP7,DDP8,DDP9,DU1,DU2,DU3,DU4,DU5,DU6,DU7,XRF1,XRF2,XRF3,XRF4,XRF5,XRF6,XRF7,XRF8,XRF9,BXR1,BXR2,BXR3,BXR4,BXR5,BXR6,BXR7,BXR8,BXR9,BXR10,BXR11,BXR12,DUS1,DUS2,DUS3,DUS4,DUS5,DUS6,DUS7,DUS8,AM1,AM2,AM3,AM4,AM5,AM6,AM7,AM8,AM9,AM10,AM11,MMM1,MMM2,MMM3,MMM4,MMM5,MMM6,MRI1,MRI2,MRI3,MRI4,MRI5,MRI6,MRI7,CT1,CT2,CT3,CT4,sig)
        mycursor.execute(sql, val)
        mydb.commit() 
        
        mycursor.execute("SELECT DeviceName, SerialNumber FROM Radiology")
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        myresult = mycursor.fetchall()
        data={
         
         'rec':myresult,
         'header':row_headers
        }
        return render_template('radiology.html',data=data)
        
        
        
    else:
        return render_template('radiology_report.html')
    
    
@app.route('/dailyreportdepartment')
def dailyreportdepartment():
    
    mycursor.execute("SELECT `DATE`,`Equipment cleaning`,`Damages Or Abnormalities`,`preparation of protection apron`,`Switches Presetting And Dials`,`Power ON and confirm self test pass`,`X_ray exposure is available on the desired setting`,`Abnormasound vibration or smell`,`Cleaning Of Equipment And Accessories`,`Dental Degital Panorama Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data1={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Cleaning equipment and detector`,`damage or abnormalities`,`Accessories ready to use`,`Switches`,`FHR`,`Cleaning equipment and Accessories After Operation`,`Doppler Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data2={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Cleaning equipment`,`Remove Racks And Wash It`,`Damages or abnormality`,`Switches maps and dials`,`Power on abnormal sound vibration smell or leak of liquid`,`Temperature`,`sound movement and vibration when feeding test films`,`equipment and accessories cleaning after any operation`,`X_Ray_Film Developer Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data3={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`equipment clean`,`damages on cables and unit`,`movement of X_ray tube holder bucky table and bucky stand`,`Locking mechanism`,`movement of collimator`,`switches and dials`,`unit energized After power on`,`value for kVA and mA`,`X_ray exposure`,`sound vibration or smell`,`equipment accessories cleaning after operation`,`Bone X_Ray Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data4={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`EquipmentCleaning`,`abnormalities and damages`,`Ultrasound jell`,`switches dials and keyboard`,`Power`,`Operation of the equipment`,`accessories cleaning after operation`,`Diagnostic Ultrasound Comments`,`Signature`FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data5={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Machine cleaning`,`Abnormalities`,`accessories`,`CO2 Color`,`flow meters`,`pop off valve switches and knob`,`abnormal sound vibration and gas leak sound`,`flow meter N2O flows`,`alarm sound`,`Accessories Cleaning`,`Anesthesia machine comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data6={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`equipment clean free of cracks loose parts`,`hoses and cables`,`cleaning solution for the breast`,`Monitor viewing conditions`,`accessories are clean and no damage after any operation`,`Mammography comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data7={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`free of cracks loose parts clean equipment`,`Monitor system performance`,`Image artifacts`,`abnormal sound`,`Resonance`,`Low contrast detectability`,`MRI Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data8={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Cleaning`,`noise and field Uniformity`,`image quality`,`CT Comments`,`Signature` FROM Radiology_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data9={
         
         'rec':myresult,
         'header':row_headers
    }
    
    
    return render_template('total_rad_report.html',data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9)

    
    
@app.route('/dailyreportdevice',methods =['POST'])
def dailyreportdevice():
    serial = request.form['serial']
    if serial == '49635':
        mycursor.execute("SELECT `DATE`,`Equipment cleaning`,`Damages Or Abnormalities`,`preparation of protection apron`,`Switches Presetting And Dials`,`Power ON and confirm self test pass`,`X_ray exposure is available on the desired setting`,`Abnormasound vibration or smell`,`Cleaning Of Equipment And Accessories`,`Dental Degital Panorama Comments`,`Signature` FROM Radiology_DailyI")
        mes='Dental digital panorama report'
    elif serial == 'USD15D0281':
        mycursor.execute("SELECT `DATE`,`Cleaning equipment and detector`,`damage or abnormalities`,`Accessories ready to use`,`Switches`,`FHR`,`Cleaning equipment and Accessories After Operation`,`Doppler Comments`,`Signature` FROM Radiology_DailyI")
        mes='Doppler Ultrasound'
    elif serial == '66723822':
        mycursor.execute("SELECT `DATE`,`Cleaning equipment`,`Remove Racks And Wash It`,`Damages or abnormality`,`Switches maps and dials`,`Power on abnormal sound vibration smell or leak of liquid`,`Temperature`,`sound movement and vibration when feeding test films`,`equipment and accessories cleaning after any operation`,`X_Ray_Film Developer Comments`,`Signature` FROM Radiology_DailyI")
        mes='Automatic X-RAY Film Developer Report'
    elif serial == '69690':
         mycursor.execute("SELECT `DATE`,`equipment clean`,`damages on cables and unit`,`movement of X_ray tube holder bucky table and bucky stand`,`Locking mechanism`,`movement of collimator`,`switches and dials`,`unit energized After power on`,`value for kVA and mA`,`X_ray exposure`,`sound vibration or smell`,`equipment accessories cleaning after operation`,`Bone X_Ray Comments`,`Signature` FROM Radiology_DailyI")
         mes='Bone X-RAY Report'
    elif serial == '500047SU7':
         mycursor.execute("SELECT `DATE`,`EquipmentCleaning`,`abnormalities and damages`,`Ultrasound jell`,`switches dials and keyboard`,`Power`,`Operation of the equipment`,`accessories cleaning after operation`,`Diagnostic Ultrasound Comments`,`Signature`FROM Radiology_DailyI")
         mes='Diagnostic Ultrasound'
    elif serial == 'MRI505087191':
         mycursor.execute("SELECT `DATE`,`Machine cleaning`,`Abnormalities`,`accessories`,`CO2 Color`,`flow meters`,`pop off valve switches and knob`,`abnormal sound vibration and gas leak sound`,`flow meter N2O flows`,`alarm sound`,`Accessories Cleaning`,`Anesthesia machine comments`,`Signature` FROM Radiology_DailyI")
         mes='Anesthesia machine report'
    elif serial == '12220':
         mycursor.execute("SELECT `DATE`,`equipment clean free of cracks loose parts`,`hoses and cables`,`cleaning solution for the breast`,`Monitor viewing conditions`,`accessories are clean and no damage after any operation`,`Mammography comments`,`Signature` FROM Radiology_DailyI")
         mes='Mammography Report'
    elif serial == '781396':
         mycursor.execute("SELECT `DATE`,`free of cracks loose parts clean equipment`,`Monitor system performance`,`Image artifacts`,`abnormal sound`,`Resonance`,`Low contrast detectability`,`MRI Comments`,`Signature` FROM Radiology_DailyI")
         mes='MRI Report'
    elif serial == '6AA1242056':
         mycursor.execute("SELECT `DATE`,`Cleaning`,`noise and field Uniformity`,`image quality`,`CT Comments`,`Signature` FROM Radiology_DailyI")
         mes='CT Scan Report'
    elif serial == '301201261310':
         
         mes='NO Report For Dye Injector'
         return render_template('error2.html',message=mes)
    elif serial == '96525518':
         
         mes='NO Report For FCR'
         return render_template('error2.html',message=mes)
        
    elif serial == '451220202201':
         
         mes='NO Report For Diagnostic X-Ray'
         return render_template('error2.html',message=mes)
    else:
        mes="No matching device ...."
        return render_template('error2.html',message=mes)
    
    
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         'message':mes,
         'rec':myresult,
         'header':row_headers
    }
    return render_template('dailydevicereport.html',data=data)
    
       

#catheter department code   
    
@app.route('/catheters')
def catheters():
    
      mycursor.execute("SELECT DeviceName, SerialNumber FROM Catheter")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         
         'rec':myresult,
         'header':row_headers
      }
      return render_template('catheter.html',data=data)
    
    

@app.route('/devicesdetailsC')
def devicesdetailsC():
    
      mycursor.execute("SELECT * FROM catheter")
      row_headers=[x[0] for x in mycursor.description] #this will extract row headers
      myresult = mycursor.fetchall()
      data={
         'message':"Radiology department devices",
         'rec':myresult,
         'header':row_headers
      }
      return render_template('catheter_devices_details.html',data=data)
 
@app.route('/makedailyReport',methods = ['POST', 'GET'])
def makedailyReport():
    if request.method == 'POST':
        
        date = request.form['date']
        SM1 = request.form.get('SM1')
        SM2 = request.form.get('SM2')
        SM3 = request.form.get('SM3')
        SM4 = request.form.get('SM4')
        SM5 = request.form.get('SM5')
        SM6 = request.form['SM6']
        
        ECG1 = request.form.get('ECG1')
        ECG2 = request.form.get('ECG2')
        ECG3 = request.form.get('ECG3')
        ECG4 = request.form.get('ECG4')
        ECG5 = request.form.get('ECG5')
        ECG6 = request.form.get('ECG6')
        ECG7 = request.form['ECG7']
        
        OT1 = request.form.get('OT1')
        OT2 = request.form.get('OT2')
        OT3 = request.form.get('OT3') 
        OT4 = request.form.get('OT4')
        OT5 = request.form.get('OT5')
        OT6 = request.form.get('OT6')
        OT7 = request.form['OT7']
        
        CUS1 = request.form.get('CUS1')
        CUS2 = request.form.get('CUS2')
        CUS3 = request.form.get('CUS3')
        CUS4 = request.form.get('CUS4')
        CUS5 = request.form.get('CUS5')
        CUS6 = request.form['CUS6']
        
        MO1 = request.form.get('MO1')
        MO2 = request.form.get('MO2')
        MO3 = request.form.get('MO3')
        MO4 = request.form.get('MO4')
        MO5 = request.form.get('MO5')
        MO6 = request.form.get('MO6')
        MO7 = request.form.get('MO7')
        MO8 = request.form.get('MO8')
        MO9 = request.form['MO9']
        
        AM1 = request.form.get('AM1')
        AM2 = request.form.get('AM2')
        AM3 = request.form.get('AM3')
        AM4 = request.form.get('AM4')
        AM5 = request.form.get('AM5')
        AM6 = request.form.get('AM6')
        AM7 = request.form.get('AM7')
        AM8 = request.form.get('AM8')
        AM9 = request.form.get('AM9')
        AM10 = request.form.get('AM10')
        AM11 = request.form['AM11']
        
        SL1 = request.form.get('SL1')
        SL2 = request.form.get('SL2')
        SL3 = request.form.get('SL3')
        SL4 = request.form.get('SL4')
        SL5 = request.form['SL5']
        
        DT1 = request.form.get('DT1')
        DT2 = request.form.get('DT2')
        DT3 = request.form.get('DT3')
        DT4 = request.form.get('DT4')
        DT5 = request.form.get('DT5')
        DT6 = request.form.get('DT6')
        DT7 = request.form['DT7']
        
        UT1 = request.form.get('UT1')
        UT2 = request.form.get('UT2')
        UT3 = request.form.get('UT3')
        UT4 = request.form.get('UT4')
        UT5 = request.form.get('UT5')
        UT6 = request.form.get('UT6')
        UT7 = request.form['UT7']
        
        DF1 = request.form.get('DF1')
        DF2 = request.form.get('DF2')
        DF3 = request.form.get('DF3')
        DF4 = request.form.get('DF4')
        DF5 = request.form.get('DF5')
        DF6 = request.form.get('DF6')
        DF7 = request.form.get('DF7')
        DF8 = request.form['DF8']
 
        sig = request.form['sig']
        
        sql = "INSERT INTO catheter_DailyI (`DATE`,`Equipment cleaning`,`Wash bottle And patient tubing`,`Fittings and accessories`,`filter cleaning`,`Run abrief function check before clinic`,`Suction Machine Comments`,`Cleaning Of Equipment`,`battery and power indicators`,`Patient cable connector indicator`,`baseline of the ECG recording`,`calibration of machine before use`,`Clearness of printing`,`ECG comments`,`Clean dry and disinfect all parts`,`Remove all paper tape and foreign matter`,`Existence of all parts`,`Replace mattress if worn or damaged`,`no oil is leaking from hydraulics`,`essential movements before use`,`Operating Table comments`,`device cleaning`,`Remove any tape paper or foreign body`,`all parts are present and connected`,`Check cables`,`Switch on power`,`Cardiology Ultrasound comments`,`Cleaning Equipment`,`damages or abnormalities on main unit switches connections`,`damages in Patient cable`,`All parts are ready to use`,`Power`,`Operation of the equipment is normal`,`abnormal sound or vibration when operated`,`ECG wave heart rate SpO2`,`Monitor comments`,`EquipmentCleaning`,`Damages or abnormalities`,`any leak is audible with soapy solution`,`Replacement of CO2 absorbent if its color has changed`,`Verify smooth control of flow meters adial of vaporizer`,`Verify smooth control of apop off valve switches knob`,`all seals connectors adapters and parts are tight`,`Verify flow meter`,`alarm sound`,`system is depressurized and all caps are replaced`,`Anesthesia comments`,`equipment clean and free of dust`,`Fitting And accessories`,`cracks in glass or liquid spillages`,`Run brief function check before clinic`,`Surgical light comments`,`equipment Clean`,`abnormalities`,`accessories ready to use`,`switches dials and screws`,`Connection of hand piece`,`sound or vibration`,`Diathermy comments`,`free of cracks and cleaning`,`Damage`,`Ultrasound jell`,`switches dials and keyboard`,`Power on and confirm self test pass`,`Operation`,`Ultrasound comments`,`cleaning`,`Damages`,`power sources AC and battery`,`Recycle damaged or leaking battery`,`cracks in ECG cables`,`Replace electrodes if date pass`,`observe illumination of self test message and LEDs`,`Difibrillator comments`,`Signature`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date,SM1,SM2,SM3,SM4,SM5,SM6,ECG1,ECG2,ECG3,ECG4,ECG5,ECG6,ECG7,OT1,OT2,OT3,OT4,OT5,OT6,OT7,CUS1,CUS2,CUS3,CUS4,CUS5,CUS6,MO1,MO2,MO3,MO4,MO5,MO6,MO7,MO8,MO9,AM1,AM2,AM3,AM4,AM5,AM6,AM7,AM8,AM9,AM10,AM11,SL1,SL2,SL3,SL4,SL5,DT1,DT2,DT3,DT4,DT5,DT6,DT7,UT1,UT2,UT3,UT4,UT5,UT6,UT7,DF1,DF2,DF3,DF4,DF5,DF6,DF7,DF8,sig)
        mycursor.execute(sql, val)
        mydb.commit() 
        
        mycursor.execute("SELECT DeviceName, SerialNumber FROM Catheter")
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        myresult = mycursor.fetchall()
        data={
         
         'rec':myresult,
         'header':row_headers
        }
        return render_template('catheter.html',data=data)
        
 
    else:
        return render_template('catheter_report.html')
    
    
  
@app.route('/dailyreportdepartmentC')
def dailyreportdepartmentC():
    
    mycursor.execute("SELECT `DATE`,`Equipment cleaning`,`Wash bottle And patient tubing`,`Fittings and accessories`,`filter cleaning`,`Run abrief function check before clinic`,`Suction Machine Comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data1={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Cleaning Of Equipment`,`battery and power indicators`,`Patient cable connector indicator`,`baseline of the ECG recording`,`calibration of machine before use`,`Clearness of printing`,`ECG comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data2={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Clean dry and disinfect all parts`,`Remove all paper tape and foreign matter`,`Existence of all parts`,`Replace mattress if worn or damaged`,`no oil is leaking from hydraulics`,`essential movements before use`,`Operating Table comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data3={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`device cleaning`,`Remove any tape paper or foreign body`,`all parts are present and connected`,`Check cables`,`Switch on power`,`Cardiology Ultrasound comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data4={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`Cleaning Equipment`,`damages or abnormalities on main unit switches connections`,`damages in Patient cable`,`All parts are ready to use`,`Power`,`Operation of the equipment is normal`,`abnormal sound or vibration when operated`,`ECG wave heart rate SpO2`,`Monitor comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data5={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`EquipmentCleaning`,`Damages or abnormalities`,`any leak is audible with soapy solution`,`Replacement of CO2 absorbent if its color has changed`,`Verify smooth control of flow meters adial of vaporizer`,`Verify smooth control of apop off valve switches knob`,`all seals connectors adapters and parts are tight`,`Verify flow meter`,`alarm sound`,`system is depressurized and all caps are replaced`,`Anesthesia comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data6={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`equipment clean and free of dust`,`Fitting And accessories`,`cracks in glass or liquid spillages`,`Run brief function check before clinic`,`Surgical light comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data7={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`equipment Clean`,`abnormalities`,`accessories ready to use`,`switches dials and screws`,`Connection of hand piece`,`sound or vibration`,`Diathermy comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data8={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`free of cracks and cleaning`,`Damage`,`Ultrasound jell`,`switches dials and keyboard`,`Power on and confirm self test pass`,`Operation`,`Ultrasound comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data9={
         
         'rec':myresult,
         'header':row_headers
    }
    
    mycursor.execute("SELECT `DATE`,`cleaning`,`Damages`,`power sources AC and battery`,`Recycle damaged or leaking battery`,`cracks in ECG cables`,`Replace electrodes if date pass`,`observe illumination of self test message and LEDs`,`Difibrillator comments`,`Signature` FROM catheter_DailyI")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data10={
         
         'rec':myresult,
         'header':row_headers
    }
    
    
    return render_template('total_catheter_report.html',data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9,data10=data10)
    


@app.route('/dailyreportdevicecatheter',methods =['POST'])
def dailyreportdevicecatheter():
    serial = request.form['serial']
    if serial == '001091':
        mycursor.execute("SELECT `DATE`,`Equipment cleaning`,`Wash bottle And patient tubing`,`Fittings and accessories`,`filter cleaning`,`Run abrief function check before clinic`,`Suction Machine Comments`,`Signature` FROM catheter_DailyI")
        mes='Suction Machine Report'
    elif serial == '2013-3-22':
        mycursor.execute("SELECT `DATE`,`Cleaning Of Equipment`,`battery and power indicators`,`Patient cable connector indicator`,`baseline of the ECG recording`,`calibration of machine before use`,`Clearness of printing`,`ECG comments`,`Signature` FROM catheter_DailyI")
        mes='ECG Report'
    elif serial == '03650':
        mycursor.execute("SELECT `DATE`,`Clean dry and disinfect all parts`,`Remove all paper tape and foreign matter`,`Existence of all parts`,`Replace mattress if worn or damaged`,`no oil is leaking from hydraulics`,`essential movements before use`,`Operating Table comments`,`Signature` FROM catheter_DailyI")
        mes='Operating Table Report'
    elif serial == '141066':
         mycursor.execute("SELECT `DATE`,`device cleaning`,`Remove any tape paper or foreign body`,`all parts are present and connected`,`Check cables`,`Switch on power`,`Cardiology Ultrasound comments`,`Signature` FROM catheter_DailyI")
         mes='Cardiology Ultrasound System Report'
    elif serial == '74261-3A5-0A5S':
         mycursor.execute("SELECT `DATE`,`Cleaning Equipment`,`damages or abnormalities on main unit switches connections`,`damages in Patient cable`,`All parts are ready to use`,`Power`,`Operation of the equipment is normal`,`abnormal sound or vibration when operated`,`ECG wave heart rate SpO2`,`Monitor comments`,`Signature` FROM catheter_DailyI")
         mes='Monitor Report'
    elif serial == 'APKU02673':
         mycursor.execute("SELECT `DATE`,`EquipmentCleaning`,`Damages or abnormalities`,`any leak is audible with soapy solution`,`Replacement of CO2 absorbent if its color has changed`,`Verify smooth control of flow meters adial of vaporizer`,`Verify smooth control of apop off valve switches knob`,`all seals connectors adapters and parts are tight`,`Verify flow meter`,`alarm sound`,`system is depressurized and all caps are replaced`,`Anesthesia comments`,`Signature` FROM catheter_DailyI")
         mes='Anesthesia machine report'
    elif serial == '102226880':
         mycursor.execute("SELECT `DATE`,`equipment clean and free of dust`,`Fitting And accessories`,`cracks in glass or liquid spillages`,`Run brief function check before clinic`,`Surgical light comments`,`Signature` FROM catheter_DailyI")
         mes='Surgical light Report'
    elif serial == '11378619':
         mycursor.execute("SELECT `DATE`,`equipment Clean`,`abnormalities`,`accessories ready to use`,`switches dials and screws`,`Connection of hand piece`,`sound or vibration`,`Diathermy comments`,`Signature` FROM catheter_DailyI")
         mes='Diathermy Report'
    elif serial == '4874':
         mycursor.execute("SELECT `DATE`,`free of cracks and cleaning`,`Damage`,`Ultrasound jell`,`switches dials and keyboard`,`Power on and confirm self test pass`,`Operation`,`Ultrasound comments`,`Signature` FROM catheter_DailyI")
         mes='Ultrasound Report'
    elif serial == 'US41412124':
         mycursor.execute("SELECT `DATE`,`cleaning`,`Damages`,`power sources AC and battery`,`Recycle damaged or leaking battery`,`cracks in ECG cables`,`Replace electrodes if date pass`,`observe illumination of self test message and LEDs`,`Difibrillator comments`,`Signature` FROM catheter_DailyI")
         mes='DC shock Report'
    
         
         
    else:
        mes="No matching device ...."
        return render_template('error3.html',message=mes)
    
    
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data={
         'message':mes,
         'rec':myresult,
         'header':row_headers
    }
    return render_template('catheter_device_report.html',data=data)
    
if __name__ == '__main__':
   app.run(debug=True)