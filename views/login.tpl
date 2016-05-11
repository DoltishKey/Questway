<!DOCTYPE html>
<html lang="sv">

    %include('head.tpl')

	<body>
        %include('nav.tpl')

        <div class="wrapperLogin">
            <div class="wrap">
                <form name="logIn" id="logIn" method="post" action="/do_login">
                    <h2>Logga in</h2>
                    <!--<label for="email">Användarnamn</label>-->
                    <p id="alert" style="display: none"></p>
                    <input placeholder="Email" type="input" name="email" id="email" value="">
                    <!--<label for="password">Lösenord</label>-->
                    <input placeholder="Lösenord" type="password" name="password" id="password" value="">
                    <input class="myButton" type="submit" id="log_in_button" value="Logga in">	
                <p id="error"></p>
                </form>
            </div>
        </div>

        <div class="content2">
            <div id="wrapContent">
                <div class="contentInContent">
                    <a id="regShortCutStud" class="shortcut" href="/create_student">
                        <div class="roundBox">
                            <h2>Studenter</h2>
                            <p class="regText">Registrera dig nu!</p>
                        </div>
                    </a>
                    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                </div>
                <div class="contentInContent">
                    <a id="regShortCutStud" href="/create_employer">
                        <div class="roundBox">
                            <h2>Uppdragsgivare</h2>
                            <p class="regText">Registrera dig nu!</p>
                        </div>
                    </a>
                    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                </div>
            </div>
        </div>

        %include('footer.tpl')
        <!--<footer>
            <div class="wrap">
                <img id="footlog" src="../static/img/Logga.png" alt="loggan">
                <p>© Questway, 2016</p>
            </div>
        </footer>-->
	</body>
</html>
