<!DOCTYPE html>
<html lang="sv">
    
    %include('head.tpl')
    
	<body>
        <header>
            <div class="wrap">
                <h1>Questway</h1>
                <nav class="menu">
                    <a href="/login" class="currentMenuItem">Logga in</a>
                    <a href="/create">Registrera</a>
                    <a href="">Om oss</a>
                </nav>
            </div>
        </header>
        <div class="wrapperLogin">
            <div class="wrap">
                <form name="logIn" id="logIn" method="post" action="/do_login">
                    <h2>Logga in</h2>
                    <!--<label for="email">Användarnamn</label>-->
                    <p id="alert" style="display: none"></p>
                    <input placeholder="Email" type="input" name="email" id="email" value="">
                    <!--<label for="password">Lösenord</label>-->
                    <input placeholder="Lösenord" type="password" name="password" id="password" value="">
                    <input class="myButton" type="submit" value="Logga in">		
                </form>
                <p id="error"></p>
                <!--<div class="push"></div> <!-- Är till för att footer ska hamna längst ner, ta ej bort -->
            </div>
        </div>
        <div class="content2">
            <div id="wrapContent">
                <div class="contentInContent">
                    <div class="roundBox"><h2>Studenter</h2></div>
                    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                </div>
                <div class="contentInContent">
                    <div class="roundBox"><h2>Uppdragsgivare</h2></div>
                    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                </div>
            </div>
        </div>
        
        <footer>
            <div class="wrap">
            © Questway, 2016
            </div>
        </footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>