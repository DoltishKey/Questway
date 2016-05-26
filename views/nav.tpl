<!--
Skriven av: Jacob (HTML)
Skriven av: ??Sofia?? (CSS)
-->
<header>
    <div class="wrap" id="header_wrap">
        <a id="QWTitle" href="/"><h1>Questway</h1></a>
        <!--<img alt="meny" src="../static/img/menyicons/menyicon2.png" id="menyknapp" onclick="showHideMenu()" onload="menuSetUp()">-->
        <nav class="menu">
                %from bottle import request

                %if request.path == "/login":
                    <a class="currentMenuItem allMenuItems" href="/login">Logga in</a>
                %else:
                    <a class=" allMenuItems" href="/login">Logga in</a>
                %end

                %if request.path == "/create":
                    <a class="currentMenuItem allMenuItems" href="/create">Registrera</a>
                %else:
                    <a class=" allMenuItems" href="/create">Registrera</a>
                %end


                %if request.path == '/about':
                    <a class="currentMenuItem allMenuItems" href="/about_us">Om oss</a>
                %else:
                    <a class=" allMenuItems" href="/about_us">Om oss</a>
                %end
        </nav>
    </div>
</header>
