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
                        <h2>{{student['first_name']}}</h2>
                    </div>
                    <div>
                        <h4>{{education['title']}}</h4>
                        <h3>{{education['tag_line']}}</h3>
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
                            <p>{{education['subject_one']}}</p>
                        </div>
                    </div>
                    <div class="education_info">
                        <div class="icon circle"></div>
                        <div>
                            <p>{{education['subject_two']}}</p>
                        </div>
                    </div>
                    <div class="education_info">
                        <div class="icon circle"></div>
                        <div>
                            <p>{{education['subject_three']}}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="key_tags">
                <div>
                    <h2>Nyckelkompetenser</h2>
                    <ul>
            			%for tag in education['tags']:
            				<li>{{tag}}</li>
            			%end
        		    </ul>
                </div>
            </div>

            <div class="pre_missions">
                <div>
                    <h2>Genomförda uppdrag</h2>
                    <ul>
            			<li>
            				<div class="img circle"></div>
            				<div>
                                <h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
            				<li>
            				<div class="img circle"></div>
            				<div>
	            				<h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
            				<li>
            				<div class="img circle"></div>
            				<div>
                                <h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
            				<li>
            				<div class="img circle"></div>
            				<div>
                                <h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
            				<li>
            				<div class="img circle"></div>
            				<div>
                                <h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
            				<li>
            				<div class="img circle"></div>
            				<div>
                                <h4>Calles AB</h4>
	            				<h3>Hemsida</h3>
                                <a href="#">Kolla in!</a>
            				</div>
            			</li>
        		    </ul>
                </div>
            </div>
		</main>
		<footer style=" bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
