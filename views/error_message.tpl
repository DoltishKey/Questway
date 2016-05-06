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
        <p>{{error_message}}</p>
            
    </body>

</html>