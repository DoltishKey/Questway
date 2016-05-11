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
    		        	<!--<div class="icon circle"></div>-->
                        <img src="/static/img/phone-call.svg" class="centered_icon" alt="Phone">
    		            <p>{{student[5]}}</p>
	            	</div>
                    <div class="line"></div>
    	        	<div class="contact_info">
                        <img src="/static/img/envelope.svg" class="centered_icon" alt="Mail">
    		        	<p>{{student[6]}}</p>
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
            %if len(grading) > 0:
                <div class="pre_missions">
                    <div>
                        <h2>Genomförda uppdrag</h2>
                        <ul>
                            %for grade in grading:
                                %if this_user == True:
                                    <li class="item">

                                        <form class="update_info" action="/edit_mission/{{user_id}}/{{grade[2]}}" method="POST" enctype="multipart/form-data">
                                            %if grade[4] == 1:
                                                <div class="edit_mission_info">
                                                    <div>
                                                        <h4>{{grade[0]}}</h4>
                                                        <h4 class="status">Uppdraget visas inte på din profil</h4>
                                                        <div class="btn">Redigera och visa</div>
                                                    </div>
                                                </div>
                                            %end
                                            <div class="edit_mission_btn ">Redigera</div>
                                            <div class="img circle" style="background-image:url(../{{grade[3]}});">
                                                <label for="fileToUpload_{{grade[2]}}" class="fileToUploadLabel">Ladda upp en bild</label>
                                                <input type="file" name="fileToUpload_{{grade[2]}}" class="fileToUpload" id="fileToUpload_{{grade[2]}}">
                                            </div>
                                            <div class="mission_general">
                                                <h4>{{grade[0]}}</h4>
                                                <div class="type_container">
                                                    <h3>{{grade[8]}}</h3>
                                                    <input type="text" name="mission_type_{{grade[2]}}" value="{{grade[8]}}">
                                                </div>
                                                <div class="btn misson_info_control">Kolla in!</div>
                                                <div class="mission_info">
                                                    <div class="mission_feedback">
                                                        <p>"{{grade[5]}}"<span> - {{grade[0]}}</span></p>
                                                        <div class="grade_bar_container">
                                                            <div>
                                                                <h4>Betyg från {{grade[0]}}:</h4>
                                                                <div class="grade_bar">
                                                                    % grade_calc = (float(grade[6])/float(5))*float(100)
                                                                    <div style="width: {{grade_calc}}%" class="grade_mission" >
                                                                        <p>med {{student[0]}}</p>
                                                                    </div>
                                                                </div>
                                                                <p>Inte så nöjd!</p>
                                                                <p>Mycket nöjd!</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="key_continer nr_{{grade[2]}}">
                                                        <h4>Kompetenser som krävdes:</h4>
                                                        <ul class="keys">
                                                            % for skill in grading_skills:
                                                                %if skill[1] == grade[2]:
                                                                    <li>{{skill[0]}}</li>
                                                                    <div class="edit_key">
                                                                        <div class="remove_key">X</div>
                                                                        <input type="text" name="add_key_{{grade[2]}}" value="{{skill[0]}}" class="add_key" maxlength="20">
                                                                    </div>
                                                                %end
                                                            %end
                                                        </ul>
                                                        <p class="add_one_key">Lägg till +</p>
                                                        <div class="display_or_not">
                                                            %if grade[4] == int(2):
                                                                <input type="checkbox" name="display_{{grade[2]}}" value="True" checked>Visa uppdraget på din profil
                                                            %else:
                                                                <input type="checkbox" name="display_{{grade[2]}}" value="True">Visa uppdraget på din profil
                                                            %end
                                                        </div>
                                                    </div>
                                                    <div class="mission_link">
                                                        <h4>Länk till resultatet:</h4>
                                                        <a href="#">{{grade[7]}}</a>
                                                        <input type="text" name="url_{{grade[2]}}" value="{{grade[7]}}">
                                                    </div>
                                                </form>
                                            </div>
                                        </div>
                                    </li>
                                %else:
                                    %if grade[4] != 1:
                                    <li class="item">
                                            <div class="img circle" style="background-image:url(../{{grade[3]}});">
                                            </div>
                                            <div class="mission_general">
                                                <h4>{{grade[0]}}</h4>
                                                <div class="type_container">
                                                    <h3>{{grade[8]}}</h3>
                                                </div>
                                                <div class="btn misson_info_control">Kolla in!</div>
                                                <div class="mission_info">
                                                    <div class="mission_feedback">
                                                        <p>"{{grade[5]}}"<span> - {{grade[0]}}</span></p>
                                                        <div class="grade_bar_container">
                                                            <div>
                                                                <h4>Betyg från {{grade[0]}}:</h4>
                                                                <div class="grade_bar">
                                                                    % grade_calc = (float(grade[6])/float(5))*float(100)
                                                                    <div style="width: {{grade_calc}}%" class="grade_mission" >
                                                                        <p>med {{student[0]}}</p>
                                                                    </div>
                                                                </div>
                                                                <p>Inte så nöjd!</p>
                                                                <p>Mycket nöjd!</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="key_continer nr_{{grade[2]}}">
                                                        <h4>Kompetenser som krävdes:</h4>
                                                        <ul class="keys">
                                                            % for skill in grading_skills:
                                                                %if skill[1] == grade[2]:
                                                                    <li>{{skill[0]}}</li>
                                                                %end
                                                            %end
                                                        </ul>
                                                        <p class="add_one_key">Lägg till +</p>
                                                    </div>
                                                    <div class="mission_link">
                                                        <h4>Länk till resultatet:</h4>
                                                        <a href="#">{{grade[7]}}</a>
                                                    </div>
                                            </div>
                                        </div>
                                    </li>
                                    %end
                                %end
                            %end
                        </ul>
                    </div>
                </div>
            %end

		</main>
		%include('footer.tpl')
	</body>
</html>
