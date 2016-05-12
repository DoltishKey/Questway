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
                    <h2 class="about_questway">Om Questway</h2>
                    <div class="about_us_info">
                        <p>Questway är en tjänst för studenter på Malmö Högskola och företag i Malmöregionen. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. </p>
                        <p>Questway har utvecklats under ett projektarbete i kursen Systemutveckling och Projekt 1 av fyra studenter på Malmö Högskola. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.</p>
                    </div>
                </div>
            </div>
            %include('footer.tpl')
        </div>
    </body>
</html>
