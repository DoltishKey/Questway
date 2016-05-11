<!DOCTYPE html>
<html>
    % include('head.tpl')
	<body>
        <div id="wrapper">
            %include('nav.tpl')
            <div id="content">
                <h3>Skapa profil som:</h3>
            <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->
                <a class="choicereg" id="employreg" href="/create_employer"><h3>Uppdragsgivare</h3></a>

                <a class="choicereg" id="studentreg" href="/create_student"><h3>Student</h3></a>
                </p>
            </div>
        </div>

        %include('footer.tpl')
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
