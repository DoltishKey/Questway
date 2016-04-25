<header>
    <div class="wrap">
		<h1>Questway</h1>
		<nav class="menu">
				%from bottle import request

				%if request.path == "/login":
					<a class="currentMenuItem" href="/login">Logga in</a>
				%else:
					<a href="/login">Logga in</a>
				%end

				%if request.path == "/create":
					<a class="currentMenuItem" href="/create">Registrera</a>
				%else:
					<a href="/create">Registrera</a>
				%end


				%if request.path == 'about':
					<a class="currentMenuItem" href="">Om oss</a>
				%else:
					<a href="">Om oss</a>
				%end
		</nav>
    </div>
</header>
