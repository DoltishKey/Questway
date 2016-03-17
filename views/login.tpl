<!DOCTYPE html>
<html>
	<head>
		<title>Logg in</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="/static/css/main.css">
	</head>
	<body>
		<form name="logIn" id="logIn" method="post" action="/do_login">
			<label for="username">Användarnamn</label>
			<input type="input" name="username" id="username" value="">
			<label for="password">Lösenord</label>
			<input type="password" name="password" id="password" value="">
			<input type="submit" value="Logga in">		
		</form>
		<p id="error"></p>
		<a href="/">Tillbaka</a>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>