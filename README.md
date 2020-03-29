# Discord Custom Connections
Add custom connections to your Discord profile!
<h2>Using the exploit:</h2>

First Navigate to Discord in the browser to find your [authorization token](https://discordhelp.net/discord-token)

* On Windows:
  - Download and extract the `win-gui.zip` file
  - Double click on `exploit.bat`
  - The GUI will start, allowing you to add connections!
* On Linux:
  - Download and extract the `linux-gui.zip` file
  - Open a terminal inside the directory (Right Click -> Open in terminal)
  - Type in `./exploit` and hit Enter
  - The GUI will start, allowing you to add connections!

<h2>Alternatively:</h2>
If you prefer to do it manually:

* Download the `Python-Code/CustomConnections.py` file
* Navigate to Discord in the browser to find your [authorization token](https://discordhelp.net/discord-token)
* Using python, execute CustomConnections.py (make sure you installed requests eg: pip install requests)
* To remove, just change the script to <b>DELETE</b> instead of <b>PUT</b>, or just remove from Discord manually in your settings!
  
<center><h3>Feel free to test other endpoints, "leaugeoflegends", "skype", and "battlenet" appear to work! </h3> 
  <br><i>Be careful of the "contacts" endpoint, it will cause your Discord to crash until removed!</i></center>
</p>
<br>
<h2>PoC</h2>
<img src="https://i.imgur.com/cvzG95Q.png">
<br>
<i>I will be adding some more methods in the future, check back for an update</i>
<br>

