<!DOCTYPE html>
<html>
        % include('head.tpl')
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
        		                <a href="/allMissions" data-value="{{i[0]}}" class="go_to_ad">
                                    <li>
                                        <div>
                                            <h3>{{i[1]}}</h3>
                                            %num_applications = sum(x.count(i[0]) for x in students_application)
                                            % if num_applications > 1:
                                                <p><span>{{num_applications}}</span> ansökningar</p>
                                            %elif num_applications == 1:
                                                <p><span>{{num_applications}}</span> ansökningar</p>
                                            %else:
                                                <p>Inga ansökningar</p>
                                            %end
                                        </div>

                                        <div>></div>
                                    </li>
                                </a>

        	            %end
                    </ul>
                </div>
            </div>
      </main>
      <footer>Copyright Questway, 2016</footer>
	</body>
</html>
