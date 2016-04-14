<header>
		<div class="courtesyNav">
				<p class="courtesyNavItem">Inloggad som <strong>{{user}}</strong></p>
		</div>
		<h1>Questway</h1>
		<nav class="menu">
				%from bottle import request

				%if request.path == '/admin':
					<a class="currentMenuItem" href="/admin">Start</a>
				%else:
					<a href="/admin">Start</a>
				%end

				%if request.path == '/allMissions':
					<a class="currentMenuItem" href="">Uppdrag</a>
				%else:
					<a href="">Uppdrag</a>
				%end


				%if request.path == '/edit':
					<a class="currentMenuItem" href="">Redigera</a>
				%else:
					<a href="">Redigera</a>
				%end


				%if request.path == '/log_out':
					<a class="currentMenuItem" href="/log_out">Logga</a>
				%else:
					<a href="/log_out">Logga ut</a>
				%end
		</nav>
</header>
