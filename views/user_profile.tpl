<!DOCTYPE html>
<html>
    
    % include('head.tpl')
    
	<body>
		<header>
			<h1>Questway</h1>
            <nav class="menu">
                <a href="/admin">Uppdrag</a>
                <a class="currentMenuItem" href="">Profil</a>
                <a href="/log_out">Logga ut</a>
            </nav>
		</header>
        
        <div class="contentProfile">
            <div class="centerProfileInfo">
                <div id="profileName" class="roundBox_Profile">{{student['first_name']}} {{student['last_name']}}</div>
                <div class="profileDescription"><p>Jag pluggar <span class="bold">{{education['title']}}</span>. {{education['tag_line']}}</p></div>
            </div>
        </div>
        
        <div class="content2_Profile">
            <div class="center_roundBox_Profile">
                <div class="roundBox_Profile"><p>{{education['subject_one']}}</p></div>
                <div class="roundBox_Profile"><p>Ämne</p></div>
                <div class="roundBox_Profile"><p>Ämne</p></div>
            </div>
        </div>
        
        <div class="studentInformation">
            <h3>Malmö Högskola</h3>
            <p><span class="bold">Kunskaper: </span> <span class="comptences">HTML5</span><span class="comptences">CSS3</span></p>
            <p><span class="bold">Kompetenser utöver utbildningen: </span> <span>PHP</span></p>
        </div>
        
		<!--<main>
			<h1>Hello World!</h1>
			<h2>Mitt namn är {{student['first_name']}} {{student['last_name']}}</h2>
			<h3>Jag pluggar {{education['title']}}</h3>
			<h4>{{education['tag_line']}}</h4>
			<p>{{education['subject_one']}}</p>
			<p>{{education['subject_two']}}</p>
			<p>{{education['subject_three']}}</p>
			<ul>
			%for tag in education['tags']:
				<li>{{tag}}</li>
			%end
		</ul>
		<a href="{{education['url']}}">Länk till utbildningen</a>

		</main>-->
		<footer style="position: fixed; bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
