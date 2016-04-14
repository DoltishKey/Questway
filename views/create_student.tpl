<!DOCTYPE html>
<html>
	% include('head.tpl')
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
            <div id="content">
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->

            <form name="create_student" id="create_student" method="post" action="/do_create_student">
               <h3 class="form_head" id="studentform_Title">Skapa profil | Student</h3>
                
                <div class="form_labels">
                    <label for="first_name">Förnamn</label>
                    <br>
                    <label for="last_name">Efternamn</label>
                    <br>
                    <label for="program">Utbildning</label>
                    <br>
                    <label for="year">Årskurs</label>
                    <br>
                    <label for="email">Mejl</label>
                    <br>
                    <label for="password">Lösenord</label>
                </div>
                
                <div class="form_inputs">
                    <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
                    <br>
                    <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">
                    <br>
                    <select name="program" id="program" value="">
                        <option value="1">Informationsarkitekt</option>
                        <option value="2">Systemutvecklare</option>
                        <option value="3">App</option>
				    </select>
                    <br>
                    <input placeholder="Årskurs" type="input" name="year" id="year" value="">
                    <br>
                    <input placeholder="Mejl" type="input" name="email" id="email" value="">
                    <br>
                    <input placeholder="Lösenord" type="input" name="password" id="password" value="">
                </div>
                <input class="create_account" id="logInButton" type="submit" value="Skapa konto">
               <!-- 
               <label for="first_name">Förnamn</label>
               <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
                <br>
                
			   	<label for="last_name">Efternamn</label>
                <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">
                <br>

                <label for="program">Utbildning</label>
                <select name="program" id="program" value="">
					<option value="1">Informationsarkitekt</option>
					<option value="2">Systemutvecklare</option>
					<option value="3">App</option>
				</select>
                <br>
                
                <label for="year">Årskurs</label>
                <input placeholder="Årskurs" type="input" name="year" id="year" value="">
                <br>
                
                <label for="email">Mejl</label>
                <input placeholder="Mejl" type="input" name="email" id="email" value="">
                <br>
                
                <label for="password">Lösenord</label>
                <input placeholder="Lösenord" type="input" name="password" id="password" value="">
                
                <input id="logInButton" type="submit" value="Skapa konto">
                <br>
                -->
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
