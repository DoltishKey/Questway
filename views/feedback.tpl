<!--
Skriven av: Sofia (HTML+CSS)
-->
<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        <div id="wrapper">
            % include('nav_employers.tpl')
            <div id="content_wrap">
                <h2 class="center">Ge feedback till studenten</h2>
                <div class="form_color">
                    <form id="feedback_form" action="/ad_done/{{adnr}}" method="post">
                        <label for="feedback">Vad tyckte du om studentens arbete?</label>
                        <textarea name="feedback" id="feedback"></textarea>
                        <label for="grade">Betygsätt studentens arbete:</label>
                        <select id="grade" name="grade">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                        <input class="myButton" id="submit_feedback" type="submit" value="Skicka">
                    </form>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
