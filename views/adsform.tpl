<!DOCTYPE html>
<html>
<head>
    <title>Questway Adds</title>
    <meta charset="utf-8">
    <link type="text/css" rel="stylesheet" href="../static/css/main.css">
</head>
    <body>
        
        <form  name="create_ad" id="create_ad" method="POST" action="/make_ad">
            
            <div class="ad_title">
                <label for="ad_title">Titel:</label>
                <input type="input" name="ad_title" id="ad_title" value="">
            </div>

            <div class="ad_text">
                <label for="ad_text">Annonstext:</label>
                <input type="input" name="ad_text" id="ad_text" value="">
            </div>

            <input type="submit" value="Skapa annons" name='uniq_adNr' id="ad_done" class="myButton">
        </form>
        
    </body>
</html>