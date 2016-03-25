<!DOCTYPE html>
<html>
	<head>
		<title>Logga in</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="../static/css/main.css">
	</head>
	<body>
        <header>
            <h1>Questway</h1>
            <nav>
                <a class="options" href="">Logga in</a>
                <a class="options" href="">Registrera</a>
                <a class="options" href="">Om oss</a>
            </nav>
        </header>
        <div id="content">
        <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
            <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->
		<form name="logIn" id="logIn" method="post" action="/do_login">
            <h3>Logga in</h3>
			<!--<label for="username">Användarnamn</label>-->
			<input placeholder="Användarnamn" type="input" name="username" id="username" value="">
			<!--<label for="password">Lösenord</label>-->
			<input placeholder="Lösenord" type="password" name="password" id="password" value="">
			<input id="logInButton" type="submit" value="Logga in">		
		</form>
		<p id="error"></p>
		<a href="/" id="back-button">Tillbaka</a>
        </div>
        <footer>© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>