<!DOCTYPE html>
<html>
	<head>
		<title>Profil {{student_id}}</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="../static/css/main.css">
	</head>
	<body>
		<header>
			<h1>Questway</h1>
			<nav>
				<a class="options" href="/login">Logga in</a>
				<a class="options" href="">Registrera</a>
				<a class="options" href="">Om oss</a>
			</nav>
		</header>
		<main>
			<h1>Hello World!</h1>
			<h2>My ID is {{student_id}}</h2>
		</main>
		<footer style="position: fixed; bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>