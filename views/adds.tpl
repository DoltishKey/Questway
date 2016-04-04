<ul>
    %for i in annons:
    
        <li><a href="/{{i['ad_corpName']}}"> {{i['ad_corpName']}}</a></li>
    
        <h1>{{i['ad_title']}}</h1>
    
        <p>{{i['ad_text']}}</p>
        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
            <input type="submit" value="Ta bort annons">
        </form>
    %end
</ul>