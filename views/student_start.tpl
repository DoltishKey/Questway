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
                    <div id="thanks_for_applying">Tack för din ansökan. Uppdraget finns nu under "Sökta uppdrag".</div>
                    %if len(avail_ads)<= 0:
                        <h2 class="no_ads"> Listan av annonser är tom </h1>
                    %else:
                        %for each in avail_ads:
                                <div class="add">
                                        <h2>{{each[1]}}</h2>
                                        <h4 class="inline_block">Publicererades: </h4>
                                        <p class="inline_block">{{each[3]}}</p>
                                        <div class="showMore">
                                            <h4>Beskrivning:</h4>
                                            <p>{{each[2]}}</p>
                                            <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{each[4]}}</p>
                                            <form  name="sok_annons" id="sok_annons" method="POST" action="/apply_on_ad/{{each[0]}}">
                                                <input type="submit" value="Sök annons" class="myButton delete_ad" onclick="thanks_for_applying()">
                                            </form>
                                        </div>
                                    <div class="arrow">></div>
                                </div>
                        %end
                    %end
                    </div>
                </div>

            <div class="tabContent" id="sökta_uppdrag">
                <div class="wrap">
                    %if not pending_ad and not denied_missions:
                        <h1 class="no_ads"> Listan av annonser är tom </h1>
                    %else:
                        %for every in pending_ad:
                            <div class="add">
                                <h2>{{every[1]}}</h2>
                                <h4 class="inline_block">Publicererades: </h4>
                                <p class="inline_block">{{every[3]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{every[2]}}</p>
                                    <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{every[4]}}</p>
                                </div>
                                <div class="arrow">></div>
                            </div>
                        %end
                        %for item in denied_missions:
                            <div class="add">
                                <h2>{{item[0]}}</h2>
                                <p class="inline_block">Tyvärr så fick du inte uppdraget.</p>
                            </div>
                        %end
                    %end
                </div>
            </div>

            <div class="tabContent" id="pågående_uppdrag">
                <div class="wrap">
                    %if not accepted_on:
                        <h1 class="no_ads"> Listan av annonser är tom </h1>
                    %else:
                        %for each_ad in accepted_on:
                            <div class="add">
                                <h2>{{each_ad[1]}}</h2>
                                <h4 class="inline_block">Publicererades:
                                </h4> <p class="inline_block">{{each_ad[3]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{each_ad[2]}}</p>
                                    <h4 class="inline_block">Företag: </h4>
                                    <p class="inline_block"> {{each_ad[4]}}</p>
                                    <h4>Kontakt:</h4>
                                    <p>Kontaktperson: {{each_ad[8]}} {{each_ad[9]}}</p>
                                    <p>Epostadress: <a href="mailto:{{each_ad[10]}}" target="_top">{{each_ad[10]}}</a></p>
                                </div>
                                <div class="arrow">></div>
                            </div>
                        %end
                    %end
                </div>
            </div>


        <div class="tabContent" id="avslutade_uppdrag">
            <div class="wrap">
                %if not finished_ads or finished_ads[0]==user_id and finished_ads[1]=='Avslutad':
                    <h1 class="no_ads"> Listan av annonser är tom </h1>
                %else:
                    %for one in finished_ads:
                        <div class="add">
                            <h2>{{one[1]}}</h2>
                            <h4 class="inline_block">Publicererades: </h4>
                            <p class="inline_block">{{one[3]}}</p>
                            <div class="showMore">
                                <h4>Beskrivning:</h4>
                                <p>{{one[2]}}</p>
                                <h4 class="inline_block">Företag: </h4><p class="inline_block"> {{one[4]}}</p>
                                <h4>Kontakt:</h4>
                                <p>Kontaktperson: {{one[8]}} {{one[9]}}</p>
                                <p>Epostadress: <a href="mailto:{{one[10]}}" target="_top">{{one[10]}}</a></p>
                                <h4>Feedback från företaget:</h4>
                                <p>{{one[11]}}</p>
                                <p>Betyg: {{one[12]}}</p>
                            </div>
                            <div class="arrow">></div>
                        </div>
                    %end
                %end
            </div>
        </div>

        <footer>
            <div class="wrap">
                <p>Copyright Questway, 2016</p>
            </div>
        </footer>
    </body>
</html>
