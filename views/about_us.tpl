<!DOCTYPE html>
<html>
 %include('head.tpl')
    <body>
        <div id="wrapper">
            %if user_autho == 1:
                % include('nav_students.tpl')
            %elif user_autho == 2:
                % include('nav_employers.tpl')
            %else:
                % include('nav.tpl')
            %end
            <div id="content_wrap">
                <div id="container_of_container">
                    <h2 class="about_questway">Om Questway</h2>
                    <div class="about_us_info">
                        <p>Questway är en tjänst för studenter på Malmö Högskola och företag i Malmöregionen. Tjänsten inriktar sig främst på studenter som studerar data-/IT-inriktade program. Här kan företag som är i behov av hjälp med IT-relaterade projekt lägga ut annonser för detta, som studenter sedan enkelt kan ansöka till. Företaget kan sedan välja den student som man anser passar bäst till projektet/uppdraget.
                        </p>
                        <p>Anledningen till att tjänsten inriktar sig på företag i Malmöregionen är att vi vill uppmuntra till fysiska möten mellan uppdragsgivare och student. Ambitionen är dock att på sikt utöka tjänsten så att även företag i andra regioner samt andra lärosäten kan inkluderas.
                        </p>
                        <p>Questway har utvecklats under ett projektarbete i kursen Systemutveckling och Projekt 1 av fyra studenter på Malmö Högskola.
                        </p>
                    </div>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
