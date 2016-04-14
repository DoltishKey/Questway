<!DOCTYPE html>
<html>

    %include('head.tpl')

	<body onload="init()">
        <header>
            <div class="courtesyNav">
                <p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
            </div>
            <h1>Questway</h1>
            <nav class="menu">
                <a class="currentMenuItem" href="">Uppdrag</a>
                <a href="/profiles/{{user_id}}">Profil</a>
                <a href="/log_out">Logga ut</a>
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
                     %for i in annons:
                        %if user_id not in i['who_applied']:
                        <div class="add">
                                <h2>{{i['ad_title']}}</h2>
                            <p class="inline"><span class="bold">Publicererades:</span> {{i['date_of_adcreation']}}</p>
                                <div class="showMore">
                                    <p>{{i['ad_text']}}</p>
                                    <p>{{i['ad_corpName']}}</p>
                                    <form  name="sok_annons" id="sok_annons" method="POST" action="/sok_annons/{{i['uniq_adNr']}}">
                                        <input type="submit" value="Sök annons" class="myButton">
                                    </form>
                                </div>
                        </div>
                        %end
                    %end
        </div>

        <div class="tabContent" id="sökta_uppdrag">
                <h2 class="pageTitle">Uppdrag du sökt</h2>
                    %for i in annons:
                        %if user_id in i['who_applied']:
                        <div class="add">
                            <h2>{{i['ad_title']}}</h2>
                            <p class="inline"><span class="bold">Publicererades:</span> {{i['date_of_adcreation']}}</p>
                            <div class="showMore">
                                <p>{{i['ad_text']}}</p>
                                <p>{{i['ad_corpName']}}</p>
                            </div>
                        </div>
                        %end
                    %end
        </div>

        <div class="tabContent" id="pågående_uppdrag">
            <h2 class="pageTitle">Dina pågående uppdrag</h2>
            <p>Går ej att visa ännu.</p>
        </div>

        <div class="tabContent" id="avslutade_uppdrag">
            <h2 class="pageTitle">Avslutade uppdrag</h2>
            %for grading in gradings:
                %if user_id == grading['selected']:
                <div class="add">
                    <h2>{{grading['ad_title']}}</h2>
                    %if grading['display'] == False:
                        <p>Uppdraget visas inte på din profil</p>
                    %end
                    <div class="showMore">
                        <p>{{i['ad_text']}}</p>
                        <p>{{i['ad_corpName']}}</p>
                    </div>
                    <a href="#">Visa på din profil</a>
                </div>
                %end
            %end
        </div>

        <footer>Copyright Questway, 2016</footer>

	</body>
</html>
