<!--
Skriven av: Philip (HTML + CSS)
-->
<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        <div id="wrapper">
            %include('nav.tpl')
            <div id="content_wrap">
                <div id="content">

                <form name="create_student" id="create_student" method="post" action="/do_create_user/student">
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
                        <select id="year" name="year" value="" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                        </select>
                        <br>
                        <input placeholder="Mejl" type="input" name="email" id="email" value="" required>
                        <br>
                        <input placeholder="Telefon" type="input" name="phone" id="phone" value="" required>
                        <br>
                        <input placeholder="Lösenord" type="input" name="password" id="password" value="" required>
                    </div>
                    <input class="myButton" id="create_student_account" type="submit" value="Skapa konto" required>
                </form>
                <p id="error"></p>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
