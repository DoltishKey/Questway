<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
	<body>
        <header>
            <nav class="menu">
                <a class="menuButton" href="">Uppdrag</a>
                <a class="menuButton" href="">Profil</a>
                <a class="menuButton" href="/log_out">Logga ut</a>
            </nav>
        </header>
		<content>
            <h1>Admin, {{user}}</h1>
            <h2>Du är inloggad som {{level}}</h2>
            
            %for i in annons:
    
	        <li><a href="/{{i['ad_corpName']}}"> {{i['ad_corpName']}}</a></li>
	    
	        <h1>{{i['ad_title']}}</h1>
	    
	        <p>{{i['ad_text']}}</p>
	        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
	            <input type="submit" value="Ta bort annons">
	        </form>
            
            <form  name="sok_annons" id="sok_annons" method="POST" action="/sok_annons/{{i['uniq_adNr']}}">
            <input type="submit" value="Sök annons">
        </form>
	    %end
            
            
            <a href="/log_out">Logga ut</a>
            <a href="/">Till start</a>
        </content>
	</body>
</html>