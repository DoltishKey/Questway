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


		</main>
		<footer style=" bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
</html>
