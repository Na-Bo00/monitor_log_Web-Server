# Web-Server monitoring and logging
Monitor and log the availability of an URL.

## Requirements
The application should be able to test the availability of a URL. 
To achieve this, a user should start the program and enter a URL to a HTML page followed by Enter.
Every 30 seceonds, the program checks if the URL is still available and writes the result to a local log file.
A user can stop the program by presseing **ANY** key available on the keyboard. 

### Return Info to the user:
+ http://example/login.html is being monitored and logged, press any key to exit...

### Output example of the log file:
- 19-Nov-2022 10:15:00 - http://example/login.html -> reachable!
- 19-Nov-2022 10:15:30 - http://example/login.html -> reachable!
- 19-Nov-2022 10:16:00 - http://example/login.html -> not reachable!
- 19-Nov-2022 10:16:30 - http://example/login.html -> reachable!

### Additional notice:
This program has no GUI because it was developed as a console application.

## Contact
If you have any questions, face any problems or have any improvment suggestions do not hesitate to open a new [issue](https://github.com/Na-Bo00/monitor_log_Web-Server/issues/new).

---
Made by Na-Bo00 | Copyright (c) Na-Bo00

<!--Made by Na-Bo00 ![Na-Bo00-Logo.jpg](Na-Bo00-Logo.jpg "Na-Bo00-Logo")--!>
<div><img alt="Na-Bo00-Logo.jpg" src="https://github.com/Na-Bo00/monitor_log_Web-Server/blob/main/Na-Bo00-Logo.jpg" width="100" height="35" /></div>
