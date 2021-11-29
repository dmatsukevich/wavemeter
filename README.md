# wavemeter
A web interface for [Toptica / HighFinesse / Angstrom](https://www.highfinesse.com/en/wavelengthmeter/index.html
) wavemeter with a fiber switch option.

Uses Python2 under Windows. The program starts a simple python web server at the port 8000 to monitor wavelength of the lasers via a web browser.
The main wavemeter program should be already running.

Usage:
python2 http.py

Some special URLs:   
/index.html -- a simple interactive web page for wavelength monitoring   
/sse.html -- stream of wavelength measurement data. All new measurement results are added here in real time   
/wavemeter.html -- current value of wavelength for all the wavemeter channels.   

If the server refuses to start, make sure that the path to the wavemeter dll in the wavemeter.py file is specified correctly.
The default is WinDLL("C:\Windows\System32\wlmData.dll")
