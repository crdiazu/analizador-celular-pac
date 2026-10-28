# G-NetTrack Manual - Gyokov Solutions

G-NetTrack Manual 

**G-NetTrack**

## G-NetTrack Manual

Your browser does not support inline frames or is currently configured not to display inline frames.

### [Introduction](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

**G-NetTrack Pro** is a wireless network monitor and drive test tool for Android OS devices. It allows monitoring and logging of mobile network parameters without using specialized equipment. It's a tool and it's a toy. It can be used by professionals to get better insight on the network or by radio enthusiasts to learn more about wireless networks. It can be used even if you want just to make easy representation of your traveled route.

[Here is a video demonstration of G-NetTrack Pro](https://www.youtube.com/watch?v=nQPJURKpCkM) and [here are videos showing G-NetTrack Pro applications.](https://www.youtube.com/playlist?list=PLeZ3lA81P9ETJ_sdEFuRWyfxK3wHoj_hK)

Download pdf version of manual - [here](http://www.gyokovsolutions.com/manuals/G-NetTrack_Pro_manual.pdf)

Using application you can easily pinpoint network problems like:

bad coverage - low RXLEVEL

low uplink and downlink data throughput

lack of dominant server causing lot of cell reselections and frequent service interruptions - when the serving cell time is small

weak 3G coverage - when you have a lot of reselections between cells on 3G and 2G

blocked calls

dropped calls

The main features of **G-NetTrack Pro** are:

2G/3G/4G serving and neighbor cells information measurement

Record measurements in logfiles (text and kml format)

Cellfile import/export and sites and serving and neighbor cells lines visualization on map

Frequency information ARFCN measurements

OUTDOOR and INDOOR measurements

AUTO INDOOR mode for tunnels and places with bad GPS reception

Dual SIM support

Cell scan kml export

Floorplans load

Predefined routes load

3D map - different types of maps, 3D buildings, maps auto caching

Data (upload,download,ping) test sequence

Voice test sequence

Mixed Data/Voice sequence

Bluetooth control of multiple phones

G-NetWiFI control

Cells scan

Multithread upload and download

Chart with serving and neighbor cells levels

Unlimited number of cell layers and custom cell colors

Barometer usage for height determination

Voice announcements for different events

Screen orientation change

The measured data by G-NetTrack can be analyzed with the help of other tools available here on this site as [G-NetLook Pro](https://play.google.com/store/apps/details?id=com.gyokovsolutions.gnetlookpro) , [G-NetView Pro](https://play.google.com/store/apps/details?id=com.gyokovsolutions.gnetviewpro) and [G-NetLook Web](http://www.gyokovsolutions.com/G-NetLook).

### [Tabs](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

There are five tabs with different information - CELL, NEI, MAP, INFO and DRIVE. The information displayed on each tab is

[2.1 CELL Tab](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

CELL tab shows network and geographical information. It also shows history log of the serving cells. The shown information is:

Operator - the name of your wireless provider

MCC - Mobile Country Code - it is a 3 digit code specific for each country

MNC - Mobile Network Code - it is 2 or 3 digits code and is specific for each operator in the country

LAC - location area code - the network is split by location areas, in which the subscriber is paged in all cells simultaneously. LAC is the code of the current area

NODE - Radio Network Controller - when on 3G it shows the ID of the RNC that controlls the current serving cell. On 4G it shows enodeB ID.

CID - the CELLI ID of the current serving cell

PCI/PSC/BSIC - PCI on 4G, PSC on 3G and BSIC on 2G for current serving cell.

F - ARFCN frequency channel number

B - frequency band (Uxx for 3G, Lxx for LTE)

TA - timing advance - for 2G and 4G

Type - the network technology mode (like GPRS, EDGE on 2G or UMTS, HSPA etc... on 3G)

LEVEL - the current signal strength in dBm. For different technologies the caption is different - RXLEV for 2G, RSCP for 3G and RSRP for 4G.

QUAL - the signal quality of the network. For different technologies the caption is different - RXQUAL for 2G, ECNO for 3G and RSRQ for 4G. This value is not reported by most phones. Only several phones report ECNO and maybe no phone reports RXQUAL.

SNR - signal to noise ratio. It is measured on LTE only.

CQI - channel quality indicator. It is measured on 4G only.

Longitude - current location longitude in decimal format

Latitude - current location latitude in decimal format

Speed - current speed in kmph.

Accuracy - the accuracy with which the location is determined. Location determination could be based on GPS or Network (using Google location service - using serving and neighbor cells or WiFi networks)

Height - the difference between Altitude and Ground values

Altitude - the GPS measured altitude

Height - the ground level height - this is ajustable in settings.

UL - the current uplink data transfer speed in kbps

DL - the current downlink data transfer speed in kbps

Data - the used data network - Mobile Network or WiFi

Phone State - IDLE, CALL, DATA - the current phone state - if it is idle or in active data transfer or in active voice call

Serving Time - the current serving cell time in seconds. If cellfile is used this line also shows the serving cell name and cell layer.

Serving cell history table - this table shows history log of serving cell changes with time of the change and level at which this change happened. The table also shows cell serving time which is useful for spotting frequent cell reselection and lack of dominant cells. Also here it is possible to see loss of network coverage - rows with level values equal to -201.

[2.2 NEI Tab](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

NEI tab shows information about neighbor cells measurements. It consists of two tables:

Serving cell table - shows information about current serving cell id and level. when on 3G CELLID column will show RNC-CELLID and PSC (Primary Scrambling Code) if the phone reports it.

Neighbor cells table - shows information about the current neighbor cells and their levels. When on 2G the neighbors are shown as LAC and CELLID. When on 3G they are shown as PSC

In neighbors table for 4G PCI collision are shown with exclamation sign "!" - !(mod3), !!(mod6), !!!(mod30) and serving - neighbor level difference - enable it in SETTINGS - OTHER - Show PCI collisions and Show level difference for PCI collisions.

The neighbor cells information is not reported by all phones. Check [phone measurement capabilities](http://www.gyokovsolutions.com/survey/surveyresults.php) for more information.

At the bottom of the NEI tab is area with links to other available tools on this site.

[2.3 MAP tab](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

MAP tab shows geographical view of hte measurements and mobile network basestations.

In the first row there is information about current technology, cell layer, MCC-MNC-LAC-RNC-CELLID of the current serving cell, level and quality measurements.

On the second row there is information about the distance to serving cell and bearing to it. This information is available only if cellfile with networks cell information is loaded. On this row also is information about the GPS - if it has fix (green color) or not (red color).

The map shows the surrounding area view and thematic map of selected measurement (LEVEL, QUAL, CELL, DL bitrate, UL bitrate, SPEED).

There are four buttons available:

first button is for changing the thematic map measurement

"Export" button - exports the current thematic map of the selected measurements in kml format. This is useful for on the fly recording of measurement if the logging function has not been turned on.

"Screenshot" button - saves the snapshot of the current view - useful for on the fly saving of image representation of the measurements.

"Clear" button - clears the view - if there are a lot of points, it can slow the map view and then is good to clear the view.

[2.4 INFO tab](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

The INFO tab provides following information:

Log Status - shows if the log recording has been started or not

IMSI - SIM card Inernational Mobile Subscriber Identity - this is useful for providing information in order different traces to be performed by Network Operator.

IMEI - this is hardware ID of the mobile phone

Current Operator - name of the current serving operator

Current Country - the country of the used mobile provider

Home Operator - name of your operator

Home Country - country of the Home Operator

Is Roaming - if the mobile is in roaming or not

MSISDN - your phone number

SD Card - if sd card storage is available

App folder - the used root folder for exported files - the folder where G-NetTracl_Logs folder stays

Cellfile - the loaded cellfile name

G-NetTrack version - current version of the app

G-NetTrack code - number representation of the current app verson

Android SDK - the Android OS version number

Device - device name

Brand - device brand

Device Manufacturer - manufacturer of the device

Build Number - device software build

Network Type Num - network type number - determines the current network mode (GSM, HSDPA, CDMA etc...). If your phone shows 0 (unknown) in idle or connected mode, check [Discard Network Type 0] in Settings in order to report correctly the level

Sequence Status - status of voice/data sequence

Voice Calls - number of voice calls performed in Voice Sequence

Successfull Calls - number of successfully started and finished calls made in Voice Sequence

Blocked Calls - number of blocked calls in voice sequence

Dropped Calls - number of dropped calls that occur in Voice Sequence

[2.5 DRIVE tab](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

DRIVE tab represent the main serving cells information in comfortable format with big font letters

### [Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Settings are activated via Menu - Settings. There are several group of settings, which are related to different app features:

[MAP Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Map Satellite View - switches satellite/street view of the map

Map in background - when active the GPS stays on while the app is in the background when the log is not started

Auto center map - switches on/off automatic centering of the map around current location

Auto rotate map - switches on/off automatic rotation of the map

Speed in km/h - when checked the speed is shown in kilometers per hour. Uncheck it to show speed in miles per hour.

Point Size - size of the point on map view

Serving Cell Font Size - font size of the serving cell on Map view

Cells Font Size - font size of the cells on Map view

Serving Cell Thickness - thickness of the serving cell on Map view

Cells Thickness - thickness of the cells on Map view

2G cell layers colors - colors in RRGGBB format for 2G layers (default 4 layers). Modify the colors or add new layers via adding "," and new layer color

3G cell layers colors - colors in RRGGBB format for 3G layers (default 4 layers). Modify the colors or add new layers via adding "," and new layer color

4G cell layers colors - colors in RRGGBB format for 4G layers (default 4 layers). Modify the colors or add new layers via adding "," and new layer color

Ground Level - sets the ground level altitude. When set different than 0 Height in CELL tab shows the height above this ground/street level

Neighbor Cell Line Thickness - thickness of neighbor cell lines

Neighbor Cell Line Color - color in RRGGBB of neighbor cell line

Log reduction factor - when this value (N) is bigger than 1 then every N-th measurements is shown on map. This does not impact the logfile

Auto clear log points - when it is on then the log points will be cleared periodically in order their number to be kept constant. This will improve app performance since too many log points slow the app.

Maximum number of points on map - the maximum number of log points on map. If the function for autoclearing log points is on then when number of points is bigger than this value a part of log points is cleared.

Show serving cell info on map tab - Show serving cell info on map tab (requires app restart)

Serving cell info font size - Set serving cell info font size (requires app restart)

Show LAC, NODE, CELLID, PC, ARFCN on map tab - Show LAC, NODE, CELLID, PC, ARFCN on map tab (requires app restart)

Show LEVEL, QUAL, SNR on map tab - Show LEVEL, QUAL, SNR on map tab (requires app restart)

Show distance and bearing on map tab - Show distance and bearing on map tab (requires app restart)

[SITES Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Show Sites - requires cellfile. When it is on the list of cells from cellfile will be loaded at the program start. Requires restart of the app.

Use database - when this is on then database cell loading will be used instead of loading cells from cellfile. Database cell load is way faster. [Here is demo video of cell database usage](https://www.youtube.com/watch?v=ZUq2bW5GwDE).

DATABASE OPTIONS

Order by distance - when it is on it will guarantee showing closest cell. When it is off then loading will be faster.

Limit by distance - Read from database cells in [Distance limit] range. When this is on loading will be faster.

Distance limit in kilometers - distance limit when limit by distance is on.

Check if cellfile is more recent than database - check if cellfile is more recent than database. If cellfile is more recent you will see message and you can refresh database using Menu - Refresh cell database.

Show Serving Line - shows a line between current location and srving cell location

Show Cell Names - shows cell names in map view

Show dots for cells - checking this will draw dots instead lines for cells which improves map performance

Max visualized cells - This is the max number of cells that will be visualized from all cells that are loaded in memory. If you want to increase this number you can use the two features below to achieve better map performance

Visualize only sites in range - loads all the cells, but visualize only sites in specified range - usefull when the cellfile is big and the map view is slowed down because the big number of cells

Auto refresh sites in range - the surrounding sites will be refreshed on location change when [Visualize only sites in range] is selected.

Range of loaded sites - range in meters around current location of sites to be loaded

Add unknown cells - when this option is on the new cells are automatically added to cellfile. If you have no cellfile and both [Show Sites] and [Add unknown cells] are on, the app will create new cellfile and when the log is on it will start filling it with new cells.

Show neighbor cells names - when checked the neighbor cell name, distance and bearing will be shown on Neighbors table (requires 3G PSC/ 4G PCI info in cellfile)

Show neighbor cells lines - when checked the neighbor cell lines will be visualized on map (requires 3G PSC/4G PCI info in cellfile)

Cell coloring type - choose the cell coloring based on TECH, CELLID or PCI/PSC/BSIC.

[INDOOR Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Indoor Mode - Switches Indoor mode On/Off

Buffer Size - Max number of measurement samples in buffer during Indoor mode

Auto Indoor Mode - Switches Auto Indoor mode On/Off

Auto Indoor Accuracy threshold - when GPS accuracy is bigger than this value GPS fix is considered not valid and Auto Indoor mode is started

Auto Indoor Time threshold - when last GPS fix was more seconds ago than this value - the GPS fix is considered not valid and Auto Indoor mode is started

Set point in Auto Indoor mode - when On the tool for setting points in indoor mode is shown and points on the route can be set

How to use indoor mode:

[Here is a video demonstration of INDOOR mode with G-NetTrack Pro](https://www.youtube.com/watch?v=_VwzJiA__EY)

[Here is a video demonstration of subway measurements in INDOOR mode with G-NetTrack Pro](https://www.youtube.com/watch?v=61ceKjzor3A)

Go to Settings and activate INDOOR MODE

On Map the button [Set Point] and center point will appear

Point your current location on the map center and press [Set Point] - a marker will appear on the map

Move to the next point. Center map on it and press [Set Point] - several new markers (one for each second) will appear connecting previous and current location

Go through the route putting points when you change direction.

You can clear the markers using [CLR] button

AUTO INDOOR mode allows auto filling of measurement points when the GPS fix is not available like in tunnels or on places with bad GPS recep tion.

When GPS fix is lost the measurements are collected in a buffer and when the GPS fix is back again the missing measurements are filled on a straight line connecting the point of loss and regaining GPS fix.

Alternatively you can use the point set tool to set intermediate points if the route is not straight line - [Settings] - [Set Point in auto indoor mode].

[Here is a video demonstration of tunnel measurements in AUTO INDOOR mode with G-NetTrack Pro](https://www.youtube.com/watch?v=uSVangL2GSM)

AUTO INDOOR mode works only when the log is active.

If INDOOR mode is selected AUTO INDOOR mode is not activated.

How to use it:

Enable AUTO INDOOR mode in Settings.

Choose threshold for GPS validity

Accuracy - if the GPS accuracy is bigger than this threshold the GPS is considered not valid

Time - if the last good GPS fix was received before the specified value (in seconds) - the GSP is considered not valid.

When log is active both current values are visible on the upper right corner of MAP tab next to GPS writing. When one of the conditions is satisfied the GPS fix is considered not valid and values are colored in blue.

Start log.

When you enter the tunnel and lose GPS fix the GPS writing on upper right corner of MAP tab will color in blue which means that AUTO INDOOR mode is active and measurements are collected. In order measurements to be more precise you can wait a little until GPS fix is lost at the beginning of the tunnel and the entering point is auto set.

When you go out of the tunnel and GPS fix is valid the values for GPS accuracy and time are colored in green, the exiting point is auto set and the missing measurements between entering and exiting point are shown on the map and filled in the log.

[VOICE SEQUENCE Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Here is a video demonstration of VOICE SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=VRe-0JPNwGU)

VOICE SEQUENCE allows automatic generation of voice calls to specified number with specified duration and pause between the calls. When Voice Sequence is active the number of successful, blocked and dropped calls are shown in INFO tab

Called Number - the number to be dialed. You can enter several numbers ("," comma separated) that will be called sequentially.

Number of Calls - number of calls to be made

Call Duration - duration of a single call

Pause Between Calls - pause between the calls

Start calls only on - allows starting of calls only on specific technology (2G, 3G, 4G) - useful for example when you want to test 3G coverage only. If the call has been handovered to 2G the sequence will wait until 3G is reselected again and then will continue

Keep app in foreground - keeps app in foreground during voice sequence

On some phones the app can start calls only if app is in foreground. In this case keep the app in foreground in order to make calls. On these phones the option to keep automatically app in foreground does not work so you have to bring the app to foreground manually if it was in background.

[DATA SEQUENCE Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Here is a video demonstration of DATA SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=8i-hYpXRer8)

DATA SEQUENCE allows test of data transfer.

Ping - include PING in data sequence

Ping URL - the URL for ping test. The format is like www.xxxxxxxxxxxxxx.com or 10.100.1.101

Upload - include UPLOAD in data sequence

Upload URL - the URL for upload test. The format should start with http:// and is like

http://www.xxxxxxxxxxx.com.

Upload time, s - time for upload in seconds.

Download - include DOWNLOAD in data sequence

Download URL - the URL for ping test. The format should start with http:// and is like http://www.xxxxxxxxxxx.com/downloadedfile.mp3. It is recommended to set bigger file which can not be downloaded fully for download time in order to achieve bigger download speed.

Download time, s - time for download in seconds.

Pause between tests - pause between test cycles

Log bitrates only during data test - when this is checked current DL and UL bitrates will be logged only when data sequence is active. Useful when you want to view easily the maximum available bitrates

Multithread - when checked multiple simultaneous connections will be used for upload and download in Data Test and Data Sequence. Using several threads increases the bitrates.

Number of threads - the number of threads to be used ([Multithread] should be checked). Set number of simultaneous threads more than 1 and less or equal to number of phone CPU.

Simultaneous UL/DL (experimental feature) - When checked then UL and DL data transfer is performed simultaneously. Make sure the phone processsor has at least 8 cores in order to use this.

Export data test summary - When checked then text file datatest.txt containing results of data sequence and data tests is written in log folder. You can view results on the map in datatest.kml file.

Show data sequence errors - this is for data sequence problems debugging only. Keep this off. You might see some messages even when everything works ok.

**IMPORTANT!** Make sure you are using for DL and UL URL server with good connectivity. In this case you will get results similar to apps that use dedicated servers for data throughput test. Here is a [screenshot](http://www.gyokovsolutions.com/img/speedtest_comparison.png) showing similar results when compared with such apps.

[SMS SEQUENCE Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

SMS sequence is not available anymore due to Google policy for apps not to use SMS.

[Here is a video demonstration of SMS SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=vaBAsm_kybg)

SMS SEQUENCE allows test of SMS sending and delivery.

Number of SMS - numbers of SMS that are sent

SMS recipient - MSISDN of recipient to whom the SMSs are sent

SMS text - text of SMS message

Pause between SMS - pause (seconds) between SMS messages

[MIXED SEQUENCE Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Here is a video demonstration of MIXED SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=32QaozZFZTc)

Mixed sequence allows including multiple types of test - data/voice/SMS in a test sequence. The settings for each type of test is taken from respective sequence settings.

Data Test - include data test in sequence.

Voice Test - include data voice in sequence.

SMS Test - include SMS test in sequence. SMS sequence is not available anymore due to Google policy for apps not to use SMS.

Test Pause - pause between test cycles.

Number of cycles - number of mixed sequence cycles.

[KML EXPORT Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Here are the settings for enabling different measurements export while log is started. When activated a kml for specified measurement will be generated in the export file folder for each log in the G-NetTrack_Logs folder on your main storage.

The following measurement exports are available:

CELLID

LEVEL

QUAL

TECHNOLOGY - 2G/3G/4G

TECHNOLOGY MODE - GPRS/EDGE/HSPA etc...

EVENTS - cell reselections and voice sequence events like call start, call end, blocked call and dropped call (CR - Cell Reselection, HV - Voice handover, HD - Data handover)

DL_BITRATE - downlink data transfer bitrate

UL_BITRATE - uplink data transfer bitrate

LAC

RNC

LAYER - Cell layer information - if available in cellfile

SNR

CQI

LTE RSSI

SPEED - the speed of movement

PSC - PCI on 4G, PSC on 3G and BSIC on 2G

ARFCN - frequency channel number

BAND - frequency band

CELL LAYER - serving cell layer

HEIGHT

IP address

Timing advance

Serving distance

Serving antenna bearing

NEIGHBOR CELLS - separate file for cellid and level for each of the first 6 neighbor cells measured

CELLS scan - creates separate kml file for all detected cells. Useful to see cell coverage - check [here](http://www.gyokovsolutions.com/downloads/scan.rar) for sample scan logs

CELLFIND - when active this will activate a CELLFIND feature which shows the serving cell location determined by Google location service, based on the cellid measurements. In order this feature to be available you must have mobile network data connection on. Turn your WiFi off in order to prevent location determination based on WiFi networks. In kml file there is information about the cell location and accuracy. It can help to gain insight on cell size (bigger when accuracy is greater number) and location.

DATA TEST - 5 kml files for DATA SEQUENCE statistics - average ping, ping loss, upload bitrate, download bitrate and datatest.kml with all test data.

Use height in kml - when this is on, the points in the kml file will use altitude information. Make sure you adjust Ground Level in Settings - Map in order Height (over ground level) to be correct.

KML height mode - sets how height is used in kml files. When [Relative to ground] is selected Height (over ground) is used in kml and when [Absolute] - Altitude (over sea level) is used. If area of measurement is relatively flat and ground level does not change much - [Relative to ground] is recommended and if not - [Absolute] is recomended.

If [Relative to ground] is selected make sure you adjusted [Settings - Map - Ground Level], so Height shows correct values since they will be used in kml file. If this mode is used the easiest way is to check what Altitude shows when the phone is on ground level and put this value in [Settings - Map - Ground Level]. Then the Height will show 0 on ground level. Barometer is used does not need to be calibrated in this case.

If [Absolute] is selected and barometer is used for height detemination make sure you set [Settings - Barometer - Barometer height correction], so Altitude shows correct values, since they will be used in kml file. The easiest way to calibrate the barometer in this case is to determine from Google Earth the altitude for your location and adjust [Settings - Barometer - Barometer height correction] so Altitude(B) shows Google Earth value.

Use short kml format - reduces the kml size showing only the respective measurement in the information baloon.

KML Point Size - size of kml dot in kml export file.

Application folder - set the root folder for export files. The folder must exist, otherwise the default folder is used. Check the [App folder] in INFO tab in order to see if the correct folder was chosen. If you want to use external SD card you have to use the specia app folder located in folder "Android/data" where the app is allowed to write files. Usually this is sdcard/Android/data/com.gyokovsolutions.gnettrackproplus. Make sure the folder name is correct cause on some phnes it may be different.

[CELLHUNTER Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

CELLHUNTER Mode - this switches on/off CELLHUNTER mode. Cellfile is required for this feature. When it is on only unknown cells (that are missing in cellfile) will be written in the text and kml log files. This feature is useful for Cell Hunters when they search for new cells in th area.

CELLFILTER Mode - this switches on/off CELLFILTER mode. Cellfile is required for this feature. When it is on only known cells (that are in cellfile) will be written in the text and kml log files. This feature is useful for logging only data for specific cell.

[LEGEND](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Specifies the legend colors and thresholds settings for map and kml export.

[LEVEL Thresholds](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

If use technology offset is checked you can set level technology offset for different technologies. The offset is added to original value and can be positive or negative. Generally for 4G you can set (-20) and for 3G (-10). This will change threshold settings of the legend for different technologies.

[LEVEL Colors](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[QUAL Thresholds](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

If use technology offset is checked you can set level technology offset for different technologies. The offset is added to original value and can be positive or negative.

[QUAL Colors](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[SNR Thresholds](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[SNR Colors](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[CQI Thresholds](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[CQI Colors](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[BITRATE Thresholds](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[BITRATE Colors](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[G-NETREPORT Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Send Measurements Online - allows sending of measurements in real time to [G-NetWorld](http://www.gyokovsolutions.com/G-NetWorld/G-NetWorld.php) service. When activated the phone will send data when logging is started to G-NetWorld where you can share your measurement with other users around the world.

[LOG PARAMETERS Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Time Interval - the interval in seconds between writing record in the log if the location is not changed or cellid is not changed - default 300s, lower values will allow more frequent recording of fluctuations, higher values will make log files smaller and save battery

Distance Interval - the distance interval in meters between writing record in the log when the position is changed - default value 15m, lower values will increase point density, but will use more battery

GPS refresh time interval - time interval between GPS updates

Include IMSI and MSISDN - when on then these values are populated in logfile

Verbose log - when on then in logfile additional data is written which helps for debugging the log

Simple log - when on then only basic values are filled in the log

Write cell info in log - when it is on cell information from cellfile will be written in logfile.

Split log - when on new logfile will be started when number of rows are equal to set max number of rows in logfile.

Max number of rows in logfile - when splitting is on new logfile will be started after number of rows are equal to this value

MCC-MNC LOG FILTER - for writing logs only for specified operators (MCC-MNC-combination)

Enable MCC-MNC filter - enables filter

Filter MCC-MNC list - put ","comma separated list of MCC-MNC of the operators that you want to log - like 284-01,284-02,284-03. The other operators will be filtered out and not present in logfile.

Ask for log name - When on then at log start you can input logfile name.

Log without GPS - when this is on points will be added based on network location provider. You can use this to add ponts when there is no GPS signal. Alternatively you can use auto-indoor mode.

[AUTOMATION Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Auto log on app start - auto start logging when the app is started

Auto VOICE SEQUENCE - auto start VOICE SEQUENCE on app start

Auto DATA SEQUENCE - auto start DATA SEQUENCE on app start

Auto start app on boot - auto start app on phone boot

[ROUTE Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Route color - color of the route

Route size - point size of route

Show direction - draw lines showing direction on route

Reverse Route Direction - when this is on the route is loaded in reverse direction.

Follow route - when this is on colored leading points will be shown ahead on route showing direction

Number of leading points - number of colored leading points showing route direction

Route reduction factor - when this value N is bigger than 1 every Nth point of the route is shown on map

[CHARTS Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Serving and neighbors chart on - turns on/off serving and neighbor cells chart

SERVING AND NEIGHBOR CHART OPTIONS - settings for serving and neighbors chart

LEVEL chart on

QUAL chart on

SNR chart on

BITRATES chart on

TECH chart on

SPEED chart on

ALTITUDE chart on

DISTANCE chart on

ANTENNA BEARING chart on

TA (Timing advance) chart on

Chart buffer - number of points buffere of charts.

[CALIBRATION Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Discard Network Type 0/99 - Check this if your phone reports network type 0 or 99 and as a result the level is -200. Check current network type number on bottom of INFO tab.

Network type 0/99 - casts network type 0 or 99 as what is chosen.

Use old functions for serving and neighbor cells - if YES then serving cell parameters are not based on new API17 functions. Use it if your phone does not support API17 functions.

Calibrate 2G/3G - select it to do calibration of levels for 2G/3G. When calibration is done this will be unchecked automatically. Works only when API17 functions are used.

2G/3G factor - calibration factor for 2G/3G. Works only when API17 functions are used.

Calibrate 4G/5G - select it to do calibration of levels for 4G. When calibration is done this will be unchecked automatically. Works only when API17 functions are used.

4G/5G factor - calibration factor for 4G. Works only when API17 functions are used.

Disable auto calibration - select this when you are sure about adjusting factors for 4G and 2G/3G and do not need auto adjustment.

Use new functions for SNR - if YES the LTE SNR will be read from API17 functions if available.

SNR factor - calibration factor for LTE SNR. Usually is 1, but for some devices should be set to 10. Works only when API17 functions are used.

Use alternative method for network type - check this if network type is not correctly determined. Use this only if your phone supports new API17 functions.

Use MCC MNC for operator name - when on operator name will be MCC-MNC instead of carrier name. - Force updates - if your phone does not automatically update serving cell and level you can force them to do so.

Enhanced mode - when on then cell reselections will be loogged at the exact moment of the event. In log also timesample will be up to milliseconds.

[SMS CONTROL](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

SMS control is not available anymore due to Google policy for apps not to use SMS.

SMS control allows remote control of the app via SMS. The sender of SMS can be controlled via 'Authorized Senders' setting. The app returns confirmation to the sender via SMS.

SMS control - allows SMS control (requires restart of the app)

Authorized senders - phone numbers of people authorized to control the app via SMS

Start logging code - SMS content for starting logging

End logging code - SMS content for stop logging

Start data sequence code - SMS content for starting data sequence

Stop data sequence code - SMS content for stop data sequence

Start voice sequence code - SMS content for starting voice sequence

Stop voice sequence code - SMS content for stop voice sequence

Start SMS sequence code - SMS content for starting SMS sequence

Stop SMS sequence code - SMS content for stop data SMS

Info code - SMS content for requesting phone to send via SMS immediately his current measurements information. When the phone receives this code it replies with SMS with its current measurements.

[BLUETOOTH CONTROL](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Bluetooth control enables simultaneous measurement with multipe phones. One phone is server and others are clients. 

Enable bluetooth server - select it for server phone

Enable bluetooth client - check this for client phones

Bluetooth client ID - choose unique value [1-7] for all clients

Feature activation:

Switch all phones bluetooth on.

Make sure server phone is paired with all clients phones.

Activate feature in SETTING - BLUETOOTH CONTROL.

For server phone select [Enable bluettoth server]

For client phone select [Enable bluetooth client] and choose

unique [Blutooth client ID] for all clients.

Restart the app in order settings to take effect.

When this is done in INFO tab just below the charts

the BLUETOOTH PANEL will be shown.

Now you can control other phones with server phone. The commands available are:

Start Log

Pause log

Resume Log

End Log

Set point in indoor measurements

Data sequence

Voice sequence

SMS sequence

Mixed sequence

Add filemark

[G-NETWIFI CONTROL](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

G-NetWiFi control - enables G-NEtWiFi control from G-NetTrack. This feature allews simultaneous indoor/outdoor logging with both apps.

Here is a [demo video](https://www.youtube.com/watch?v=gp8ZZk6aeW0) of this feature

How to use:

Activate feature in G-NetTrack Pro - Settings - G-NetWiFi control.

Make sure both apps are open - G-NetTrack in foreground and G-NetWiFi in background. Check if G-NetWiFi is allowed to run in background and is not closed. Check if there is not some battery optimisation preventing the app to run in the background. Alternatively you can first start manually log on both apps - this will keep the apps running in background.

When the feature is active following commands will be transferred:

Start Log

Pause Log

Resume Log

End Log

Set points in indoor mode

[BAROMETER Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

If the phone has barometer sensor it can be used to determine height instead of GPS. The barometer sensor has better height accuracy than GPS. Using barometer you can do more accurate height measurement. Using this and setting [Settings - KML Export - Use height in kml] allows you to view height profile of kml logs in Google Earth.

Use barometer for height - app has to be restarted when this is allowed. If checked height will be determined from barometer sensor instead of GPS and you will see (B) next to Altitude on CELL tab.

Barometer height correction - this value is added to barometer height in order to correct the height value. This value has to be often corrected since the altitude dependence of air pressure depends on many factors.

Height change threshold logging - the change of height with this value will generate new record in logfile.

[DUAL SIM Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Dual SIM support - turns on/off dual SIM feature (requires app restart). If in Settings - Calibration - [USe old functions] is checked then old dual sim support is tried. If [Use old functions] is not checked then new dual sim support is started. Read more in Dual SIM section of this manual.

Voice SIM - set the sim card that you are using for voice calls and SMS. All voice related events will be written in logfile for this SIM

Data SIM - set the sim card that you are using for data. All data related values will be written in log for this SIM

Old Dual Sim Settings:

Disable GEMINI dual SIM support - this is valid for old type of dual SIM support - if your phone supports both GEMINI functions for dual sim and also some vendor specific functions then first GEMINI is tried. Check this if you want to skip GEMINI support and try vendor specific.

Use specific classname - check this if you want manually to input dual sim classname for your phone. When checked none of predefined dual im supports will be tried.

Dual SIM classname - classname for dual sim support - example - com.mediatek.telephony.TelephonyManagerEx

Switch SIM cards - use this for example when you have only one SIM in slot 2. In this case you can work without dual mode activated.

[VOICE ANNOUNCEMENTS Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Voice announcements - activates voice announcements for different events - reselections, handovers etc...

Pitch - voice pitch

Speed - voice speed

Voice announcements in log mode only - use announcements only when logging

EVENTS - activate voice announcement for specific event

PHRASES - here you can set what you want the speaker to say for each event. You can select phrases on your own language.

[DRIVE TAB Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Here you can customize the DRIVE TAB look.

Show strength indicator.

DRIVE tab text size - sets font size on DRIVE tab.

Show technology

Show LAC

Show NODE

Show CELLID

Show ARFCN

Show frequency band

Show LEVEL

Show QUAL

Show timing advance

Show SNR

Show CQI

Show speed

Show heading

Show serving distance

Show site bearing

Show antenna bearing

Align values - align values to left.

Show PSC/PCI/BSIC - shows BSIC (GSM) PSC (WCDMA) and PCI (LTE) on DRIVE tab.

Show RSSI

Show CELL and NODE HEX values

Show buttons - show control buttons in DRIVE tab

STRENGTH INDICATOR - settings for customization of strength indicator

Use custom values - enable custom values use

max and min values for different technology - set these values to desired max and min levels for each technology

[OTHER Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Screen orientation - sets the screen orientation

Show events - shows messages for events like reselection handover etc.

History log text size - sets font size for history log on Cell tab.

Serving and neighbor tables text size - sets font size for serving and neighbor tables on Nei tab.

Show PCI collisions - when checked PCI collisions are shown in Neighbors table on NEI tab.

Show level difference for PCI collisions - when on level diffrence in decibels will be shown in brackets in neighbors table.

Filter NODE-CELLID list - filters out specific NODE-CELLID combination from the log - useful when some phone reports sporadic fake cellids. You can put several cells comma separated (NODE1-CELLID1,NODE2-CELLID2)

Show HEX values - when on hex values for cellid are shown.

Show frequency band in NEI tab - when on frequency band will be shown next to ARFCN in NEI tab.

Improved location - when on then the location updates will happen at maximum update rate resulting in better location information. This will increase battery consumption.

Auto screen on - while the log is active if the screen is turned off incidentally (with POWER button) it will be turned automatically on again. This has to be on if your phone does not support new API17 functions. If your phone supports API17 then your screen can be off while logging.

### [Actions](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Start Log](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Starts the logging. During this the text and kml export files are created in G-NetTrack_Logs folder on main phone storage. The measurements kml files that are created can be selected in Settings. A record is put in log on change of position with specified distance interval, change of cellid or each specified time interval if there is no change of position or celld. Time and distance intervals can be set in Settings.

When the logging is activated the app will lock your GPS and screen on and the screen will remain lit during the logging. In order not to interrupt logging you have to not switch the device screen off. The phone could be locked, but the screen should be on.

[Pause Log](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Pauses the log.

[Resume Log](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Resumes the log.

[End Log](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Finishes the log.

[Add Filemark](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Adds the filemark (note) to the file. The filemarks are visible in text logfile and filemarkers.kml file.

[Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens the settings page.

[Exit](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Exits the app.

[Start Voice Sequence](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Here is a video demonstration of VOICE SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=VRe-0JPNwGU)

Starts the Voice Sequence with which you can make automatic voice calls with specified duration and pause. During this sequence the number of successful, blocked and dopped calls are dispalyed in INFO tab.

For phones that don't support automatic call hangup (like Google phones with security update from 05.05.2018) when it is time to end a call a message is showed to end call manually.

[Start Data Sequence](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Here is a video demonstration of DATA SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=8i-hYpXRer8)

Starts automatic data transfer sequence. It includes:

10 seconds ping

10 seconds upload

10 seconds download

pause (specified in Settings)

Note: If your Android version is 2.2 or earlier then the upload is until at least 128kB file is uploaded.

How to use:

Input the ping, upload and download URL in Settings.

Check DATA TEST in kml export settings to export statistics in kml

Start Data Sequence from Menu.

Observe the stats on INFO tab

The statistics are:

average ping

min ping

max ping

ping standard deviation

ping loss

upload bitrate

download bitrate

The statistics are exported in text logfile and in kml files if option DATA TEST is selected in kml export settings.

[Data Test](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Starts data test. It includes:

10 seconds ping

10 seconds upload

10 seconds download

Note: If your Android version is 2.2 or earlier then the upload is until at least 128kB file is uploaded.

How to use:

Input the ping, upload and download URL in Settings.

Select Menu - More - Data Test

[Start SMS sequence](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

SMS sequence is not available anymore due to Google policy for apps not to use SMS.

[Here is a video demonstration of SMS SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=vaBAsm_kybg)

Starts SMS sequence. It sends predefined number of SMS and tracks its success.

[Export Cellfile to kml](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Exports cellfile to kml, which can be opened with Google Earth. The exported file is in folder \cellfile

[Disable Map and GPS](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Disables the map view. Then the map view won't be updated

[Enable Map and GPS](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Enables the map view. This allows zooming and moving the map view.

[G-NetDiag](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens [G-NetDiag](http://www.gyokovsolutions.com/G-NetDiag/G-NetDiag.html) page where you can analyze your text log files.

[G-NetWorld](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens [G-NetWorld](http://www.gyokovsolutions.com/G-NetWorld/G-NetWorld.php) page, where you can share and view measurements made by other G-NetTrack users around the world.

[Upload file to G-NetWorld](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens [G-NetWorld file upload](http://www.gyokovsolutions.com/G-NetWorld/insertfile.php) page, where you can upload text log files to G-NetWorld service.

[Measurement Capabilities](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens [Phone Measurements Capabilities](http://www.gyokovsolutions.com/survey/surveyresults.php) page, where you can view different phone brands and models reporting capabilities.

[Export Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Export settings to text file, which can be loaded again. The exported file is in ht e app folder

[Import Settings](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Imports settings from previously exported settings file

[Load Cells](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Load cells from cellfile. If cells are already loaded it will reload them from cellfile.

[Refresh cell database](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Refrshes cell database from cellfile. Do this when cell information is changed and database needs to be updated.

[Redraw Cells](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Redraws cells. Use this to manually redraw cells when using option to visualize only surrounding cell and auto refresh of cells is not on.

[Load Route](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Loads a route from logfiles. Put the logfiles in folder [route] in app folder. Also tab delimited text file with two column headers "Longitude" and "Latitude" can be used. This will help when you want to follow predefined route. When option to follow route is on then colored leading points will be shown ahead on the route showing the direction you have to move.

Here is a demo video for route following - [https://youtu.be/qqg7VEFIcxw](https://youtu.be/qqg7VEFIcxw)

[Load Floorplan](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Loads floorplan image for indoor measurements. For details how to prepare floorplan see Floorplan section.

[Load Instant Floorplan](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

This is a faster way to loads floorplan image for indoor measurements. The image is shown at place with coordinates (0,0).

[Here is a video demonstration of instant floorplan load](https://www.youtube.com/watch?v=hg9WRzS8yB0)

[facebook page](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Opens G-NetTrack](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php) [facebook](https://www.facebook.com/gnettrack) page, where you can communicate with other G-NetTrack users.

[About](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Opens [G-NetTrack](http://www.gyokovsolutions.com/G-NetTrack%20Android.html) web page

### [Cellfile](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

If you have cell information you can create a cellfile and view the sites on the map. In order to do this create cellfile and put it into folder G_NetTrack_Logs/cellfile. Two types of cellfiles can be used:

The cellfile format is tab delimited text file with following columns:

tab delimited text cellfile

clf file

Recommended format is tab delimited text cellfile since it suppports more features (azimuth, layers, height etc...)

[Tab delimited text cellfile](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

The cellfile should be named cellfile.txt or [MCC][MNC].txt like 28401.txt

CELLNAME - name of the cell - you can put anything here

LAT - latitude in decimal format

LONG - longitude in decimal format

LAC - LAC of the cell - number

CELLID - CELLID of the cell - number

AZIMUTH - azimuth of the antenna - number. If you put 360, the cell will be shown as circle. If you want to change the size of the circle put values > 360. Then the circle radius will be value-360.

TECH - technology - 2G, 3G or 4G

NODE - for GSM is empty, for 3G is RNC and for 4G is eNodeB ID - this column is mandatory only for 4G. For 3G you can skip it if "LAC-CELLID" is unique

Optionally you can add the following columns. If you add them you can use this cellfile also with other tools on the site like G-NetTrack and G-NetEarth:

HEIGHT - antenna height in meters

TILT - antenna tilt in degrees - positive values are for downtilt and negative for uptilt

HORIZBEAM - horizontal beamwidth of the antenna

VERTBEAM - vertical beamwidth of the antenna

PSC - BSIC for GSM, primary scrambling code - for 3G, PCI for LTE

ARFCN - frequency channel (optional)

LAYER - up to 4 (1,2,3,4 ) layers per technology (2G/3G/4G) - with layer information you can make your map view show different cell layers with different colors. Use 1 for lower layer and 4 for higher layer. For example for operator with GSM900/1800, 4 UMTS frequencies and 2 LTE frequencies it will be: GSM900 - 1, GSM1800 - 2, UMTS F1 - 1, UMTS F2 - 2, UMTS F3 - 3, UMTS F4 - 4, LTE F1 - 1, LTE F2 - 2

INFO - Whatever is written there will be displayed in NEI tab when the cell is serving cell. Use semicolon ";" for new row.

Here is a sample [cellfile](http://www.gyokovsolutions.com/downloads/G-NetTrack/cellfile.txt).

[CLF cellfile](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

CLF cellfile is a format used with some network monitoring tools. It is a semicolon (;) delimited text file. The cellfile should be named cellfile.clf or [MCC][MNC].clf like 28401.clf.

If you want to use clf format for cellfile make sure that there is no cellfile.txt in the cellfile folder, cause then it will be used as cellfile.

The current supported format is clf 3.3.0. CLF format is not recommended. It is better to use tab delimited text file cause it contains more information.

|   |   |

| --- | --- |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

|   |   |

Here is a sample [clf cellfile](http://www.gyokovsolutions.com/downloads/G-NetTrack/28401.rar)

[Database](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Database can be used for fast loading of cells.

How to use:

Activate the feature - check

Settings - Sites - Show Sites

Settings - Sites - Use database

Set database options

Order by distance - when it is on it will guarantee showing closest cell. When it is off then loading will be faster.

Limit by distance - Read from database cells in [Distance limit] range. When this is on loading will be faster

To fill the celldatabase from cellfile

use MENU - Refresh cell database.

Once database is filled then loading

of cells from database is much faster

than loading from cellfile.

### [Logfile](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Download sample kml and text logfiles](http://www.gyokovsolutions.com/downloads/G-NetTrack/sample_logfiles.rar)

Here is description of logfile columns:

Timestamp - time of the measurement

Longitude - longitude of measurement

Latitude - latitude of measurement

Speed - speed at the time of measurement in km/h

Operatorname - name of the operator

Operator - MCC and MNC of the operator

CGI - Cell Global Identity of serving cell

Cellname - name of serving cell - from cellfile

Node - RNCID on 3G, eNodeBID on 4G

CellID - CELLID of serving cell

LAC - LAC of serving cell

NetworkTech - current technology - 2G, 3G, 4G

NetworkMode - current network mode

Level - RxLev on 2G, RSCP on 3G, RSRP on 4G in dBm

Qual - RxQual on 2G, ECNO on 3G, RSRQ on 4G

SNR - SNR (4G only)

CQI - CQI (4G only)

LTERSSI - RSSI

DL_bitrate - current downlink bitrate at the time of measurement

UL_bitrate - current uplink bitrate at the time of measurement

PSC - PSC on 3G, PCI on 4G

Altitude - altitude

Height - height over ground level, provided ground level altitude is set in Settings

Accuracy - GPS/Network accuracy of location

Location - G for GPS, N for Network accuracy

State - I (idle), V(voice), D(data)

PINGAVG - average ping result from data sequence

PINGMIN - min ping result from data sequence

PINGMAX - max ping result from data sequence

PINGSTDEV - standard deviation for ping statistic from data sequence

PINGLOSS - ping loss in percents

TESTDOWNLINK - average downlink bitrate from data sequence

TESTUPLINK - average uplink bitrate from data sequence

TESTDOWNLINKMAX - maximum downlink bitrate achieved during data sequence

TESTUPLINKMAX - maximum uplink bitrate achieved during data sequence

Test_Status - status of data sequence test

DataConnection_Type - Mobile or WiFi

DataConnection_Info - WiFi SSID when on WiFi

Layer - serving cell layer (from cellfile)

Filemark - filemarks saved during logging

Filemark - filemarks saved during logging

IMEI - device IMEI

Distance - distance from serving cell

Bearing - serving bearing

IP - device IP

TA - timing advance

Event - event name

Event details - event details

IMSI - device IMSI

MSISDN - device MSISDN

Serving time - serving cell serving time in seconds

CELLHEX - cell in hex format

NODEHEX - node in hex format

LACHEX - LAC in hex format

RAWCELLID - cellid in raw form

Version name - app version

Version code - app version code

Device - device name

Band - frequency band (L for 4G, U for 3G, G for 2G)

R8 - R10 - reserved parameters

NCellName1-6 - Neighbor cell name - from cellfile

NCellid1-6 - Neighbor CELLID

NLAC1-6 - Neighbor LAC

NCell1-6 - Neighbor CELLID on 2G, PSC on 3G, PCI on 4G

NRxLev1-6 - Neighbor level in dBm

NQual1-6 - Neighbor RSRQ on 4G

NDistance1-6 - distance to neighbor cell

NBearing1-6 - bearing to neighbor cell

### [How to prepare Floorplan](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

There are two options to load floorplan image: normal and instant. Using normal way you need image and index text file where you specify the location of image corners. The instant way is just using image and then the image is shown on location (longitude=0, latitude=0).

**Instant way to load floorplan**: Put floorplan image in G-NetTrack_Pro_Logs/floorplan. Then press Menu - Load instant floorplan. Select image and the image will be shown on map on location(longitude=0, latitude=0)

**Normal way to load floorplan**: Load floorplan from image files (jpg or png) located in G-NetTrack_Pro_Logs/floorplan folder. Index file index.txt describing edge locations also should be present in the folder

How to load floorplans:

Prepare image files for all floors. The image format must be jpg or png.

The floorplan image has to be oriented towards North. 

Prepare text file for geocoding. This means to tell the app where to put your images on the map. Create file index.txt with rows for each image and following content (tab delimited)

imagename longitudeSW latitudeSW longitudeNE latitudeNE

where SW and NE are South - West corner and North - East corner.

Here is an example:

Note that in the example above floor1.png and floor2.png are the names of the image files for the specific floor. Also do not forget that the format is tab delimited. You have to put tabs (not spaces) between the values.

In folder G_NetTrack_Pro_Logs/floorplan put the floorplan images and create text index file (index.txt) with rows for each image and following content (tab delimited)

Make sure you have no empty rows in index file.

Go to Menu - Load Floorplan. The floorplans will be shown on map and for each floorplan a kml file will be created to be used with Google Earth. Notice that you have to change the image location tag  if you copy kml file and intend to use it on your computer.

[Here you can download floorplan sample.](http://www.gyokovsolutions.com/downloads/G-NetTrack/floorplan.rar)

### [Dual SIM](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Dual SIM is available:

-for phones that use New API 17 functions and report both SIM information

-for older phones that use old API functions

If dual SIM is supported you can use all app features for both operators. In dual SIM mode the cellfile should have both operators celldata in it in order to see both serving cell and neighbor cell lines.

**New Dual SIM support:**

If in Settings - Calibration [Use old functions} is checked then several types of old dual SIM support is checked and if phone supports it on app restart you will see the message saying which type of dual sim is started.

Your phone has to report both SIM cards. You can check if your phone reports both SIM info by going to INFO tab and scroll to the bottom of it. Then check if there are 2 cells with mRegistered=YES. That means both SIM are reported. 

**Old Dual SIM support:**

If in Settings - Calibration [Use old functions} is not checked then dual sim support based on new API 17 functions is started on app restart.

Automatically first Gemini dual sim support is checked and if not successfull several vendor specific types of dual sim supports are checked. You can skip Gemini support check by checking SETTINGS - DUAL SIM - OLD DUAL SIM SETTINGS - Disable Gemini Dual Sim support.

You can manually input the needed dual sim class for your phone if you select [Use specific classname] and input the classname value in [Dual SIM classname]. Classname example - com.mediatek.telephony.TelephonyManagerEx

### [Known issues](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

**Measurements**

Not all the phones are capable of reporting the measurements:

CELLID and LEVEL - if you see that LEVEL is less than -200 that means that your phone does not report anything and can not be used for measurement purposes.

RXQUAL, ECNO, PSC is not reported by all phones.

Neighbor cells are not reported by all phones.

Some phones do not update values for levels or serving cell.

**If your phone manufacturer has not implemented correctly needed functions for reporting there is still hope.

Try this:

Go to Settings - Other and check 'Use old functions' for serving and neighbor cells. This will make phone to use old functions, which may be correctly implemented by phone manufacturer.

Go to Settings - Other and check 'Force updates'. This will help if your level and cell values are correct, but are not updated.

If nothing of above helps you have to update your phone software or wait for such update if it is not available at the moment.**

Check [Phone Measurement Capabilities](http://www.gyokovsolutions.com/survey/surveyresults.php) for list of phones and measurements that they report.

If your phone does not report some measurements the only thing you can do is to search for software update from device manufacturer. There is no possibility a change in app to make your phone to report properly.

**Licensing**

If you have problem with app licensing getting error message that app is not licensed then check [here](http://www.gyokovsolutions.com/licensing.html).

[Tips & Tricks](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

[Working with big number of cells in cellfile](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

So there are two problems when you want to load many cells:

You have to read lot of info from text file and reading from text cellfile is not fast

You have to visualize a lot of cells on map and the map can not handle too many objects..

Database addresses problem 1. You can use database as fast reading option. Database is preloaded with cells from cellfile. In database options set quite big range like 200km if you will travel 100km to make sure you will read from database all needed cells at once. There should not be a need to reload cells from database during measurement.

Then comes problem 2 - visualizing of cells. This is handled by limiting range of visualized cells on map [SETTINGS - SITES - Visualize onlu sites in range] and [SETTINGS - SITES - Max visualized cells]. Then you can use automatic redraw of cells while you travel [SETTINGS - SITES - Auto refresh sites in range]. There is option to do it manually - MENU - Redraw cells. During this cells are deleted from map and new cells are showed on map. [SETTINGS - SITES - Range of visualized sites] has to be smaller like 5-10km in urban areas. If you are travelling rural areas you can set it higher like 30km cause there are not so many sites in rural areas and sometimes serving cell can be far away. The auto redraw of cells is done automatically when you travel half of range of visualized cells [SETTINGS - SITES - Range of visualized sites].

[How to improve G-NetTrack map performance.](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

Map performance depends on number of objects drawn on the map. The objects are:

Cells - it include two types of objects: line and cell name

Log points - the points drawn each time the location is changed

Route points - the points of loaded predefined route (Pro version only)

When the number of objects becomes big (too many cells in cellfile, too long log, or too long route) then the map performance deteriorates and the app is slowed. This depends on the phone capabilities (CPU, RAM). It depends on the phone but generally the Google map cannot handle well more than 5000 objects. Bear in mind that each cell consists of two objects - line and name. The map performance can be improved by taking the following actions to reduce the number of objects without losing the app functionality.

Reduce the number of cell objects.

Loading of cellfile has two stages:

Phase 1. Loading cells in memory - the cell information is read from cellfile, loaded in memory and used by the app for serving and neighbor cells information.

Phase 2. Visualizing cells on map - the cells are visualized on map. It depends on the phone but generally the Google map cannot handle well more than 5000 objects. So for improving map performance you can control it with:

option "Max visualized cells" (default 1000) in Settings-Sites. This is the max number of cells that will be visualized from all cells that are loaded in memory. If you want to increase this number you can use the following features below to achieve better map performance.

option "Visualize only sites in range" (default - YES) and set [range of visualized cells] (default 2000m). This way you make sure that closest sites will be visualized. For [range of visualized cells] select values that will guarantee that number of cells in this range is not bigger than [Max visualized cells]. In this way no surrounding cell will be missing on map.

uncheck option "Show cell names". Then cell names won't be shown which will reduce the number of map objects and will improve map performance.

use option "Show dots for cells" this will draw dots instead lines for cells which improves map performance.

Reduce the number of log points - Change [Log Reduction Factor] in Settings - this determines when a log point is drawn on the map. If the value is default (1) then every location change bigger than 15m is drawn as log point. If you put value N bigger than 1, then every N-th log point is drawn on the map which results in less log points and improved map performance.

Note that the number of samples in text and kml log is not affected and stays the same.

Reduce the number of route points - when predefined route is loaded it can contains a lot of points which are not necessary and can be reduced without losing the route direction. Change Route Reduction Factor] in Settings - this determines when a route point is drawn on the map. If the value is default (1) then every route point is drawn. If you put value N bigger than 1, then every N-th log point is drawn on the map which results in less log points and improves the map performance.

This manual in pdf format - [http://www.gyokovsolutions.com/manuals/G-NetTrack_Pro-manual.pdf](http://www.gyokovsolutions.com/manuals/G-NetTrack_Pro-manual.pdf)

### [Contacts](http://www.gyokovsolutions.com/manuals/G-NetTrackpro_manual.php)

email: [info@gyokovsolutions.com](mailto:info@gyokovsolutions.com)

G-NetTrack [facebook](https://www.facebook.com/gnettrack) page  

Contacts: [info@gyokovsolutions.com](mailto:info@gyokovsolutions.com)

Copyright (c) 2010 Gyokov Solutions. All rights reserved.