<!DOCTYPE html>
<html>
<<<<<<< HEAD
<<<<<<< Updated upstream

    % include('head.tpl')

=======
	<head>
		<title>Skapa konto</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0">
		<link rel="stylesheet" type="text/css" href="../static/css/main.css">
	</head>
>>>>>>> Stashed changes
=======
    % include('head.tpl')
>>>>>>> origin/master
	<body>
        <div class="wrapper">
            <header>
                <h1>Questway</h1>
                <nav class="menu">
                    <a href="/login">Logga in</a>
                    <a href="/create" class="currentMenuItem">Registrera</a>
                    <a href="">Om oss</a>
                </nav>
            </header>
<<<<<<< HEAD
            <div id="content">
            <form name="create_employer" id="create_employer" method="post" action="/do_create_employer" style="width:50%; margin: 0 auto; float: left;">
                <h3>Skapa profil | Uppdragsgivare</h3>
                <label for="company_name">Företag</label>
                <input placeholder="Företagsnamn" type="input" name="company_name" id="company_name" value="">
                <label for="org_nr">Org.nr</label>
                <input placeholder="Org.nr" type="input" name="org_nr" id="org_nr" value="">
                <label for="first_name">Förnamn</label>
                <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
                <label for="last_name">Efternamn</label>
                <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">
                <label for="email">Mejl</label>
                <input placeholder="Mejl" type="input" name="email" id="email" value="">
                <label for="password">Lösenord</label>
                <input placeholder="Lösenord" type="input" name="password" id="password" value="">
                <input id="logInButton" type="submit" value="Skapa konto">
            </form>

            <form name="create_student" id="create_student" method="post" action="/do_create_student" style="width:50%; margin: 0 auto;">
               <h3>Skapa profil | Student</h3>
               <label for="first_name">Förnamn</label>
               <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
			   	<label for="last_name">Efternamn</label>
                <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">
=======
                <nav>
                    <a class="options" href="/login">Logga in</a>
                    <a class="options" href="/">Registrera</a>
                    <a class="options" href="">Om oss</a>
                </nav>
            </header>
=======

>>>>>>> origin/master
            <div id="content">
                <h3>Skapa profil som:</h3>
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->

<<<<<<< HEAD
                <a class="choicereg" id="employreg" href="../views/create_employer.tpl"><h3>Uppdragsgivare</h3></a>
>>>>>>> Stashed changes

                <a class="choicereg" id="studentreg" href="../views/create_student.tpl"><h3>Student</h3></a>

            <p id="error"></p>
=======
                <a class="choicereg" id="employreg" href="../views/create_employer.tpl">
                    <h3>Uppdragsgivare</h3>
                </a>
                
                <a class="choicereg" id="studentreg" href="../views/create_student.tpl">      
                    <h3>Student</h3>
                </a>
               
            <p id="error">
                </p>
>>>>>>> origin/master
            </div>
            <div class="push">
            </div> <!-- Är till för att footer ska hamna längst ner, ta ej bort --><!--Kolla på position:fixed istället-->
        </div>
        <footer>© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
