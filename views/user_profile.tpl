<!DOCTYPE html>
<html>
	<head>
		<title>Profil {{student_id}}</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="../static/css/main.css">
	</head>
	<body>
		<header>
			<h1>Questway</h1>
			%if user_autho == 1:
				% include('nav_students.tpl')

			%elif user_autho == 2:
				% include('nav_employers.tpl')
			%else:
				% include('nav.tpl')

			%end
		</header>
		<main>
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

		</main>
		<footer style="position: fixed; bottom:0px; width: 100%;">© Questway, 2016</footer>
	</body>
	<script src="/static/js/jquery.js"></script>
	<script src="/static/js/main.js"></script>
</html>
