<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
        <title>Admin</title>
    </head>
	<body>
        % include('nav_employers.tpl')
		<main id="admin_start_employer">
            <div id="employer_how_it_works" class="col">
                <h2>Hur funkar det?</h2>
                <div>
                    <p>Bacon ipsum dolor amet pancetta chuck picanha shoulder.
                        T-bone sirloin bresaola ham hock beef ribs leberkas, brisket
                        turkey pancetta boudin chicken tenderloin. Tri-tip sirloin capicola
                        chuck, frankfurter drumstick ball tip. Pork short ribs bresaola, meatloaf
                        pastrami prosciutto salami. Picanha fatback shank brisket short ribs. Ground
                        round landjaeger sausage t-bone pork.
                    </p>
                </div>
            </div>
            <div id="toggle_how_it_works">
                <p>Hur funkar det?</p>
            </div>
            <div class="employers_add_new_ad col">
                <div>
                    <a class="btn" href="/showadds">Lägg till annons</a>
                </div>
            </div>
            <div class="emloyers_all_adds col">
                <h2>Dina aktuella annonser</h2>
                <div>
                    <ul>
                        %for i in annons:
                	       %if i['creator'] == user_id:
        		                <a href="#" data-value="{{i['uniq_adNr']}}" class="go_to_ad">
                                    <li>
                                        <div>
                                            <h3>{{i['ad_title']}}</h3>
                                            <p>{{len(i['who_applied'])}} ansöknignar</p>
                                        </div>
            		                    <!--<p>{{i['ad_text']}}</p>
                        		        <form  name="delete_ad" id="delete_ad" method="POST" action="/del_ad/{{i['uniq_adNr']}}">
                        		            <input type="submit" value="Ta bort annons">
                        		        </form>
                                        <a href="/give_feedback/{{i['uniq_adNr']}}">Ge feedback</a>-->
                                        <div>></div>
                                    </li>
                                </a>
        		            %end
        	            %end
                    </ul>
                </div>
            </div>
      </main>
      <footer>Copyright Questway, 2016</footer>
      <script src="/static/js/jquery.js"></script>
      <script>
          $(document).ready(function() {
              $('#toggle_how_it_works').click(function(){
                  $('#employer_how_it_works').slideToggle('slow');
              });

              $('.go_to_ad').click(function functionName() {
                  val = $(this).data( 'value' );
                  localStorage.setItem("clicked_ad", val);
              });
          });
      </script>
	</body>
</html>
