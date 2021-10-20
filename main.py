#!/user/bin/python37all
print(""" 
Content-type:text/html\n\n
<html>
<head>
<title>LED brightness</title>
</head>
<body>
<div style="width:600px;background:#AAAAFF;border:1px;text-align:center">
<br>
<form action="/cgi-bin/labfour.py" method="POST">
<input type="submit" value="create a new page">
<input type="radio" name ="option" value="LED_A" checked> LED A <br>
<input type="radio" name ="option" value="LED_B"> LED B <br>
<input type="radio" name ="option" value="LED_C"> LED C <br>
<input type="range" name="Brightness" min="0" max="100" value="50"/><br>
<input type="submit" value="Submit"
</form>
</div>
</body>
</html>
""")
