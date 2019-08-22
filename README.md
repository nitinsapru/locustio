# Locust - User load testing application
This repository is for code, documentation &amp; sample related to Locust (load testing application) &amp; its use cases.

<h3><b>Installation & Setup for Windows Host:</b></h3>

1. Make sure you are running Python 2.7 and above to make sure that there are no versioning issues with Locust.
2. If you are not having a running Python 2.7 + version on your host, please download the same from <a href="https://www.python.org/downloads/">here</a>.
3. Once you have downloaded & installed python , open any of the python IDE's like Visual Studio Code, Notepadd ++ , Anaconda etc, to install locust library for Python.
4. On completion of download and installation of the module, the application is ready to be used on your local host.
5. Running locust on windows platform with Python 2.7+ version can simply run the command : <i><b>pip install locustio</b></i> in the terminal & it will install all packages associated with locust. 

<h3><b>Using & Running Locust:</b></h3>
1. Write the script using Python as a language. The framework is very much similar to JS or .NET frameworks.<br>
2. Once the script is ready & the above installation and setup activities are completed, please us the below mentioned command from the local CMD to execute the below mentioned command.

<b>locust -f {Full file path}.py --host {http/https hostname}</b>

<b>Output of the command execution:</b><br><br>

<i>C:\Users\Admin>locust -f E:\python\locust_sample_dotnet_anonymous_auth.py --host https://localhost:44361/ <br>
[2019-08-21 23:33:37,273] DM1BX001/INFO/locust.main: Starting web monitor at *:8089 <br>
[2019-08-21 23:33:37,273] DM1BX001/INFO/locust.main: Starting Locust 0.11.0 <br><i>
