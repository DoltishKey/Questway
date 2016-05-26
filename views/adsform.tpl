<!--
Skriven av: Philip (HTML + CSS)
Uppdaterad av: Sofia (HTML, CSS)
-->
<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        <div id="wrapper">
            %include('nav_employers.tpl')
            <div id="content_wrap">
                <div id="content">
                <h3 id="add_ad">Lägg till annons för nytt uppdrag</h3>
                <form  name="create_ad" id="create_ad" method="POST" action="/make_ad" onsubmit="return createAdValid()">
                        <label for="ca_title">Titel:</label>
                        <input type="input" name="ad_title" id="ca_title" value="" placeholder="Kort beskrivande titel" required pattern=".*\S+.*" title="Du måste ange en titel">
                        <br>
                        <label for="ca_text">Annonstext:</label>
                        <textarea type="input" name="ad_text" id="ca_text" value="" placeholder="Lite längre beskrivande text" required></textarea>
                    <input type="submit" value="Skapa annons" name='uniq_adNr' id="ad_done" class="myButton">
                </form>

                <p id="error"></p>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
