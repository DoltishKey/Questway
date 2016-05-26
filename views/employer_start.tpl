<!--
Skriven av: Jacob (HTML+CSS)
Uppdaterad av: Sofia
-->
<!DOCTYPE html>
<html>
        % include('head.tpl')
    <body>
        <div id="wrapper">
        % include('nav_employers.tpl')
        <div id="content_wrap">
        <main id="admin_start_employer">
            <div id="employer_how_it_works" class="col">
                <h2>Hur funkar det?</h2>
                <div>
                    <p>Här på Questway kan du som företag/privatperson annonsera om att få hjälp med IT-inriktade uppdrag, så som t. ex. att bygga en webbplats, helt från grunden eller att uppdatera en redan befintlig, bygga en app eller kanske att designa ett nyhetsbrev. När du publicerat din annons visas den för de studenter som är registrerade här, och de som är intresserade kan skicka in en ansökan om att hjälpa dig. När du fått in ansökningar kan du gå in och titta på dessa studenters profiler och sedan välja en student som du tycker passar för uppdraget.
                    </p>

                    <p>För att lägga ut ett nytt uppdrag trycker på du knappen ”Lägg till uppdrag” i rutan längst till höger på denna sidan, eller går in under ”Uppdrag” i menyn och klickar på ”Lägg till uppdrag” där.
                    </p>
                </div>
            </div>
            <div id="toggle_how_it_works">
                <p>Hur funkar det?</p>
            </div>
            <div class="employers_add_new_ad col">
                <div>
                    <a class="btn" href="/do_new_ad">Lägg till annons</a>
                </div>
            </div>
            <div class="emloyers_all_adds col">
                <h2>Dina aktuella annonser</h2>
                <div>
                    <ul>
                        %for i in annons:
                            %if (any( int(student[3]) == int(i[0]) and (str(student[4]) != 'Obehandlad') for student in students_application)) == False:
                                <a href="/allMissions" data-value="{{i[0]}}" class="go_to_ad">
                                    <li>
                                        <div>
                                            <h3>{{i[1]}}</h3>

                                            %num_applications =0
                                            %for stud in students_application:
                                                %if stud[3] == i[0]:
                                                    %num_applications = num_applications + 1
                                                %end
                                            %end
                                            <!--num_applications = sum(x.count(i[0]) for x in students_application)-->
                                            % if num_applications > 1:
                                                <p><span>{{num_applications}}</span> ansökningar</p>
                                            %elif num_applications == 1:
                                                <p><span>{{num_applications}}</span> ansökningar</p>
                                            %else:
                                                <p>Inga ansökningar</p>
                                            %end
                                        </div>

                                        <div>></div>
                                    </li>
                                </a>
                            %end
                        %end
                    </ul>
                </div>
            </div>
      </main>
        </div>

    %include('footer.tpl')
    </div>
    </body>
</html>
