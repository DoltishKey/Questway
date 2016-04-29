<!DOCTYPE html>
<html>
    %include('head.tpl')
    <body onload="init()">
        %include('nav_employers.tpl')

        <div class="wrap" id="move_under_header">
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
                            <h4 class="inline_block">Publicererades: </h4> 
                            <p class="inline_block">{{add[4]}}</p>

                            %num_applications = sum(x.count(add[0]) for x in students)
                            % if num_applications > 1:
                                <h4 class="inline_block col2">Ansökningar: <span>{{num_applications}}</span></h4>
                            %elif num_applications == 1:
                                <h4 class="inline_block col2">Ansökningar: <span>{{num_applications}}</span></h4>
                            %else:
                                <h4 class="inline_block col2">Inga ansökningar</h4>
                            %end
                            
                            <div class="showMore">
                                <h4>Beskrivning:</h4>
                                <p>{{add[2]}}</p>
                                <form  name="ta_bort_annons" id="del_annons" method="POST" action="/del_ad/{{add[0]}}">
                                    <input type="submit" value="Ta bort annons" class="myButton delete_ad">
                                </form>
                           
                                %num_applications = sum(x.count(add[0]) for x in students)
                                % if num_applications > 1 or num_applications == 1:
                                    <h3>Ansökningar:</h3>
                                    <!-- Om antal ansökningar > 0, gör detta: -->
                                    <div id="applications">
                                        <ul>
                                            %for student in students:
                                                %if int(student[3]) == int(add[0]):
                                                    <a href="/profiles/{{student[0]}}" target="_blank">
                                                        <li>
                                                            <h4 class="col1">{{student[1]}} {{student[2]}}</h4>
                                                            <p class="col1 inline_block">{{student[5]}}, {{student[6]}}</p>
                                                            <p class="col2 inline_block">Malmö Högskola</p>
                                                            <!--<p class="col3 inline_block">Övriga kunskaper: PHP, Java, Bootstrap</p>-->
                                                            <a id="choose" href="/select_student/{{add[0]}}/{{student[0]}}">Välj student</a>
                                                        </li> 
                                                    </a>
                                                %end
                                            %end
                                    </div>
                                %end
                            </div>
                            <div class="arrow">></div>
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
                                <h4 class="inline_block">Publicererades: </h4> <p class="inline_block">{{add[4]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{add[2]}}</p>
                                    <ul class="chosen_student">
                                        %for student in students:
                                            %if int(student[3]) == int(add[0]) and student[4] == 'Vald':
                                                <h4>Vald student för uppdraget:</h4>
                                                <li>Namn: <a href="/profiles/{{student[0]}}" target="_blank">{{student[1]}} {{student[2]}}</a></li>
                                                <li>Epost: <a href="mailto:{{student[7]}}" target="_top">{{student[7]}}</a></li>
                                            %end
                                        %end
                                    </ul>
                                    <a class="myButton inline_block" id="mission_done" href="/give_feedback/{{add[0]}}">Uppdraget är klart</a>
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
                                <h4 class="inline_block">Publicererades: </h4> <p class="inline_block">{{add[4]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{add[2]}}</p>
                                    <ul class="chosen_student">
                                        %for student in students:
                                            %if int(student[3]) == int(add[0]) and student[4] == 'Avslutad':
                                                <h4>Student som utfört uppdraget:</h4>
                                                <li>Namn: <a href="/profiles/{{student[0]}}" target="_blank">{{student[1]}} {{student[2]}}</a></li>
                                                <li>Epost: <a href="mailto:{{student[7]}}" target="_top">{{student[7]}}</a></li>
                                            %end
                                        %end
                                    </ul>
                                    <h4>Feedback</h4>
                                    %for f in feedback: 
                                        % if f[0] == add[0]:
                                        <p>{{f[1]}}</p>
                                        <p>Betyg: {{f[2]}}</p>
                                        %end
                                    %end
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
