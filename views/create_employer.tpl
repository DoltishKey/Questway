<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        <div id="wrapper">
            %include('nav.tpl')
            <div id="content_wrap">
                <div id="content">
                <!--<img src="../static/img/qwback.jpg" alt="qwbackground">
                    <div id="slogan"><p>Lorem ipsum dolor sit amet, <br>consectetur adipiscing elit.</p></div>-->
                <form name="create_employer" id="create_employer" method="post" action="/do_create_user/employer">
                    <h3 class="form_head" id="employerform_Title">Skapa profil | Uppdragsgivare</h3>
                    <div class="form_labels">
                        <label for="company_name">Företag</label>
                        <br>
                        <label for="org_nr">Org.nr</label>
                        <br>
                        <label for="first_name">Förnamn</label>
                        <br>
                        <label for="last_name">Efternamn</label>
                        <br>
                        <label for="email">Mejl</label>
                        <br>
                        <label for="password">Lösenord</label>
                    </div>
                    <div class="form_inputs">
                        <input placeholder="Företagsnamn" type="input" name="company_name" id="company_name" value="" required>
                        <br>
                        <input placeholder="Org.nr" type="input" name="org_nr" id="org_nr" value="" required>
                        <br>
                        <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="" required>
                        <br>
                        <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="" required>
                        <br>
                        <input placeholder="Mejl" type="input" name="email" id="email" value="" required>
                        <br>
                        <input placeholder="Lösenord" type="input" name="password" id="password" value="" required>
                    </div>

                    <input class="myButton" id="create_student_account" type="submit" value="Skapa konto">
                </form>

                <p id="error"></p>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
