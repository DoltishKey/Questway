<!DOCTYPE html>
<html>
    %include('head.tpl')
    <body onload="init()">
        %include('nav_employers.tpl')

        <div class="wrap">
            <ul id="tabs" class="tabs_class width_of_tabs_1">
                <li><a href="#uppdrag" onclick="showTab()">Dina uppdrag</a></li>
                <li><a href="#pågående_uppdrag" onclick="showTab()">Pågående uppdrag</a></li>
                <li><a href="#avslutade_uppdrag" onclick="showTab()">Avslutade uppdrag</a></li>
            </ul>
        </div>

        <div class="tabContent" id="uppdrag">
            <div class="wrap">
            %if len(adds)>0:
                <div>
                    <a class="btn" id="btn_id_ads" href="/showadds">Lägg till annons</a>
                </div>

            %else:
                <h1 class="no_ads"> Listan av annonser är tom </h1>
                <div class="employers_add_new_ad col btnbox">
                    <div>
                        <a class="btn" id="btn_id_ads" href="/showadds">Lägg till annons</a>
                    </div>
                </div>
            %end

            %for add in adds:
                    <div class="add">
                        <h2>{{add[1]}}</h2>
                        <h4 class="inline_block">Publicererades: </h4> 
                        <p class="inline_block">{{add[4]}}</p>
                        <h4 class="inline_block col2">Antal ansökningar: </h4>
                        <p class="inline_block">5 <!-- Ladda in antal här --></p>
                        <div class="showMore">
                            <h4>Beskrivning:</h4>
                            <p>{{add[2]}}</p>
                            <h3>Ansökningar:</h3>
                            <!-- Om antal ansökningar > 0, gör detta: -->
                            <div id="applications">
                                <ul>
                                    %for student in students:
                                        %if int(student[3]) == int(add[0]):
                                            <li>
                                                <h4 class="col1"><a href="/profiles/{{student[0]}}">{{student[1]}} {{student[2]}}</a></h4>
                                                <p class="col1 inline_block">Namn på program, år</p>
                                                <p class="col2 inline_block">Malmö Högskola</p>
                                                <p class="col3 inline_block">Övriga kunskaper: PHP, Java, Bootstrap</p>
                                                <form name="choose_student" action="" id="choose_student" method="get">
                                                <input type="submit" name="choose" id="choose" class="myButton" value="Välj student">
                                                </form>
                                            </li> 
                                        %end
                                    %end
                                </ul>
                            </div>
                            <!-- Om antal ansökningar = 0, visa detta: -->
                            <!--<p>Än så länge finnas det inga ansökningar till detta uppdrag.</p>-->
                            <form  name="ta_bort_annons" id="del_annons" method="POST" action="/del_ad/{{add[0]}}">
                            <input type="submit" value="Ta bort annons" class="myButton delete_ad">
                            </form>
                        </div>
                        <div class="arrow">></div>
                </div>
                %end
                </div>
            </div>
                                    <!--<ul>
                                        %for student in students:
                                            %if int(student[3]) == int(add[0]):
                                                <li><a href="/profiles/{{student[0]}}">{{student[1]}} {{student[2]}} Satus: {{student[4]}}</a></li>
                                            %end
                                        %end
                                    </ul>-->
                                


        <div class="tabContent" id="pågående_uppdrag">
            <div class="wrap">
                %if len(adds) == 0:
                    <h1 class="no_ads"> Listan av annonser är tom </h1>
                    <div>
                        <a class="btn" id="btn_id_ads" href="/showadds">Lägg till annons</a>
                    </div>
                %end
                %for add in adds:
                    %if user_id in add:
                        <div class="add">
                            <h2>{{add[1]}}</h2>
                            <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{add[4]}}</p>
                            <div class="showMore">
                                <h4>Beskrivning:</h4>
                                <p>{{add[2]}}</p>
                                <form  name="ta_bort_annons" id="del_annons" method="POST" action="/del_ad/{{add[0]}}">
                                <input type="submit" value="Ta bort annons" class="myButton delete_ad">
                                </form>
                            </div>
                            <div class="arrow">></div>
                        </div>
                    %end
                %end
            </div>
        </div>

        <div class="tabContent" id="avslutade_uppdrag">
            <div class="wrap">
                <h1 class="no_ads"> Du har inga avslutade uppdrag. </h1>
                <div>
                    <a class="btn" id="btn_id_ads" href="/showadds">Lägg till annons</a>
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
