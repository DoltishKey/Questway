<!--
Skriven av: Sofia (HTML+CSS)
-->
<!DOCTYPE html>
<html>

    % include('head.tpl')

    <body>
        <div id="wrapper">
            %if user_autho == 1:
                % include('nav_students.tpl')

            %elif user_autho == 2:
                % include('nav_employers.tpl')
            %else:
                % include('nav.tpl')

            %end
            <div id="content_wrap">
                <div id="error_message_container_div">
                    <img src="/static/img/cancel.svg" alt="Ikon för fel">

                    <p class="error">{{error_message}}</p>

                    %if user_autho == 1 or user_autho == 2:
                        <p><a href="/admin"> &lt;&lt;&lt; Gå tillbaka till startsidan</a></p>
                    %else:
                        <p><a href="/">&lt;&lt;&lt; Gå tillbaka till startsidan</a></p>
                    %end
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>

</html>
