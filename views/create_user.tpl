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
                <h3>Skapa profil som:</h3>
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->
                <a class="choicereg" id="employreg" href="/create_employer"><h3>Uppdragsgivare</h3></a>

                <a class="choicereg" id="studentreg" href="/create_student"><h3>Student</h3></a>
                </p>
            </div>
        </div>
        <footer>© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
