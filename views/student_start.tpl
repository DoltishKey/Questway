<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
	<body>
        <header>
            <nav class="menu">
                <a class="menuButton" href="">Uppdrag</a>
                <a class="menuButton" href="">Profil</a>
                <a class="menuButton" href="/log_out">Logga ut</a>
            </nav>
        </header>
		<content>
            <h1>Admin, {{user}}</h1>
            <h2>Du är inloggad som {{level}}</h2>
            <a href="/log_out">Logga ut</a>
            <a href="/">Till start</a>
        </content>
	</body>
</html>