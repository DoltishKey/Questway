<!DOCTYPE html>
<html>

    % include('head.tpl')

	<body>
			%if user_autho == 1:
				% include('nav_students.tpl')

			%elif user_autho == 2:
				% include('nav_employers.tpl')
			%else:
				% include('nav.tpl')

			%end
		<main id="profiles">
            <div class="top">
                <div>
                    <div class="circle name_tag">
                        <h2>{{student[0]}}</h2>
                    </div>
                    <div>
                        <h4>{{education['education_info'][0]}}</h4>
                        <h3>{{education['education_info'][1]}}</h3>
                    </div>
                </div>
            </div>
            <div class="contact">
    	        <div>
    	        	<div class="contact_info">
    		        	<div class="icon circle"></div>
    		            <p>070-6645406</p>
	            	</div>
                    <div class="line"></div>
    	        	<div class="contact_info">
    		        	<div class="icon circle"></div>
    		        	<p>jcbpettersson@gmail.com</p>
    	            </div>
                </div>
            </div>
            <div class="main_education_info">
                <div class="container">
                    <div class="education_info">
                        <div class="icon circle"></div>
                        <div>
                            <p>{{education['education_info'][2]}}</p>
                        </div>
                    </div>
                    <div class="education_info">
                        <div class="icon circle"></div>
                        <div>
                            <p>{{education['education_info'][3]}}</p>
                        </div>
                    </div>
                    <div class="education_info">
                        <div class="icon circle"></div>
                        <div>
                            <p>{{education['education_info'][4]}}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="key_tags">
                <div>
                    <h2>Nyckelkompetenser</h2>
                    <ul>
                		%for tag in education['education_skills']:
                            %for skill in tag:
                                <li>{{skill}}</li>
                            %end
            			%end
        		    </ul>
                </div>
            </div>
            <div class="pre_missions">
                <div>
                    <h2>Genomförda uppdrag</h2>
                    <ul>
                        %for grade in grading:
                            <li class="item">
                                <form class="update_info">
                                    <input style="dispaly:none" name="grading_id" value="{{grade[2]}}">
                                    %if grade[4] == 1:
                                        <div class="edit_mission_info">
                                            <div>
                                                <h4>{{grade[0]}}</h4>
                                                <h4 class="status">Uppdraget visas inte på din profil</h4>
                                                <div class="btn">Redigera och visa</div>
                                            </div>
                                        </div>
                                    %end
                                    <div class="edit_mission_btn">Redigera</div>
                                    <div class="img circle">
                                        <label for="fileToUpload" class="fileToUploadLabel">Ladda upp en bild</label>
                                        <input type="file" name="fileToUpload" class="fileToUpload" id="fileToUpload">
                                    </div>
                                    <div class="mission_general">
                                        <h4>{{grade[0]}}</h4>
                                        <h3>Type</h3>
                                        <input style="dispaly:none" name="mission_type" value="{{grade[8]}}">
                                        <div class="btn misson_info_control">Kolla in!</div>
                                        <div class="mission_info">
                                            <div class="mission_feedback">
                                                <p>{{grade[4]}}<span> - {{grade[5]}}</span></p>
                                                <div class="grade_bar_container">
                                                    <div>
                                                        <h4>Betyg från {{grade[0]}}:</h4>
                                                        <div class="grade_bar">
                                                            % grade_calc = (float(grade[6])/float(5))*float(100)
                                                            <div style="width: {{grade_calc}}%" class="grade_mission" >
                                                                <p>{{student[0]}}</p>
                                                            </div>
                                                        </div>
                                                        <p>Inte så nöjd!</p>
                                                        <p>Mycket nöjd!</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="key_continer">
                                                <h4>Kompetenser som krävdes:</h4>
                                                <ul class="keys">
                                                    <li>HTML</li>
                                                    <div class="edit_key">
                                                        <div class="remove_key">X</div>
                                                        <input type="text" name="add_key" value="HTML" class="add_key" maxlength="20">
                                                    </div>
                                                    <li>CSS</li>
                                                    <div class="edit_key">
                                                        <div class="remove_key">X</div>
                                                        <input type="text" name="add_key" value="CSS" class="add_key" maxlength="20">
                                                    </div>
                                                    <li>Pythn</li>
                                                    <div class="edit_key">
                                                        <div class="remove_key">X</div>
                                                        <input type="text" name="add_key" value="Python" class="add_key" maxlength="20">
                                                    </div>
                                                    <li>UX</li>
                                                    <div class="edit_key">
                                                        <div class="remove_key">X</div>
                                                        <input type="text" name="add_key" value="UX" class="add_key" maxlength="20">
                                                    </div>

                                                </ul>
                                                <p class="add_one_key">Lägg till +</p>
                                                <div class="display_or_not">
                                                    <input type="checkbox" name="display" value="True">Visa uppdraget på din profil
                                                </div>
                                            </div>
                                            <div class="mission_link">
                                                <h4>Länk till resultatet:</h4>
                                                <a href="#">www.questway.se</a>
                                                <input type="text" name="url" value="www.questway.se">
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </li>
                        %end
                    </ul>
                </div>
            </div>

		</main>
		<footer style=" bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
</html>
