<!--
Skriven av: Jacob (HTML)
Skriven av: Sofia (HTML + CSS)
Mindre uppdateringar: Philip (logotyp)
-->
<header>
    <div class="wrap" id="header_wrap">
        <div class="courtesyNav">
                <p class="courtesyNavItem">Inloggad som <strong> {{user}}</strong></p>
        </div>
        <a id="QWTitle" href="/"><h1>Questway</h1></a>
        <!--<img alt="meny" src="../static/img/menyicons/menyicon2.png" id="menyknapp" onclick="showHideMenu()" onload="menuSetUp()">-->
        <nav class="menu">
                %from bottle import request

                %if request.path == '/admin':
                    <a class="currentMenuItem" href="/admin">Uppdrag</a>
                %else:
                    <a href="/admin">Start</a>
                %end

                %if request.path == '/profiles/' + str(user_id):
                    <a class="currentMenuItem" href="/profiles/{{student[4]}}">Profil</a>
                %else:
                    <a href="/profiles/{{user_id}}">Profil</a>
                %end

                %if request.path == '/log_out':
                    <a class="currentMenuItem" href="/log_out">Logga</a>
                %else:
                    <a href="/log_out">Logga ut</a>
                %end
        </nav>
    </div>
</header>
