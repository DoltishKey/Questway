<header>
    <div class="wrap" id="header_wrap">
		<a id="QWTitle" href="/admin"><h1>Questway</h1></a>
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
					<a class="currentMenuItem" href="/about_us">Om oss</a>
				%else:
					<a href="/about_us">Om oss</a>
				%end
		</nav>
    </div>
</header>
