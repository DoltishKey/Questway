<!DOCTYPE html>
<html>
    % include('head.tpl')
    <body>
        %include('nav_employers.tpl')
        <div id="content">
        <form  name="create_ad" id="create_ad" method="POST" action="/make_ad" onsubmit="return createAdValid()">
            <h3 id="ca_Title">Lägg till annons för nytt uppdrag</h3>

            <div class="ca_Formblock" id="ca_Labels">
                <label for="ca_title">Titel:</label>
                <label for="ca_text">Annonstext:</label>
            </div>

            <div class="ca_Formblock"  id="ca_Inputs">
                <input type="input" name="ad_title" id="ca_title" value="" placeholder="Kort beskrivande titel" required pattern=".*\S+.*" title="Du måste ange en titel">
                <br>
                <textarea rows="4" cols="50" type="input" name="ad_text" id="ca_text" value="" placeholder="Lite längre beskrivande text." required></textarea>
            </div>
            <input type="submit" value="Skapa annons" name='uniq_adNr' id="ad_done" class="myButton">
        </form>

        <p id="error"></p>
        </div>
        %include('footer.tpl')
    </body>
</html>
