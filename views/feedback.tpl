<!DOCTYPE html>
<html>
    % include('head.tpl')
	<body>
        % include('nav_employers.tpl')
		<content>
            <h1>Ge feedback!</h1>
            <form action="/ad_done/{{adnr}}" method="post">
              <textarea name="feedback" id="feedback"></textarea>
              <select id="grade" name="grade">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
              </select>
              <input type="submit" value="Sicka">
            </form>
      </content>
	</body>
</html>
