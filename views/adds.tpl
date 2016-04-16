<!DOCTYPE html>
<html>
    %include('head.tpl')
    <body>
        %include('nav_employers.tpl')
        <div class="tabContent" id="dina_uppdrag">
            <div class="wrap">
                <ul id="tabs">
                    <li><a href="#uppdrag" onclick="showTab()">Dina uppdrag</a></li>
                    <li><a href="#ansökta_uppdrag" onclick="showTab()">Ansökta</a></li>
                    <li><a href="#pågående_uppdrag" onclick="showTab()">Pågående uppdrag</a></li>
                    <li><a href="#avslutade_uppdrag" onclick="showTab()">Avslutade uppdrag</a></li>
                </ul>
                <h2 class="pageTitle">Dina uppdrag</h2>
                <div class="employers_add_new_ad col btnbox">
                    <div>
                        <a class="btn" id="btn_id" href="/showadds">Lägg till annons</a>
                    </div>
                </div>
                %if len(adds)>0:
                    %for add in adds:
                        <div class="add">
                            <h2>{{add['ad_title']}}</h2>
                            <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{add['date_of_adcreation']}}</p>
                            <div class="showMore">
                                <h4>Beskrivning:</h4>
                                <p>{{add['ad_text']}}</p>
                                %for who in add['who_applied']:
                                    %for student in students:
                                        %if student['id']==who:
                                            <li><a href="/profiles/{{student['id']}}">{{student['first_name'] + " "+student['last_name']}}</a></li>
                                        %end
                                    %end
                                %end
                            </div>
                            <ul>
                        </div>
                    %end
                %else:
                    <h1> Listan av annonser är tom </h1>
                %end
            </div>
        </div>
    </body>
</html>
