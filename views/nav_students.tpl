<header>
    <div class="wrap">
		<div class="courtesyNav">
				<p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
		</div>
		<h1>Questway</h1>
		<nav class="menu">
				%from bottle import request

				%if request.path == '/admin':
					<a class="currentMenuItem" href="/admin">Uppdrag</a>
				%else:
					<a href="/admin">Start</a>
				%end
				
				%if request.path == '/profiles/' + str(student['id']):
					<a class="currentMenuItem" href="/profiles/{{student['id']}}">Profil</a>
				%else:
					<a href="/profiles/{{student['id']}}">Profil</a>
				%end


				%if request.path == '/log_out':
					<a class="currentMenuItem" href="/log_out">Logga</a>
				%else:
					<a href="/log_out">Logga ut</a>
				%end
		</nav>
    </div>
</header>
