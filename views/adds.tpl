


%for add in adds:


            <h1>{{add['ad_title']}}</h1>
            %if add == open_ad:
                <p>{{add['ad_text']}}</p>

                <ul>
                %for who in add['who_applied']:
                    %for student in students:
                        %if student['id'] == who:

                                <li><a href="/profiles/{{student['id']}}">{{student['first_name'] + " "+student['last_name']}}</a></li>


                        %end
                    %end
                %end
                 </ul>
                <a href="/give_feedback/{{add['uniq_adNr']}}">Ge feedback</a>
                <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{add['uniq_adNr']}}">
                    <input type="submit" value="Ta bort annons">
                </form>
            %end
%end
