<!--
Skriven av: Sofia (HTML + CSS)
-->
<!DOCTYPE html>
<html>
    %include('head.tpl')
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
                <div id="container_of_container">
                    <h1 class="help_heading">Hjälp</h1>
                    <h2>Vanliga frågor</h2>
                    <div class="container_help_content">
                        <div>
                            <h3>Fråga 1</h3>
                            <p class="bold">Svar: </p>
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                            <h3>Fråga 2</h3>
                            <p class="bold">Svar: </p>
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                            <h3>Fråga 3</h3>
                            <p class="bold">Svar: </p>
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                            <h3>Fråga 4</h3>
                            <p class="bold">Svar: </p>
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
                        </div>
                    </div>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>

</html>
