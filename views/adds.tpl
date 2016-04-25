<!DOCTYPE html>
<html>
    %include('head.tpl')
    <body onload="init()">
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
                %if len(adds)>0:
                    <div class="employers_add_new_ad col btnbox">
                        <div>
                            <a class="btn" id="btn_id" href="/showadds">Lägg till annons</a>
                        </div>
                    </div>
                    %for add in adds:
                        %if user_id in add:
                            <div class="add">
                                <form  name="ta_bort_annons" id="del_annons" method="POST" action="/del_ad/{{add[0]}}">
                                    <input type="submit" value="Ta bort annons" class="myButton delete_ad">
                                </form>
                                <h2>{{add[1]}}</h2>
                                <h4 class="inline">Publicererades: </h4> <p class="inline_block">{{add[4]}}</p>
                                <div class="showMore">
                                    <h4>Beskrivning:</h4>
                                    <p>{{add[2]}}</p>
                                </div>
                                <ul>
                            </div>
                        %end
                    %end
                %else:
                    <h1 class="no_ads"> Listan av annonser är tom </h1>
                    <div class="employers_add_new_ad col btnbox">
                        <div>
                            <a class="btn" id="btn_id" href="/showadds">Lägg till annons</a>
                        </div>
                    </div>
                %end
            </div>
        </div>
    </body>
</html>
