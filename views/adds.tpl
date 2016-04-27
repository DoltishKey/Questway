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
                    %if (any( int(student[3]) == int(add[0]) and (str(student[4]) != 'Obehandlad') for student in students)) == False:
                        <div class="add">
                            <h2>{{add[1]}}</h2>
                            <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{add[4]}}</p>
                            <div class="showMore">
                                <h4>Beskrivning:</h4>
                                <p>{{add[2]}}</p>
                                <form  name="ta_bort_annons" id="del_annons" method="POST" action="/del_ad/{{add[0]}}">
                                    <input type="submit" value="Ta bort annons" class="myButton delete_ad">
                                </form>

                                <ul>
                                    %for student in students:
                                        %if int(student[3]) == int(add[0]):
                                            %print student[4]
                                            <li><a href="/profiles/{{student[0]}}">{{student[1]}} {{student[2]}} Satus: {{student[4]}}</a></li>
                                        %end
                                    %end
                                </ul>
                            </div>
                        </div>
                    %end
                %end
            </div>
        </div>


        <div class="tabContent" id="pågående_uppdrag">
            <div class="wrap">
                %if any((student[4] == "Vald") for student in students) == False:
                    <h1 class="no_ads"> Listan av annonser är tom </h1>

                %else:
                    %for add in adds:
                        %if any(int(student[3]) == int(add[0]) and (student[4] == "Vald") for student in students) == True:
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
                %end
            </div>
        </div>

        <div class="tabContent" id="avslutade_uppdrag">
            <div class="wrap">
                %if any((student[4] == "Avslutad") for student in students) == False:
                    <h1 class="no_ads"> Listan av annonser är tom </h1>

                %else:
                    %for add in adds:
                        %if any(int(student[3]) == int(add[0]) and (student[4] == "Avslutad") for student in students) == True:
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
