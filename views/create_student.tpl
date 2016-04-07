<!DOCTYPE html>
<html>
	<head>
		<title>Skapa konto</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="../static/css/main.css">
	</head>
	<body>
        <div class="wrapper">
            <header>
                <h1>Questway</h1>
                <nav>
                    <a class="options" href="/login">Logga in</a>
                    <a class="options" href="">Registrera</a>
                    <a class="options" href="">Om oss</a>
                </nav>
            </header>
            <div id="content">
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->

            <form name="create_student" id="create_student" method="post" action="/do_create_student" style="width:50%; margin: 0 auto;">
               <h3>Skapa profil | Student</h3>
               <label for="first_name">Förnamn</label>
               <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
			   	<label for="last_name">Efternamn</label>
                <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">

                <label for="program">Utbildning</label>
                <select name="program" id="program" value="">
					<option value="1">Informationsarkitekt</option>
					<option value="2">Systemutvecklare</option>
					<option value="3">App</option>
				</select>

                <label for="year">Årskurs</label>
                <input placeholder="Årskurs" type="input" name="year" id="year" value="">
                <label for="email">Mejl</label>
                <input placeholder="Mejl" type="input" name="email" id="email" value="">
                <label for="password">Lösenord</label>
                <input placeholder="Lösenord" type="input" name="password" id="password" value="">
                <input id="logInButton" type="submit" value="Skapa konto">
            </form>
            <p id="error"></p>
            </div>
            <div class="push"></div> <!-- Är till för att footer ska hamna längst ner, ta ej bort --><!--Kolla på position:fixed istället-->
        </div>
        <footer>© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
