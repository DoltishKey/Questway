<!--
Skriven av: ??Philip?? (HTML + CSS)
-->
<!DOCTYPE html>
<html lang="sv">

    %include('head.tpl')

    <body>
        <div id="wrapper">
        %include('nav.tpl')
        <div id="content_wrap">
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
                        <p>Eller <a href="/create">registrera dig</a>.</p>
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
                        <p>Är du student på Malmö Högskola och studerar en data/it-inriktad utbildning? Är du intresserad av att arbeta vid sidan av dina studier? Då är Questway något för dig. Här kan du ansöka till mindre uppdrag åt företag i Malmöregionen, en bra möjlighet att skaffa dig erfarenhet samt bygga på ditt CV inför ditt framtida yrkesliv.  </p>
                    </div>
                    <div class="contentInContent">
                        <a id="regShortCutStud" href="/create_employer">
                            <div class="roundBox">
                                <h2>Uppdragsgivare</h2>
                                <p class="regText">Registrera dig nu!</p>
                            </div>
                        </a>
                        <p>Är du i behov av hjälp med något IT-inriktat projekt, så som t. ex. att bygga en webbplats eller en app, men saknar resurser för att utföra detta? På Questway finns möjligheten att anlita studenter som kan hjälpa dig med detta, för en låg kostnad och i utbyte mot en referens samt praktisk erfarenhet.</p>
                    </div>
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
        </div>
    </body>
</html>
