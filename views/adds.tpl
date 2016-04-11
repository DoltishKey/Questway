
    

%for add in adds:
        
        <h1>{{add['ad_title']}}</h1>
    
        <p>{{add['ad_text']}}</p>
        
        <ul>
        %for who in add['who_applied']:
            %for student in students:
                %if student['id'] == who:
                    
                        <li><a href="#">{{student['first_name'] + " "+student['last_name']}}</a></li>
                        
                   
                %end
            %end
        %end
         </ul>
        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{add['uniq_adNr']}}">
            <input type="submit" value="Ta bort annons">
        </form>
%end
