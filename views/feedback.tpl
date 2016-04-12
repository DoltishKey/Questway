<!DOCTYPE html>
<html>
    % include('head.tpl')
	<body>
        <header>
            <h1>Questway</h1>
            <nav class="menu">
                <a class="menuButton" href="">Uppdrag</a>
                <a class="menuButton" href="">Profil</a>
                <a class="menuButton" href="/log_out">Logga ut</a>
            </nav>
        </header>
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

            <a href="/log_out">Logga ut</a>
            <a href="/">Till start</a>
      </content>
	</body>
</html>
