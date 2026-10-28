# G-NetTrack Pro Manual - Gyokov Solutions

G-NetTrack Pro Manual

### [Introduction](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

**G-NetWiFi** is a WiFi network monitor and drive test tool for Android OS devices. It allows monitoring and logging of WiFi network parameters without using specialized equipment. It's a tool and it's a toy. It can be used by professionals to get better insight on the network or by radio enthusiasts to learn more about wireless networks. It can be used even if you want just to make easy representation of your travelled route.

[Here is a video demonstration of G-NetWiFI Pro](https://www.youtube.com/watch?v=YElGsdT1nDQ)

G-NetWifi can be used in outdoor and in indoor environment with loading of floorplans.

The main features of G-NetWiFi are:

measuring of WiFi network parameters

logging of measured values in text and kml files

displaying measured values on map view

loading of cellfile and displaying WiFi access points and serving cell line on map view

**G-NetWiFi Pro - additional features.

WiFi scan logging

Data test (ping, upload, download)

Data sequence

Scan only configured WiFi

Change WiFi AP color

Extended kml export

Change level legend colors

Change log parameters (distance, time)

Predefined routes load

Auto add new WiFi AP to cellfile

Import/export app settings

Extended text logging

Change app folder

Log reduction factor

----------------------------------------------------------------------------------------------------------------------------------**

This manual describes the information available, the settings and the actions that can be done using G-NetWiFi.

### [Tabs](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

There are five tabs with different information - WiFi, SCAN, MAP, INFO and DRIVE. The information displayed on each tab is

[2.1 WiFi Tab](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

WiFi tab shows network and geographical information. It also shows history log of the serving cells. The shown information is:

SSID - the name of WiFi access point

BSSID

IP

Frequency

Channel

Link speed

RSSI - the current signal strength in dBm.

Longitude - current location longitude in decimal format

Latitude - current location latitude in decimal format

Speed - current speed in kmph.

Accuracy - the accuracy with which the location is determined. Location determination could be based on GPS or Network (using Google location service - using serving and neighbor cells or WiFi networks)

Height - the difference between Altitude and Ground values

Altitude - the GPS measured altitude

Ground - the ground level height - this is ajustable in settings.

UL - the current uplink data transfer speed in kbps

DL - the current downlink data transfer speed in kbps

Data - the used data network

Serving Time - the current serving AP time in seconds. If cellfile is used this line also shows the serving cell name and cell layer.

Serving cell history table - this table shows history log of serving cell changes with time of the change and level at which this change happened.

[2.2 SCAN Tab](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

SCAN tab shows information about neighbor cells measurements. It consists of two tables:

Serving cell table - shows information about current serving cell id and level.

Neighbor cells table - shows information about the current neighbor cells and their levels.

[2.3 MAP tab](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

MAP tab shows geographical view of hte measurements and mobile network basestations.

In the first row there is information about current WiFi AP.

On the second row there is information about the distance to serving cell and bearing to it. This information is available only if cellfile with networks cell information is loaded. On this row also is information about the GPS - if it has fix (green color) or not (red color).

The map shows the surrounding area view and thematic map of selected measurement (LEVEL, CELL, DL bitrate, UL bitrate, SPEED).

There are four buttons available:

first button is for changing the thematic map measurement

"Export" button - exports the current thematic map of the selected measurements in kml format. This is useful for on the fly recording of measurement if the logging function has not been turned on.

"Screenshot" button - saves the snapshot of the current view - useful for on the fly saving of image representation of the measurements.

"Clear" button - clears the view - if there are a lot of points, it can slow the map view and then is good to clear the view.

[2.4 INFO tab](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

The INFO tab provides following information:

Log Status - shows if the log recording has been started or not

Serving WiFi

Best Configured WiFi - the AP with highest level. The AP is known and configured in the phone.

Data Sequence Status - status of data sequence if running and the results (Ping stats, DL/UL bitrates)

SD Card - if sd card storage is available

App folder - the used root folder for exported files - the folder where G-NetTracl_Logs folder stays

Cellfile - the loaded cellfile name

G-NetWiFi version - current version of the app

G-NetWiFi code - number representation of the current app verson

Android SDK - the Android OS version number

Device - device name

Brand - device brand

Device Manufacturer - manufacturer of the device

Build Number - device software build

[2.5 DRIVE tab](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

DRIVE tab represent the main serving cells information in comfortable format with big font letters

### [Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html) - the settings are similar to G-NetTrack Pro and video examples from it are used in this manual

Settings are activated via Menu - Settings. There are several group of settings, which are related to different app features:

[INDOOR Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

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

[MAP Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Map Satellite View - switches satellite/street view of the map

Map in background - when active the GPS stays on while the app is in the background when the log is not started

Map Center - switches on/off automatic centering of the map around current location

Point Size - size of the point on map view

Serving Cell Font Size - font size of the serving cell on Map view

Cells Font Size - font size of the cells on Map view

Serving Cell Thickness - thickness of the serving cell on Map view

Cells Thickness - thickness of the cells on Map view

Ground Level - sets the ground level altitude. When set different than 0 Height in CELL tab shows the height above this ground/street level

Log reduction factor - when this value (N) is bigger than 1 then every N-th measurements is shown on map. This does not impact the logfile

[DATA SEQUENCE Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

[Here is a video demonstration of DATA SEQUENCE with G-NetTrack Pro](https://www.youtube.com/watch?v=8i-hYpXRer8)

DATA SEQUENCE allows test of data transfer.

Ping - include PING in data sequence

Ping URL - the URL for ping test. The format is like www.xxxxxxxxxxxxxx.com or 10.100.1.101

Upload - include UPLOAD in data sequence

Upload URL - the URL for upload test. The format should start with http:// and is like http://www.xxxxxxxxxxx.com.

Download - include DOWNLOAD in data sequence

Download URL - the URL for ping test. The format should start with http:// and is like http://www.xxxxxxxxxxx.com/downloadedfile.mp3. It is recommended to set bigger file in order to achieve bigger download speed.

Pause between tests - pause between test cycles

Log bitrates only during data test - when this is checked current DL and UL bitrates will be logged only when data sequence is active. Useful when you want to view easily the maximum available bitrates

Multithread - when checked multiple simultaneous connections will be used for upload and download in Data Test and Data Sequence. Using several threads increases the bitrates.

Number of threads - the number of threads to be used ([Multithread] should be checked). Set number of simultaneous threads more than 1 and less or equal to number of phone CPU.

[KML EXPORT Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

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

PSC - UMTS primary scrambling code of the serving cell

NEIGHBOR CELLS - separate file for cellid and level for each of the first 6 neighbor cells measured

CELLFIND - when active this will activate a CELLFIND feature which shows the serving cell location determined by Google location service, based on the cellid measurements. In order this feature to be available you must have mobile network data connection on. Turn your WiFi off in order to prevent location determination based on WiFi networks. In kml file there is information about the cell location and accuracy. It can help to gain insight on cell size (bigger when accuracy is greater number) and location.

DATA TEST - 4 kml files for DATA SEQUENCE statistics - average ping, ping loss, upload bitrate and download bitrate

Use height in kml - when this is on, the points in the kml file will show above ground level as Height in CELL tab shows.

Use short kml format - reduces the kml size showing only the respective measurement in the information baloon.

KML Point Size - size of kml dot in kml export file.

Application folder - set the root folder for export files. The folder must exist, otherwise the default folder is used. Check the [App folder] in INFO tab in order to see if the correct folder was chosen. If you want to use external SD card you have to put "/sdcardname" - check with some file manager the name of your external SD card.

[SITES Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Show Sites - requires cellfile. When it is on the list of cells from cellfile will be loaded at the program start. Requires restart of the app.

Show Serving Line - shows a line between current location and srving cell location

Show Cell Names - shows cell names in map view

Visualize only sites in range - loads all the cells, but visualize only sites in specified range - usefull when the cellfile is big and the map view is slowed down because the big number of cells

Auto refresh sites in range - the surrounding sites will be refreshed on location change when [Visualize only sites in range] is selected.

Range of loaded sites - range in meters around current location of sites to be loaded

Load only sites in range - load only closest sites within specified range - usefull when the cellfile is big and the map view is slowed down because the big number of cells

Add unknown cells - when this option is on the new cells are automatically added to cellfile. If you have no cellfile and both [Show Sites] and [Add unknown cells] are on, the app will create new cellfile and when the log is on it will start filling it with new cells.

[LEVEL Thresholds Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Specifies the level thresholds settings for LEVEL kml export.

[LEVEL Colors Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Specifies the level colors settings for LEVEL kml export.

[LOG PARAMETERS Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Time Interval - the interval in seconds between writing record in the log if the location is not changed or cellid is not changed - default 300s, lower values will allow more frequent recording of fluctuations, higher values will make log files smaller and save battery

Distance Interval - the distance interval in meters between writing record in the log when the position is changed - default value 15m, lower values will increase point density, but will use more battery

GPS refresh time interval - time interval between GPS updates

[AUTOMATION Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Auto log on app start - auto start logging when the app is started

Auto VOICE SEQUENCE - auto start VOICE SEQUENCE on app start

Auto DATA SEQUENCE - auto start DATA SEQUENCE on app start

Auto start app on boot - auto start app on phone boot

[ROUTE Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Route color - color of the route

Route size - point size of route

Show direction - draw direction on route

Route reduction factor - when this value N is bigger than 1 every Nth point of the route is shown on map

[OTHER Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Screen orientation - sets the screen orientation

Best Configured Wifi - when selected your phone will automatically reselect the best WiFi AP that is configured

Auto configure free WiFi - when this is checked the free WiFi that are detected by the phone will be automatically configured and used

Auto screen on - while the log is active if the screen is turned off incidentally (with POWER button) it will be turned automatically on again.

### [Actions](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

[Start Log](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Starts the logging. During this the text and kml export files are created in G-NetTrack_Logs folder on main phone storage. The measurements kml files that are created can be selected in Settings. A record is put in log on change of position with specified distance interval, change of cellid or each specified time interval if there is no change of position or celld. Time and distance intervals can be set in Settings.

When the logging is activated the app will lock your GPS and screen on and the screen will remain lit during the logging. In order not to interrupt logging you have to not switch the device screen off. The phone could be locked, but the screen should be on.

[Pause Log](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Pauses the log.

[Resume Log](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Resumes the log.

[End Log](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Finishes the log.

[Add Filemark](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Adds the filemark (note) to the file. The filemarks are visible in text logfile and filemarkers.kml file.

[Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Opens the settings page.

[Exit](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Exits the app.

[Start Data Sequence](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

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

[Data Test](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Starts data test. It includes:

10 seconds ping

10 seconds upload

10 seconds download

Note: If your Android version is 2.2 or earlier then the upload is until at least 128kB file is uploaded.

How to use:

Input the ping, upload and download URL in Settings.

Select Menu - More - Data Test

[Export Cellfile to kml](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Exports cellfile to kml, which can be opened with Google Earth. The exported file is in folder \cellfile

[Disable Map and GPS](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Disables the map view. Then the map view won't be updated

[Enable Map and GPS](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Enables the map view. This allows zooming and moving the map view.

[Export Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Export settings to text file, which can be loaded again. The exported file is in ht e app folder

[Import Settings](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Imports settings from previously exported settings file

[Load Route](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Loads a route from logfiles. Put the logfiles in folder [route] in app folder. Also text file with column headers "Longitude" and "Latitude" can be used. This will help when you want to follow predefined route.

[Load Floorplan](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Loads floorplan image for indoor measurements. For details how to prepare floorplan see Floorplan section.

[Load Instant Floorplan](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

This is a faster way to loads floorplan image for indoor measurements. The image is shown at place with coordinates (0,0).

[Here is a video demonstration of instant floorplan load](https://www.youtube.com/watch?v=hg9WRzS8yB0)

### [How to prepare Floorplan](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

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

[facebook page](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

[Opens G-NetTrack](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html) [facebook](https://www.facebook.com/gnettrack) page, where you can communicate with other G-NetTrack users.

[About](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

Opens [G-NetTrack](http://www.gyokovsolutions.com/G-NetTrack%20Android.html) web page

### [Cellfile](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

If you have cell information you can create a cellfile and view the sites on the map. In order to do this create cellfile and put it into folder G_NetTrack_Logs/cellfile. Two types of cellfiles can be used:

The cellfile format is tab delimited text file with following columns:

tab delimited text cellfile

clf file

Recommended format is tab delimited text cellfile since it suppports more features (azimuth, layers, height etc...)

[Tab delimited text cellfile](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

If you have cell information you can create a cellfile and view the sites on the map. In order to do this create cellfile and put it into folder G_NetWiFi_Logs/cellfile.

Here is a sample cellfile: [http://www.gyokovsolutions.com/downloads/G-NetWiFi/cellfile.txt](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttp://www.gyokovsolutions.com/downloads/G-NetWiFi/cellfile.txt%26sa%3DD%26usg%3DAFQjCNHx_e-hPLZeaMDGE1F5IZqypoXmGg&sa=D&usg=AFQjCNF1OhGrrc7YxT5nRrLLaJPktCGM5w)

NAME - name of the cell - you can put anything here

LAT - latitude in decimal format

LONG - longitude in decimal format

SSID

BSSID

FREQ

AZIMUTH - azimuth of the antenna - number. If you put 360, the cell will be shown as circle. If you want to change the size of the circle put values > 360. Then the circle radius will be value-360.

HEIGHT - antenna height in meters

INFO - Whatever is written there will be displayed in NEI tab when the cell is serving cell. Use semicolon ";" for new row.

Here is a sample [cellfile](http://www.gyokovsolutions.com/downloads/G-NetTrack/cellfile.txt).

### [Contacts](https://www.gyokovsolutions.com/manuals/gnetwifipro_manualcontent.html)

email: [info@gyokovsolutions.com](mailto:info@gyokovsolutions.com)

G-NetTrack [facebook](https://www.facebook.com/gnettrack) page