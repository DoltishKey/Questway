<header>
        <div class="wrap" id="header_wrap">
        <div class="courtesyNav">
                <p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
            </div>
            <a id="QWTitle" href="/"><h1>Questway</h1></a>
            <!--<img alt="meny" src="../static/img/menyicons/menyicon2.png" id="menyknapp" onclick="showHideMenu()" onload="menuSetUp()">-->
            <nav class="menu">
                    %from bottle import request

                    %if request.path == '/admin':
                        <a  class="currentMenuItem allMenuItems" href="/admin">Start</a>
                    %else:
                        <a class=" allMenuItems" href="/admin">Start</a>
                    %end

                    %if request.path == '/allMissions':
                        <a  class="currentMenuItem allMenuItems" href="/allMissions">Uppdrag</a>
                    %else:
                        <a class=" allMenuItems" href="/allMissions">Uppdrag</a>
                    %end

                    %if request.path == '/log_out':
                        <a class="currentMenuItem allMenuItems" href="/log_out">Logga</a>
                    %else:
                        <a class=" allMenuItems" href="/log_out">Logga ut</a>
                    %end
            </nav>
        </div>
</header>
