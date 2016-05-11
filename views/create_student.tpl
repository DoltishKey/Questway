<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        <div id="wrapper">
            %include('nav.tpl')
            <div id="content_wrap">
                <div id="content">

                <form name="create_student" id="create_student" method="post" action="/do_create_student">
                   <h3 class="form_head" id="studentform_Title">Skapa profil | Student</h3>

                    <div class="form_labels">
                        <label for="first_name">Förnamn</label>
                        <br>
                        <label for="last_name">Efternamn</label>
                        <br>
                        <label for="program">Utbildning</label>
                        <br>
                        <label for="year">Årskurs</label>
                        <br>
                        <label for="email">Mejl</label>
                        <br>
                        <label for="phone">Tele</label>
                        <br>
                        <label for="password">Lösenord</label>
                    </div>

                    <div class="form_inputs">
                        <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="" required>
                        <br>
                        <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="" required>
                        <br>
                        <select name="program" id="program" value="" required>
                            <option value="1">Informationsarkitekt</option>
                            <option value="2">Systemutvecklare</option>
                            <option value="3">App</option>
                        </select>
                        <br>
                        <input placeholder="Årskurs" type="input" name="year" id="year" value="" required>
                        <br>
                        <input placeholder="Mejl" type="input" name="email" id="email" value="" required>
                        <br>
                        <input placeholder="Telefon" type="input" name="phone" id="phone" value="" required>
                        <br>
                        <input placeholder="Lösenord" type="input" name="password" id="password" value="" required>
                    </div>
                    <input class="create_account myButton" type="submit" value="Skapa konto" required>
                   <!--
                   <label for="first_name">Förnamn</label>
                   <input placeholder="Förnamn" type="input" name="first_name" id="first_name" value="">
                    <br>

                       <label for="last_name">Efternamn</label>
                    <input placeholder="Efternamn" type="input" name="last_name" id="last_name" value="">
                    <br>

                    <label for="program">Utbildning</label>
                    <select name="program" id="program" value="">
                        <option value="1">Informationsarkitekt</option>
                        <option value="2">Systemutvecklare</option>
                        <option value="3">App</option>
                    </select>
                    <br>

                    <label for="year">Årskurs</label>
                    <input placeholder="Årskurs" type="input" name="year" id="year" value="">
                    <br>

                    <label for="email">Mejl</label>
                    <input placeholder="Mejl" type="input" name="email" id="email" value="">
                    <br>

                    <label for="password">Lösenord</label>
                    <input placeholder="Lösenord" type="input" name="password" id="password" value="">

                    <input id="logInButton" type="submit" value="Skapa konto">
                    <br>
                    -->
                </form>
                <p id="error"></p>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
