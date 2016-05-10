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
        
        <p class="error">{{error_message}}</p>
        
        %if user_autho == 1 or user_autho == 2:
            <p><a href="/admin">Gå tillbaka till startsidan</a></p>
        %else:
            <p><a href="/">Gå tillbaka till startsidan</a></p>
        %end
         
    %include('footer.tpl')
    </body>

</html>