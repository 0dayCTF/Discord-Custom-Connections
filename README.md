# Discord Custom Connections
Add custom connections to your Discord profile!
<h2>Submitting the PUT request</h2>
<p>
  ∙ Navigate to Discord in the browser to find your authorization token <a href="https://discordhelp.net/discord-token">(How To Find Token)</a>
  <br>
  ∙  Change the token in the request to your own, and add some random integers after <i>/connections/battlenet/</i><b>HERE</b> 
  <br>
∙ Using python, execute <b>CustomConnections.py</b> (make sure you installed requests eg: pip install requests)
<br>
∙ To remove, just change the script to <b>DELETE</b> instead of <b>PUT</b>, make sure you use the same integers in the request!
<br>
<center><h3>Feel free to test other endpoints, "leaugeoflegends" & "skype" appear to work as well. </h3> 
  <br><i>Be careful of the "contacts" endpoint, it will cause your Discord to crash until removed!</i></center>
</p>
<br>
<br>
<h2>PoC</h2>
<img src="https://i.imgur.com/cvzG95Q.png">
<br>
<h3><i>2/16/2020 | Lew fixed the protocol, to work with the new patch</i></h3>
<i>I will be adding some more methods in the future, check back for an update</i>
<br>
