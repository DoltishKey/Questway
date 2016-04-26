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
                <ul id="tabs" class="tabs_class width_of_tabs_2">
                    <li><a href="#lediga_uppdrag" onclick="showTab()">Lediga uppdrag</a></li>
                    <li><a href="#sökta_uppdrag" onclick="showTab()">Sökta uppdrag</a></li>
                    <li><a href="#pågående_uppdrag" onclick="showTab()">Pågående uppdrag</a></li>
                    <li><a href="#avslutade_uppdrag" onclick="showTab()">Avslutade uppdrag</a></li>
                </ul>
            </div>

                <div class="tabContent" id="lediga_uppdrag">
                    <div class="wrap">
                         %for i in annons:
                            <div class="add">
                                    <h2>{{i[1]}}</h2>
                                    <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{i[4]}}</p>
                                    <div class="showMore">
                                        <h4>Beskrivning:</h4>
                                        <p>{{i[2]}}</p>
                                        <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{i[0]}}</p>
                                        <form  name="sok_annons" id="sok_annons" method="POST" action="/sok_annons/{{i[5]}}">
                                            <input type="submit" value="Sök annons" class="myButton">
                                        </form>
                                    </div>
                                <div class="arrow">></div>
                            </div>
                        %end
                    </div>
                </div>

            <div class="tabContent" id="sökta_uppdrag">
                <div class="wrap">
                        %for i in annons:
                            <div class="add">
                                <h2>{{i[1]}}</h2>
                                <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{i[4]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{i[2]}}</p>
                                    <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{i[0]}}</p>
                                </div>
                            </div>
                        %end
                </div>
            </div>

            <div class="tabContent" id="pågående_uppdrag">
                <div class="wrap">
                    %for i in annons:
                        <div class="add">
                            <h2>{{i[1]}}</h2>
                            <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{i[4]}}</p>
                            <div class="showMore">
                            <h4>Beskrivning:</h4>
                            <p>{{i[2]}}</p>
                            <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{i[0]}}</p>
                            </div>
                        </div>
                    %end
                </div>
            </div>


        <div class="tabContent" id="avslutade_uppdrag">
            <div class="wrap">
            %for grading in gradings:
                %if user_id == grading['selected']:
                <div class="add">
                    <h2>{{grading['ad_title']}}</h2>
                    %if grading['display'] == False:
                        <p>Uppdraget visas inte på din profil</p>
                        <a href="/profiles/{{user_id}}#mission{{grading['uniq_adNr']}}">Visa på din profil</a>
                    %end    
                %end
                </div>
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
