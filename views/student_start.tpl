<!DOCTYPE html>
<html>
    <head>
        <title>Uppdrag</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
	<body>
        <header>
            <h1>Questway</h1>
            <p>Inloggad som {{user}}</p>
            <p>Du är inloggad som: {{level}}</p>
            <nav class="menu">
                <a class="menuButton" href="">Uppdrag</a>
                <a class="menuButton" href="">Profil</a>
                <a class="menuButton" href="/log_out">Logga ut</a>
            </nav>
        </header>
<<<<<<< HEAD
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
            
=======
                <content>
                    <h1>Admin, {{user}}</h1>
                    <h2>Du är inloggad som {{level}}</h2>
                    <a href="/log_out">Logga ut</a>
                    <a href="/">Till start</a>
                </content>
        <!--<div class="content">
            <section class="quests">
                <h2>Lediga uppdrag</h2>
                <div class="add">
                     %for i in annons:
                        <h1>{{i['ad_title']}}</h1>
                        <p>Publiceringsdatum och antal ansökningar ska laddas in här.</p>
                            <p>{{i['ad_text']}}</p>
        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
            <input type="submit" value="Ta bort annons">
        </form>
                    <h3>{{i['ad_corpName']}} Vad är detta?</h3>
                    %end
                </div>-->
            </section>
        </div>
>>>>>>> origin/master
            
            <a href="/log_out">Logga ut</a>
            <a href="/">Till start</a>
        </content>
>>>>>>> origin/master
	</body>
</html>