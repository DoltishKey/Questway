<!DOCTYPE html>
<html>
    % include('head.tpl')
	<body>
        % include('nav_employers.tpl')
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
                <input class="myButton" type="submit" value="Skicka">
            </form>
        </div>
        
        <footer>
            <div class="wrap">
                <p>Copyright Questway, 2016</p>
            </div>
        </footer>
	</body>
</html>
