-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 09:00 PM
-- Server version: 5.6.37
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinicaldatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `Catheter`
--

CREATE TABLE IF NOT EXISTS `Catheter` (
  `Department` varchar(255) DEFAULT NULL,
  `DeviceName` varchar(255) DEFAULT NULL,
  `Brand` varchar(255) DEFAULT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `SerialNumber` varchar(255) NOT NULL,
  `CountryOfOrigin` varchar(255) DEFAULT NULL,
  `InstallationDate` date DEFAULT NULL,
  `SupplyingDate` date DEFAULT NULL,
  `WarrantyPeriod` int(11) DEFAULT NULL,
  `CompanyName` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Catheter`
--

INSERT INTO `Catheter` (`Department`, `DeviceName`, `Brand`, `Model`, `SerialNumber`, `CountryOfOrigin`, `InstallationDate`, `SupplyingDate`, `WarrantyPeriod`, `CompanyName`) VALUES
('Catheter', 'Suction Machine', 'ATMOS', 'C 451', '001091', '', '2016-02-08', '2016-02-08', 2, ''),
('Catheter', 'Operating Table', 'Philips', 'GEO MODULE TILT WP', '03650', '', '2016-02-08', '2016-02-08', 2, ''),
('Catheter', 'Surgical light', 'Tramph', 'TruLight 5500', '102226880', 'Germany', '2016-02-08', '2016-02-08', 2, 'Egyptian group'),
('Catheter', 'Diathermy', 'RB', 'VIO300D', '11378619', 'UK', '2016-02-08', '2016-02-08', 2, 'Egyptian group'),
('Catheter', 'Cardiology Ultrasound System', 'Philips', '000047', '141066', 'Germany', '2016-02-08', '2016-02-08', 2, ''),
('Catheter', 'Ecg', 'Cardio Tek', 'EP-TRACER 70', '2013-3-22', 'New Zealand', '2016-02-08', '2016-02-08', 2, ''),
('Catheter', 'doppler ultrasound', 'Philips', 'Esterlne', '4874', 'USA', '2016-02-08', '2016-02-08', 2, ''),
('Catheter', 'Monitor', 'Dell', 'Dell', '74261-3A5-0A5S', 'China', '2016-02-08', '2016-02-08', 2, 'Al Alamia Group'),
('Catheter', 'Anesthesia machine', 'GE', 'Avance CS2', 'APKU02673', 'USA', '2016-02-08', '2016-02-08', 2, 'General electric'),
('Catheter', 'DC shock', 'Philips', 'HEART START XL ', 'US41412124', 'Switzerland', '2016-02-08', '2016-02-08', 2, 'Egyptian group');

-- --------------------------------------------------------

--
-- Table structure for table `catheter_DailyI`
--

CREATE TABLE IF NOT EXISTS `catheter_DailyI` (
  `DATE` date NOT NULL DEFAULT '0000-00-00',
  `Equipment cleaning` varchar(255) DEFAULT NULL,
  `Wash bottle And patient tubing` varchar(255) DEFAULT NULL,
  `Fittings and accessories` varchar(255) DEFAULT NULL,
  `filter cleaning` varchar(255) DEFAULT NULL,
  `Run abrief function check before clinic` varchar(255) DEFAULT NULL,
  `Suction Machine Comments` varchar(255) DEFAULT NULL,
  `Cleaning Of Equipment` varchar(255) DEFAULT NULL,
  `battery and power indicators` varchar(255) DEFAULT NULL,
  `Patient cable connector indicator` varchar(255) DEFAULT NULL,
  `baseline of the ECG recording` varchar(255) DEFAULT NULL,
  `calibration of machine before use` varchar(255) DEFAULT NULL,
  `Clearness of printing` varchar(255) DEFAULT NULL,
  `ECG comments` varchar(255) DEFAULT NULL,
  `Clean dry and disinfect all parts` varchar(255) DEFAULT NULL,
  `Remove all paper tape and foreign matter` varchar(255) DEFAULT NULL,
  `Existence of all parts` varchar(255) DEFAULT NULL,
  `Replace mattress if worn or damaged` varchar(255) DEFAULT NULL,
  `no oil is leaking from hydraulics` varchar(255) DEFAULT NULL,
  `essential movements before use` varchar(255) DEFAULT NULL,
  `Operating Table comments` varchar(255) DEFAULT NULL,
  `device cleaning` varchar(255) DEFAULT NULL,
  `Remove any tape paper or foreign body` varchar(255) DEFAULT NULL,
  `all parts are present and connected` varchar(255) DEFAULT NULL,
  `Check cables` varchar(255) DEFAULT NULL,
  `Switch on power` varchar(255) DEFAULT NULL,
  `Cardiology Ultrasound comments` varchar(255) DEFAULT NULL,
  `Cleaning Equipment` varchar(255) DEFAULT NULL,
  `damages or abnormalities on main unit switches connections` varchar(255) DEFAULT NULL,
  `damages in Patient cable` varchar(255) DEFAULT NULL,
  `All parts are ready to use` varchar(255) DEFAULT NULL,
  `Power` varchar(255) DEFAULT NULL,
  `Operation of the equipment is normal` varchar(255) DEFAULT NULL,
  `abnormal sound or vibration when operated` varchar(255) DEFAULT NULL,
  `ECG wave heart rate SpO2` varchar(255) DEFAULT NULL,
  `Monitor comments` varchar(255) DEFAULT NULL,
  `EquipmentCleaning` varchar(255) DEFAULT NULL,
  `Damages or abnormalities` varchar(255) DEFAULT NULL,
  `any leak is audible with soapy solution` varchar(255) DEFAULT NULL,
  `Replacement of CO2 absorbent if its color has changed` varchar(255) DEFAULT NULL,
  `Verify smooth control of flow meters adial of vaporizer` varchar(255) DEFAULT NULL,
  `Verify smooth control of apop off valve switches knob` varchar(255) DEFAULT NULL,
  `all seals connectors adapters and parts are tight` varchar(255) DEFAULT NULL,
  `Verify flow meter` varchar(255) DEFAULT NULL,
  `alarm sound` varchar(255) DEFAULT NULL,
  `system is depressurized and all caps are replaced` varchar(255) DEFAULT NULL,
  `Anesthesia comments` varchar(255) DEFAULT NULL,
  `equipment clean and free of dust` varchar(255) DEFAULT NULL,
  `Fitting And accessories` varchar(255) DEFAULT NULL,
  `cracks in glass or liquid spillages` varchar(255) DEFAULT NULL,
  `Run brief function check before clinic` varchar(255) DEFAULT NULL,
  `Surgical light comments` varchar(255) DEFAULT NULL,
  `equipment Clean` varchar(255) DEFAULT NULL,
  `abnormalities` varchar(255) DEFAULT NULL,
  `accessories ready to use` varchar(255) DEFAULT NULL,
  `switches dials and screws` varchar(255) DEFAULT NULL,
  `Connection of hand piece` varchar(255) DEFAULT NULL,
  `sound or vibration` varchar(255) DEFAULT NULL,
  `Diathermy comments` varchar(255) DEFAULT NULL,
  `free of cracks and cleaning` varchar(255) DEFAULT NULL,
  `Damage` varchar(255) DEFAULT NULL,
  `Ultrasound jell` varchar(255) DEFAULT NULL,
  `switches dials and keyboard` varchar(255) DEFAULT NULL,
  `Power on and confirm self test pass` varchar(255) DEFAULT NULL,
  `Operation` varchar(255) DEFAULT NULL,
  `Ultrasound comments` varchar(255) DEFAULT NULL,
  `cleaning` varchar(255) DEFAULT NULL,
  `Damages` varchar(255) DEFAULT NULL,
  `power sources AC and battery` varchar(255) DEFAULT NULL,
  `Recycle damaged or leaking battery` varchar(255) DEFAULT NULL,
  `cracks in ECG cables` varchar(255) DEFAULT NULL,
  `Replace electrodes if date pass` varchar(255) DEFAULT NULL,
  `observe illumination of self test message and LEDs` varchar(255) DEFAULT NULL,
  `Difibrillator comments` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `catheter_DailyI`
--

INSERT INTO `catheter_DailyI` (`DATE`, `Equipment cleaning`, `Wash bottle And patient tubing`, `Fittings and accessories`, `filter cleaning`, `Run abrief function check before clinic`, `Suction Machine Comments`, `Cleaning Of Equipment`, `battery and power indicators`, `Patient cable connector indicator`, `baseline of the ECG recording`, `calibration of machine before use`, `Clearness of printing`, `ECG comments`, `Clean dry and disinfect all parts`, `Remove all paper tape and foreign matter`, `Existence of all parts`, `Replace mattress if worn or damaged`, `no oil is leaking from hydraulics`, `essential movements before use`, `Operating Table comments`, `device cleaning`, `Remove any tape paper or foreign body`, `all parts are present and connected`, `Check cables`, `Switch on power`, `Cardiology Ultrasound comments`, `Cleaning Equipment`, `damages or abnormalities on main unit switches connections`, `damages in Patient cable`, `All parts are ready to use`, `Power`, `Operation of the equipment is normal`, `abnormal sound or vibration when operated`, `ECG wave heart rate SpO2`, `Monitor comments`, `EquipmentCleaning`, `Damages or abnormalities`, `any leak is audible with soapy solution`, `Replacement of CO2 absorbent if its color has changed`, `Verify smooth control of flow meters adial of vaporizer`, `Verify smooth control of apop off valve switches knob`, `all seals connectors adapters and parts are tight`, `Verify flow meter`, `alarm sound`, `system is depressurized and all caps are replaced`, `Anesthesia comments`, `equipment clean and free of dust`, `Fitting And accessories`, `cracks in glass or liquid spillages`, `Run brief function check before clinic`, `Surgical light comments`, `equipment Clean`, `abnormalities`, `accessories ready to use`, `switches dials and screws`, `Connection of hand piece`, `sound or vibration`, `Diathermy comments`, `free of cracks and cleaning`, `Damage`, `Ultrasound jell`, `switches dials and keyboard`, `Power on and confirm self test pass`, `Operation`, `Ultrasound comments`, `cleaning`, `Damages`, `power sources AC and battery`, `Recycle damaged or leaking battery`, `cracks in ECG cables`, `Replace electrodes if date pass`, `observe illumination of self test message and LEDs`, `Difibrillator comments`, `Signature`) VALUES
('2020-05-20', 'checked', 'checked', 'checked', 'checked', 'checked', 'checked', NULL, NULL, NULL, NULL, NULL, NULL, 'checked', NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `OpenHeart_ICU`
--

CREATE TABLE IF NOT EXISTS `OpenHeart_ICU` (
  `Department` varchar(255) DEFAULT NULL,
  `DeviceName` varchar(255) DEFAULT NULL,
  `Brand` varchar(255) DEFAULT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `SerialNumber` varchar(255) NOT NULL,
  `CountryOfOrigin` varchar(255) DEFAULT NULL,
  `InstallationDate` date DEFAULT NULL,
  `WarrantyPeriod` int(11) DEFAULT NULL,
  `CompanyName` varchar(255) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `OpenHeart_ICU`
--

INSERT INTO `OpenHeart_ICU` (`Department`, `DeviceName`, `Brand`, `Model`, `SerialNumber`, `CountryOfOrigin`, `InstallationDate`, `WarrantyPeriod`, `CompanyName`, `Price`) VALUES
('open_heart_ICU', 'ECG', 'Schiller', 'Cardio vit AT-102 ', '070-12242', 'Swizerland', '2016-08-02', 2, 'Glionji Trading', 19950),
('open_heart_ICU', 'Syringe Pump', 'Care fusion Alaris', 'Plus GH', '135224798', ' England', '2016-08-02', 2, 'Jessica', 7800),
('open_heart_ICU', 'Physiological Monitor System', 'Space labs ', 'Ultraview SL 2700', '1387-111678', 'USA', '2016-08-02', 2, 'Jessica', 53800),
('open_heart_ICU', 'Suction_Unit', '3A HEALTHCARE', 'MaxiA speed 6.4p', '182447', 'italy', '2016-08-02', 2, 'Alflwa for Trade', 6290),
('open_heart_ICU', 'ECG_Ultrasound', 'GE', 'Vivid s5', 'FN000060', 'Norway', '2016-08-02', 2, 'Glionge', 1300000),
('open_heart_ICU', 'Exercise ECG', 'Philips', 'Stress vue', 'Fv-12133', 'USA', '2016-02-08', 2, 'Egyptian group for medical equipment', 140000),
('open_heart_ICU', 'mobile_X-Ray', 'smam', 'ROLLER 30', 'T8135', ' Italy', '2015-08-01', 2, 'Fumdco', 20000),
('open_heart_ICU', 'Mobile_Ventilator', 'Philips RESPIRONICS', 'Trigology 202', 'TV01405054F', 'USA', '2016-02-08', 2, 'Servomed', 85000),
('open_heart_ICU', 'Defibrillator', 'Philips', 'HEARTSTART XL', 'US71514674', 'USA', '2016-08-02', 2, 'Egyption group for import and export', 44500),
('open_heart_ICU', 'Measure_Proportion_of_blood_gas', 'Gem ', ' Premier 4000', ' 14037475', 'USA', '2016-02-08', 2, 'International_medical_equipment_company', 63250);

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Defibrillator`
--

CREATE TABLE IF NOT EXISTS `PPM_Defibrillator` (
  `PPM_Date` date NOT NULL,
  `Check the shock powered by AC only` varchar(255) DEFAULT NULL,
  `Check the shock powered by battery only` varchar(255) DEFAULT NULL,
  `Check disarm while pressing disarm key` varchar(255) DEFAULT NULL,
  `Check analyzer readings after delivering 200J shock` varchar(255) DEFAULT NULL,
  `Check printed strip` varchar(255) DEFAULT NULL,
  `Repeat the test using paddles` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Defibrillator`
--

INSERT INTO `PPM_Defibrillator` (`PPM_Date`, `Check the shock powered by AC only`, `Check the shock powered by battery only`, `Check disarm while pressing disarm key`, `Check analyzer readings after delivering 200J shock`, `Check printed strip`, `Repeat the test using paddles`, `Signature`) VALUES
('2020-05-20', 'done', 'done', 'done', 'done', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_ECG`
--

CREATE TABLE IF NOT EXISTS `PPM_ECG` (
  `PPM_Date` date NOT NULL,
  `Power` varchar(255) DEFAULT NULL,
  `LCD main menu` varchar(255) DEFAULT NULL,
  `ECG Room` varchar(255) DEFAULT NULL,
  `Adequate supplies` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_ECG`
--

INSERT INTO `PPM_ECG` (`PPM_Date`, `Power`, `LCD main menu`, `ECG Room`, `Adequate supplies`, `Signature`) VALUES
('2020-01-30', 'functioned well', 'done', 'done', 'all are srocked', 'ES');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_ECG_Ultrasound`
--

CREATE TABLE IF NOT EXISTS `PPM_ECG_Ultrasound` (
  `PPM_Date` date NOT NULL,
  `Visual inspection` varchar(255) DEFAULT NULL,
  `System diagnostic` varchar(255) DEFAULT NULL,
  `System cleaning` varchar(255) DEFAULT NULL,
  `system disassembly` varchar(255) DEFAULT NULL,
  `System reassembly` varchar(255) DEFAULT NULL,
  `Diagnostic imaging` varchar(255) DEFAULT NULL,
  `Fall pass criteria` varchar(255) DEFAULT NULL,
  `Leakage testing` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_ECG_Ultrasound`
--

INSERT INTO `PPM_ECG_Ultrasound` (`PPM_Date`, `Visual inspection`, `System diagnostic`, `System cleaning`, `system disassembly`, `System reassembly`, `Diagnostic imaging`, `Fall pass criteria`, `Leakage testing`, `Signature`) VALUES
('2020-01-30', 'all is well', 'function well', 'all is clean', 'done', 'done ', 'function well', 'all is well', 'no leakage', 'AE');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Exercise_ECG`
--

CREATE TABLE IF NOT EXISTS `PPM_Exercise_ECG` (
  `PPM_Date` date NOT NULL,
  `power and cables` varchar(255) DEFAULT NULL,
  `Cords and connectors` varchar(255) DEFAULT NULL,
  `missing screws cracks or broken areas` varchar(255) DEFAULT NULL,
  `printers condition and clean it` varchar(255) DEFAULT NULL,
  `Test printer` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Exercise_ECG`
--

INSERT INTO `PPM_Exercise_ECG` (`PPM_Date`, `power and cables`, `Cords and connectors`, `missing screws cracks or broken areas`, `printers condition and clean it`, `Test printer`, `Signature`) VALUES
('2020-01-01', 'free of cracks', 'well tight', 'no missing screws or any cracks', 'done', 'functioned well', 'AB');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Measure_blood_gas`
--

CREATE TABLE IF NOT EXISTS `PPM_Measure_blood_gas` (
  `PPM_Date` date NOT NULL,
  `Analyzer performance` varchar(255) DEFAULT NULL,
  `Electronic hardware performance` varchar(255) DEFAULT NULL,
  `Soft ware performance` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Measure_blood_gas`
--

INSERT INTO `PPM_Measure_blood_gas` (`PPM_Date`, `Analyzer performance`, `Electronic hardware performance`, `Soft ware performance`, `Signature`) VALUES
('2020-01-01', 'perform well', 'all performs well', 'perform well', 'AB');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Mobile_X_ray`
--

CREATE TABLE IF NOT EXISTS `PPM_Mobile_X_ray` (
  `PPM_Date` date NOT NULL,
  `X_ray production` varchar(255) DEFAULT NULL,
  `Image Acquisition` varchar(255) DEFAULT NULL,
  `Interior cleaning` varchar(255) DEFAULT NULL,
  `Safety interlock` varchar(255) DEFAULT NULL,
  `Warning lamp` varchar(255) DEFAULT NULL,
  `Sensors` varchar(255) DEFAULT NULL,
  `Future issues` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Mobile_X_ray`
--

INSERT INTO `PPM_Mobile_X_ray` (`PPM_Date`, `X_ray production`, `Image Acquisition`, `Interior cleaning`, `Safety interlock`, `Warning lamp`, `Sensors`, `Future issues`, `Signature`) VALUES
('2020-01-01', 'done', 'done', 'all is clean', 'finction well', 'changed lamp as it has low intensity', 'function well', 'no future issue', 'AE');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Monitor`
--

CREATE TABLE IF NOT EXISTS `PPM_Monitor` (
  `PPM_Date` date NOT NULL,
  `Mounting hard Ware` varchar(255) DEFAULT NULL,
  `screws` varchar(255) DEFAULT NULL,
  `Case and cables connector` varchar(255) DEFAULT NULL,
  `Flat panel display frame` varchar(255) DEFAULT NULL,
  `Power supply` varchar(255) DEFAULT NULL,
  `Power switch` varchar(255) DEFAULT NULL,
  `Touch screen in the event` varchar(255) DEFAULT NULL,
  `Functional test` varchar(255) DEFAULT NULL,
  `Alarm limits` varchar(255) DEFAULT NULL,
  `Network` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Monitor`
--

INSERT INTO `PPM_Monitor` (`PPM_Date`, `Mounting hard Ware`, `screws`, `Case and cables connector`, `Flat panel display frame`, `Power supply`, `Power switch`, `Touch screen in the event`, `Functional test`, `Alarm limits`, `Network`, `Signature`) VALUES
('2020-01-01', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'AE'),
('2020-01-30', 'tight well', 'dine', 'well connected', 'done ', 'done', 'function well', 'there is lagging in the screen', 'test passed well', 'done', 'well connected', 'AE');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Suction_unit`
--

CREATE TABLE IF NOT EXISTS `PPM_Suction_unit` (
  `PPM_Date` date NOT NULL,
  `Tubing` varchar(255) DEFAULT NULL,
  `Collection bottle` varchar(255) DEFAULT NULL,
  `filter` varchar(255) DEFAULT NULL,
  `Battery` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Suction_unit`
--

INSERT INTO `PPM_Suction_unit` (`PPM_Date`, `Tubing`, `Collection bottle`, `filter`, `Battery`, `Signature`) VALUES
('2020-01-01', 'well connected', 'No cracks and leakage is resolved', 'filter has been changed', 'function well', 'AB');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Syringe_Pump`
--

CREATE TABLE IF NOT EXISTS `PPM_Syringe_Pump` (
  `PPM_Date` date NOT NULL,
  `condition of the external surface` varchar(255) DEFAULT NULL,
  `AC Power supply and cables` varchar(255) DEFAULT NULL,
  `case keyboard and plunger` varchar(255) DEFAULT NULL,
  `start up self test operation` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Syringe_Pump`
--

INSERT INTO `PPM_Syringe_Pump` (`PPM_Date`, `condition of the external surface`, `AC Power supply and cables`, `case keyboard and plunger`, `start up self test operation`, `Signature`) VALUES
('2020-01-01', 'Done', 'need to be changed ', 'Done', 'Done', 'AB');

-- --------------------------------------------------------

--
-- Table structure for table `PPM_Ventilator`
--

CREATE TABLE IF NOT EXISTS `PPM_Ventilator` (
  `PPM_Date` date NOT NULL,
  `Inlet filter` varchar(255) DEFAULT NULL,
  `Outer closure` varchar(255) DEFAULT NULL,
  `Door hinge` varchar(255) DEFAULT NULL,
  `Latch mechanism` varchar(255) DEFAULT NULL,
  `Connectors` varchar(255) DEFAULT NULL,
  `Handle` varchar(255) DEFAULT NULL,
  `Power cord` varchar(255) DEFAULT NULL,
  `External tubing` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PPM_Ventilator`
--

INSERT INTO `PPM_Ventilator` (`PPM_Date`, `Inlet filter`, `Outer closure`, `Door hinge`, `Latch mechanism`, `Connectors`, `Handle`, `Power cord`, `External tubing`, `Signature`) VALUES
('2020-01-01', 'changed filter', 'done', 'done', 'finction well', 'well connected', 'free of damages', 'done', 'connected well', 'ES');

-- --------------------------------------------------------

--
-- Table structure for table `Radiology`
--

CREATE TABLE IF NOT EXISTS `Radiology` (
  `Department` varchar(255) DEFAULT NULL,
  `DeviceName` varchar(255) DEFAULT NULL,
  `Brand` varchar(255) DEFAULT NULL,
  `Model` varchar(255) DEFAULT NULL,
  `SerialNumber` varchar(255) NOT NULL,
  `CountryOfOrigin` varchar(255) DEFAULT NULL,
  `InstallationDate` date DEFAULT NULL,
  `SupplyingDate` date DEFAULT NULL,
  `WarrantyPeriod` int(11) DEFAULT NULL,
  `CompanyName` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Radiology`
--

INSERT INTO `Radiology` (`Department`, `DeviceName`, `Brand`, `Model`, `SerialNumber`, `CountryOfOrigin`, `InstallationDate`, `SupplyingDate`, `WarrantyPeriod`, `CompanyName`) VALUES
('Radiology', 'Mammography', 'GE', 'Performa MGF 110', '12220', 'USA', '2006-11-30', '2006-11-30', 2, 'General electric'),
('Radiology', 'Dye Injector', 'Midrad', 'Spectris Solaris EP', '301201261310', 'USA', '2013-08-25', '2013-08-25', 2, 'Philips'),
('Radiology', 'Diagnostic X-Ray', 'Philips', 'Duo diagnost', '451220202201', '', '2010-03-24', '2010-03-24', 2, 'Republic'),
('Radiology', 'Dental digital panorama', 'Serona ', 'OPXG 3D ready', '49635', 'Germany', '2013-08-20', '2013-08-20', 2, 'International group'),
('Radiology', 'Ultrasound ', 'GE', 'Logiq P7', '500047SU7', 'Korea', '2016-10-03', '2016-10-03', 2, 'Alkan medical'),
('Radiology', 'Automatic X-RAY Film Developer', 'Fuji film', 'DRYPIX4000', '66723822', 'JAPAN', '2006-11-30', '0000-00-00', 2, 'General electric'),
('Radiology', 'Bone X-RAY', 'GE', 'Prodigy', '69690', 'USA', '2006-07-17', '2006-07-17', 2, 'Kimmit'),
('Radiology', 'CT', 'Toshiba', 'Aguilion one', '6AA1242056', 'Japan', '2013-05-25', '2013-05-25', 2, 'Medical technology for trade'),
('Radiology', 'MRI', 'Philips', 'INGENA', '781396', 'USA', '2013-08-25', '2013-08-25', 2, 'Philips'),
('Radiology', 'FCR', 'Fuji film', 'FCR-XG5000', '96525518', 'JAPAN ', '2010-03-24', '2010-03-24', 2, 'Republic'),
('Radiology', 'Anesthesia', 'DAMCA', 'DAMCA MRI 508', 'MRI505087191', 'USA', '2013-08-25', '2013-08-25', 2, 'Philips'),
('Radiology', 'Dopler', 'Philips', 'Affiniti 50', 'USD15D0281', 'USA', '2016-04-19', '2016-04-19', 2, 'International Nile Company');

-- --------------------------------------------------------

--
-- Table structure for table `Radiology_DailyI`
--

CREATE TABLE IF NOT EXISTS `Radiology_DailyI` (
  `DATE` date NOT NULL DEFAULT '0000-00-00',
  `Equipment cleaning` varchar(255) DEFAULT NULL,
  `Damages Or Abnormalities` varchar(255) DEFAULT NULL,
  `preparation of protection apron` varchar(255) DEFAULT NULL,
  `Switches Presetting And Dials` varchar(255) DEFAULT NULL,
  `Power ON and confirm self test pass` varchar(255) DEFAULT NULL,
  `X_ray exposure is available on the desired setting` varchar(255) DEFAULT NULL,
  `Abnormasound vibration or smell` varchar(255) DEFAULT NULL,
  `Cleaning Of Equipment And Accessories` varchar(255) DEFAULT NULL,
  `Dental Degital Panorama Comments` varchar(255) DEFAULT NULL,
  `Cleaning equipment and detector` varchar(255) DEFAULT NULL,
  `damage or abnormalities` varchar(255) DEFAULT NULL,
  `Accessories ready to use` varchar(255) DEFAULT NULL,
  `Switches` varchar(255) DEFAULT NULL,
  `FHR` varchar(255) DEFAULT NULL,
  `Cleaning equipment and Accessories After Operation` varchar(255) DEFAULT NULL,
  `Doppler Comments` varchar(255) DEFAULT NULL,
  `Cleaning equipment` varchar(255) DEFAULT NULL,
  `Remove Racks And Wash It` varchar(255) DEFAULT NULL,
  `Damages or abnormality` varchar(255) DEFAULT NULL,
  `Switches maps and dials` varchar(255) DEFAULT NULL,
  `Power on abnormal sound vibration smell or leak of liquid` varchar(255) DEFAULT NULL,
  `Temperature` varchar(255) DEFAULT NULL,
  `sound movement and vibration when feeding test films` varchar(255) DEFAULT NULL,
  `equipment and accessories cleaning after any operation` varchar(255) DEFAULT NULL,
  `X_Ray_Film Developer Comments` varchar(255) DEFAULT NULL,
  `equipment clean` varchar(255) DEFAULT NULL,
  `damages on cables and unit` varchar(255) DEFAULT NULL,
  `movement of X_ray tube holder bucky table and bucky stand` varchar(255) DEFAULT NULL,
  `Locking mechanism` varchar(255) DEFAULT NULL,
  `movement of collimator` varchar(255) DEFAULT NULL,
  `switches and dials` varchar(255) DEFAULT NULL,
  `unit energized After power on` varchar(255) DEFAULT NULL,
  `value for kVA and mA` varchar(255) DEFAULT NULL,
  `X_ray exposure` varchar(255) DEFAULT NULL,
  `sound vibration or smell` varchar(255) DEFAULT NULL,
  `equipment accessories cleaning after operation` varchar(255) DEFAULT NULL,
  `Bone X_Ray Comments` varchar(255) DEFAULT NULL,
  `EquipmentCleaning` varchar(255) DEFAULT NULL,
  `abnormalities and damages` varchar(255) DEFAULT NULL,
  `Ultrasound jell` varchar(255) DEFAULT NULL,
  `switches dials and keyboard` varchar(255) DEFAULT NULL,
  `Power` varchar(255) DEFAULT NULL,
  `Operation of the equipment` varchar(255) DEFAULT NULL,
  `accessories cleaning after operation` varchar(255) DEFAULT NULL,
  `Diagnostic Ultrasound Comments` varchar(255) DEFAULT NULL,
  `Machine cleaning` varchar(255) DEFAULT NULL,
  `Abnormalities` varchar(255) DEFAULT NULL,
  `accessories` varchar(255) DEFAULT NULL,
  `CO2 Color` varchar(255) DEFAULT NULL,
  `flow meters` varchar(255) DEFAULT NULL,
  `pop off valve switches and knob` varchar(255) DEFAULT NULL,
  `abnormal sound vibration and gas leak sound` varchar(255) DEFAULT NULL,
  `flow meter N2O flows` varchar(255) DEFAULT NULL,
  `alarm sound` varchar(255) DEFAULT NULL,
  `Accessories Cleaning` varchar(255) DEFAULT NULL,
  `Anesthesia machine comments` varchar(255) DEFAULT NULL,
  `equipment clean free of cracks loose parts` varchar(255) DEFAULT NULL,
  `hoses and cables` varchar(255) DEFAULT NULL,
  `cleaning solution for the breast` varchar(255) DEFAULT NULL,
  `Monitor viewing conditions` varchar(255) DEFAULT NULL,
  `accessories are clean and no damage after any operation` varchar(255) DEFAULT NULL,
  `Mammography comments` varchar(255) DEFAULT NULL,
  `free of cracks loose parts clean equipment` varchar(255) DEFAULT NULL,
  `Monitor system performance` varchar(255) DEFAULT NULL,
  `Image artifacts` varchar(255) DEFAULT NULL,
  `abnormal sound` varchar(255) DEFAULT NULL,
  `Resonance` varchar(255) DEFAULT NULL,
  `Low contrast detectability` varchar(255) DEFAULT NULL,
  `MRI Comments` varchar(255) DEFAULT NULL,
  `Cleaning` varchar(255) DEFAULT NULL,
  `noise and field Uniformity` varchar(255) DEFAULT NULL,
  `image quality` varchar(255) DEFAULT NULL,
  `CT Comments` varchar(255) DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Radiology_DailyI`
--

INSERT INTO `Radiology_DailyI` (`DATE`, `Equipment cleaning`, `Damages Or Abnormalities`, `preparation of protection apron`, `Switches Presetting And Dials`, `Power ON and confirm self test pass`, `X_ray exposure is available on the desired setting`, `Abnormasound vibration or smell`, `Cleaning Of Equipment And Accessories`, `Dental Degital Panorama Comments`, `Cleaning equipment and detector`, `damage or abnormalities`, `Accessories ready to use`, `Switches`, `FHR`, `Cleaning equipment and Accessories After Operation`, `Doppler Comments`, `Cleaning equipment`, `Remove Racks And Wash It`, `Damages or abnormality`, `Switches maps and dials`, `Power on abnormal sound vibration smell or leak of liquid`, `Temperature`, `sound movement and vibration when feeding test films`, `equipment and accessories cleaning after any operation`, `X_Ray_Film Developer Comments`, `equipment clean`, `damages on cables and unit`, `movement of X_ray tube holder bucky table and bucky stand`, `Locking mechanism`, `movement of collimator`, `switches and dials`, `unit energized After power on`, `value for kVA and mA`, `X_ray exposure`, `sound vibration or smell`, `equipment accessories cleaning after operation`, `Bone X_Ray Comments`, `EquipmentCleaning`, `abnormalities and damages`, `Ultrasound jell`, `switches dials and keyboard`, `Power`, `Operation of the equipment`, `accessories cleaning after operation`, `Diagnostic Ultrasound Comments`, `Machine cleaning`, `Abnormalities`, `accessories`, `CO2 Color`, `flow meters`, `pop off valve switches and knob`, `abnormal sound vibration and gas leak sound`, `flow meter N2O flows`, `alarm sound`, `Accessories Cleaning`, `Anesthesia machine comments`, `equipment clean free of cracks loose parts`, `hoses and cables`, `cleaning solution for the breast`, `Monitor viewing conditions`, `accessories are clean and no damage after any operation`, `Mammography comments`, `free of cracks loose parts clean equipment`, `Monitor system performance`, `Image artifacts`, `abnormal sound`, `Resonance`, `Low contrast detectability`, `MRI Comments`, `Cleaning`, `noise and field Uniformity`, `image quality`, `CT Comments`, `Signature`) VALUES
('2020-05-20', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'no problem', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'no future issue', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'done', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', '', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'no comment', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'done', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'no comment', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'done', 'Checked', 'Checked', 'Checked', 'no problem', 'AE'),
('2020-05-21', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'cables need to be changed', 'Checked', 'Checked', 'Checked', 'Checked', NULL, 'Checked', 'no future issue', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'switches need to be changed', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', '', 'Checked', NULL, 'Checked', 'Checked', NULL, 'Checked', 'Checked', 'jell expired', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'done', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', '', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'Checked', 'done', 'Checked', 'Checked', 'Checked', 'no problem', 'ES');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Catheter`
--
ALTER TABLE `Catheter`
  ADD PRIMARY KEY (`SerialNumber`),
  ADD UNIQUE KEY `SerialNumber` (`SerialNumber`);

--
-- Indexes for table `catheter_DailyI`
--
ALTER TABLE `catheter_DailyI`
  ADD PRIMARY KEY (`DATE`);

--
-- Indexes for table `OpenHeart_ICU`
--
ALTER TABLE `OpenHeart_ICU`
  ADD PRIMARY KEY (`SerialNumber`),
  ADD UNIQUE KEY `SerialNumber` (`SerialNumber`);

--
-- Indexes for table `PPM_Defibrillator`
--
ALTER TABLE `PPM_Defibrillator`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_ECG`
--
ALTER TABLE `PPM_ECG`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_ECG_Ultrasound`
--
ALTER TABLE `PPM_ECG_Ultrasound`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Exercise_ECG`
--
ALTER TABLE `PPM_Exercise_ECG`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Measure_blood_gas`
--
ALTER TABLE `PPM_Measure_blood_gas`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Mobile_X_ray`
--
ALTER TABLE `PPM_Mobile_X_ray`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Monitor`
--
ALTER TABLE `PPM_Monitor`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Suction_unit`
--
ALTER TABLE `PPM_Suction_unit`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Syringe_Pump`
--
ALTER TABLE `PPM_Syringe_Pump`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `PPM_Ventilator`
--
ALTER TABLE `PPM_Ventilator`
  ADD UNIQUE KEY `PPM_Date` (`PPM_Date`);

--
-- Indexes for table `Radiology`
--
ALTER TABLE `Radiology`
  ADD PRIMARY KEY (`SerialNumber`),
  ADD UNIQUE KEY `SerialNumber` (`SerialNumber`);

--
-- Indexes for table `Radiology_DailyI`
--
ALTER TABLE `Radiology_DailyI`
  ADD PRIMARY KEY (`DATE`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
