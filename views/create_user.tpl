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
                <nav>
                    <a class="options" href="/login">Logga in</a>
                    <a class="options" href="/">Registrera</a>
                    <a class="options" href="">Om oss</a>
                </nav>
            </header>
            <div id="content">
                <h3>Skapa profil som:</h3>
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->

                <a class="choicereg" id="employreg" href="../views/create_employer.tpl">
                    <h3>Uppdragsgivare</h3>
                </a>
                
                <a class="choicereg" id="studentreg" href="../views/create_student.tpl">      
                    <h3>Student</h3>
                </a>
               
            <p id="error">
                </p>
            </div>
            <div class="push">
            </div> <!-- Är till för att footer ska hamna längst ner, ta ej bort --><!--Kolla på position:fixed istället-->
        </div>
        <footer>© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>