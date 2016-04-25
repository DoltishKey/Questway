<!DOCTYPE html>
<html>

    %include('head.tpl')

	<body onload="init()">
        
        %include('nav_students.tpl')

        <div class="container_student_start">
            <h2>Uppdrag</h2>
        </div>
                
        <div class="wrap_around_tab_content">
            
            <div class="wrap">
                <!-- Länkar till tabbarna: -->
                <ul id="tabs">
                    <li><a href="#lediga_uppdrag" onclick="showTab()">Lediga uppdrag</a></li>
                    <li><a href="#sökta_uppdrag" onclick="showTab()">Sökta uppdrag</a></li>
                    <li><a href="#pågående_uppdrag" onclick="showTab()">Pågående uppdrag</a></li>
                    <li><a href="#avslutade_uppdrag" onclick="showTab()">Avslutade uppdrag</a></li>
                </ul>
            </div>
            
            <div class="wrap">
                <div class="tabContent" id="lediga_uppdrag">
                        <!--<h2 class="pageTitle">Lediga uppdrag</h2>-->
                             %for i in annons:
                                %if user_id not in i['who_applied']:
                                <div class="add">
                                        <h2>{{i['ad_title']}}</h2>
                                        <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{i['date_of_adcreation']}}</p>
                                        <div class="showMore">
                                            <h4 class="inline-block">Kompetenser:</h4>
                                            <p class="inline-block">HTML5</p>
                                            <p class="inline-block">CSS3</p>
                                            <h4>Beskrivning:</h4>
                                            <p>{{i['ad_text']}}</p>
                                            <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{i['ad_corpName']}}</p>
                                            <form  name="sok_annons" id="sok_annons" method="POST" action="/sok_annons/{{i['uniq_adNr']}}">
                                                <input type="submit" value="Sök annons" class="myButton">
                                            </form>
                                            <div class="arrow"> </div>
                                        </div>
                                    <div class="arrow">></div>
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
                                    <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{i['date_of_adcreation']}}</p>
                                    <div class="showMore">
                                        <h4>Beskrivning:</h4>
                                        <p>{{i['ad_text']}}</p>
                                        <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{i['ad_corpName']}}</p>
                                    </div>
                                    <div class="arrow">></div>
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
                        <a href="#">Visa på din profil</a>
                    </div>
                    %end
                %end
            </div>

            </div>
        </div>

        <footer>
            <div class="wrap">
                <p>Copyright Questway, 2016</p>
            </div>
        </footer>

	</body>
</html>
