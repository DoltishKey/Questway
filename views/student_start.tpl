<!DOCTYPE html>
<html>
    <head>
        <title>Uppdrag</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
        <script src="/static/js/tabs.js" type="text/javascript"></script>
    </head>
	<body onload="init()">
        <header>
            <div class="courtesyNav">
                <p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
            </div>
            <h1>Questway</h1>
            <nav class="menu inline">
                <a class="menuButton" href="">Uppdrag</a>
                <a class="menuButton" href="">Profil</a>
                <a class="menuButton" href="/log_out">Logga ut</a>
            </nav>
        </header>
        
        <!-- Länkar till tabbarna: -->
        <ul id="tabs">
            <li><a href="#lediga_uppdrag" onclick="showTab()">Lediga uppdrag</a></li>
            <li><a href="#sökta_uppdrag" onclick="showTab()">Sökta uppdrag</a></li>
            <li><a href="#pågående_uppdrag" onclick="showTab()">Pågående uppdrag</a></li>
            <li><a href="#avslutade_uppdrag" onclick="showTab()">Avslutade uppdrag</a></li>
        </ul>
            
        <div class="tabContent" id="lediga_uppdrag">
            <h2 class="pageTitle">Lediga uppdrag</h2>
                <div class="add">
                     %for i in annons:
                        <h2>{{i['ad_title']}}</h2>
                        <p>Publiceringsdatum och antal ansökningar ska laddas in här.</p>
                            <p>{{i['ad_text']}}</p>
                        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
                            <input type="submit" value="Ta bort annons" class="myButton">
                        </form>
                        <p>{{i['ad_corpName']}}</p>
                    %end
                </div>
        </div>
        
        <div class="tabContent" id="sökta_uppdrag">
                <h2 class="pageTitle">Uppdrag du sökt</h2>
                <div class="add">
                    %for i in annons:
                        <h2>{{i['ad_title']}}</h2>
                        <p>Publiceringsdatum och antal ansökningar ska laddas in här.</p>
                            <p>{{i['ad_text']}}</p>
                        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
                            <input type="submit" value="Ta bort annons" class="myButton">
                        </form>
                        <p>{{i['ad_corpName']}}</p>
                    %end
                </div>
        </div>
        
        <div class="tabContent" id="pågående_uppdrag">
            <h2 class="pageTitle">Dina pågående uppdrag</h2>
            <div class="add">
                    %for i in annons:
                        <h2>{{i['ad_title']}}</h2>
                        <p>Publiceringsdatum och antal ansökningar ska laddas in här.</p>
                            <p>{{i['ad_text']}}</p>
                        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
                            <input type="submit" value="Ta bort annons" class="myButton">
                        </form>
                        <p>{{i['ad_corpName']}}</p>
                    %end
            </div>
        </div>

        <div class="tabContent" id="avslutade_uppdrag">
            <h2 class="pageTitle">Avslutade uppdrag</h2>
            <div class="add">
                %for i in annons:
                    <h2>{{i['ad_title']}}</h2>
                    <p>Publiceringsdatum och antal ansökningar ska laddas in här.</p>
                        <p>{{i['ad_text']}}</p>
                    <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
                        <input type="submit" value="Ta bort annons" class="myButton">
                    </form>
                    <p>{{i['ad_corpName']}}</p>
                %end
            </div>
        </div>
        <footer>Copyright Questway, 2016</footer>
	</body>
</html>