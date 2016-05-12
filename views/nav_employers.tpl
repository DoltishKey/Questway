<header>
        <div class="wrap" id="header_wrap">
        <div class="courtesyNav">
                <p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
        </div>
        <a id="QWTitle" href="/admin"><h1>Questway</h1></a>
            <nav class="menu">
                    %from bottle import request

                    %if request.path == '/admin':
                        <a class="currentMenuItem" href="/admin">Start</a>
                    %else:
                        <a href="/admin">Start</a>
                    %end

                    %if request.path == '/allMissions':
                        <a class="currentMenuItem" href="/allMissions">Uppdrag</a>
                    %else:
                        <a href="/allMissions">Uppdrag</a>
                    %end

                    %if request.path == '/log_out':
                        <a class="currentMenuItem" href="/log_out">Logga</a>
                    %else:
                        <a href="/log_out">Logga ut</a>
                    %end
            </nav>
        </div>
</header>
