$(document).ready(function() {
    checkLogIn();
    checkCreateEmployer();
    checkCreateStudent();
    showHide();
    give_emplyers_more_info();
    set_localstorage_val_for_ad();
    mission_control();
    edit_mission();
    edith_file();
    thanks_for_applying();
    check_if_feedback_should_display();


});
function checkLogIn(){
    $('#logIn').submit(function(event){
         event.preventDefault(event);
        $.ajax({
            type: 'POST',
            url: '/ajax',
            data: $(this).serialize(),
            success: function(response) {
                   if (response == 'ok'){
                    document.getElementById("logIn").submit();
                   }
                   else if(response=='error'){
                       $('#error').html('Fel användarnamn eller lösenord!');
                    var errordisplay = document.getElementById("error");
                    errordisplay.style.display = "block";
                   }
                   else{
                       $('#error').html('Något har blivit fel!');
                   }
               }
        });
      });
}

function checkCreateEmployer(){
    $('#create_employer').submit(function(event){
        event.preventDefault(event);

        var company_name = document.getElementById("company_name"),
            org_nr = document.getElementById("org_nr"),
            fname = document.getElementById("first_name"),
            lname = document.getElementById("last_name"),
            password = document.getElementById("password"),
            error = document.getElementById("error");
        //Email-validering:
        var email = document.getElementById("email");
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))
        {
            $.ajax({
                type: 'POST',
                url: '/ajax_create_user',
                data: $(this).serialize(),
                success: function(response) {
                       if (response == 'ok'){
                        document.getElementById("create_employer").submit();
                       }
                       else if(response=='User exists'){
                           //$('#error').html('Det finns redan en användare med angiven email!');
                       }
                       else if(response=='Bad input'){
                           //$('#error').html('Du måste skriva in en email!');
                       }
                       else{
                           //$('#error').html('Något har blivit fel!');
                       }
                   }
        });
        }else{
            alert("Du måste ange en hel och riktig mailadress. Med @ och allt.");
            email.style.borderColor = "red";
            return false;
            /*
            error.innerHTML("Du måste ange hela din mailadress. Med @ och allt.");

            Denna finns här ifall man vill i ett senare skede göra så att det visas ett felmeddelande PÅ sidan i <p id=error>
            istället för en popup-ruta
            */
        }
        //Email-validation end
/*
        //BLANK Check START
        if (company_name.value == null || org_nr.value == null || fname.value == null || lname.value == null
        || email.value == null || password.value == null){
            alert("Nu har du nog missat fylla i ett fällt.");
        }*/
        //BLANK Check END

      });
}

function checkCreateStudent(){
    $('#create_student').submit(function(event){
        event.preventDefault(event);
        //Email-validering:
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))
        {
            $.ajax({
                type: 'POST',
                url: '/ajax_create_user',
                data: $(this).serialize(),
                success: function(response) {
                       if (response == 'ok'){
                        document.getElementById("create_student").submit();
                       }
                       else if(response=='User exists'){
                           $('#error').html('Det finns redan en användare med angiven email!');
                       }
                       else if(response=='Bad input'){
                           $('#error').html('Du måste skriva in en email!');
                       }
                       else{
                           $('#error').html('Något har blivit fel!');
                       }
                   }
            });
        }
        else{
            /*error.innerHTML("Du måste ange hela din mailadress. Med @ och allt.");

            Denna finns här ifall man vill i ett senare skede göra så att det visas ett felmeddelande PÅ sidan i <p id=error>
            istället för en popup-ruta
            */
            alert("Du måste ange en hel och riktig mailadress. Med @ och allt.");
            email.style.borderColor = "red";
            return false;
        }

        //Email-val end

      });
}

function give_emplyers_more_info(){
    $('#toggle_how_it_works').click(function(){
        $('#employer_how_it_works').slideToggle('slow');
    });
}

function set_localstorage_val_for_ad(){
    $('.go_to_ad').click(function functionName() {
        val = $(this).data( 'value' );
        localStorage.setItem("clicked_ad", val);
    });
}

// För att dölja/visa annonser:
function showHide() {
     $('.add').click(function(){
         $(this).children('.showMore').toggle();

         if ($(this).children('.showMore').is(':visible')) {
             $(this).children('.arrow').html("<");
         }
         else {
            $(this).children('.arrow').html(">");
         }
     });
}

// För att visa feedback meddelande vid ansökan till annons:
function check_if_feedback_should_display() {
    if(sessionStorage.getItem("name")) {
        document.getElementById("thanks_for_applying").style.display = 'block';
        sessionStorage.clear();
    }
}

function thanks_for_applying() {
    $('.sok_annons').submit( function () {
        sessionStorage.setItem("name", "applied");
    } );
}

// SLUT visa feedback-meddelande

function mission_control(){
    $('.misson_info_control').click(function() {
        clicked_parent = $(this).parents('li');
        open_close_mission(clicked_parent);

    });
}

function open_close_mission(clicked_parent){
    $('.small').each(function(){
        $(this).removeClass('small');
    });
    $('.big').each(function(){
        $(this).find('.mission_info').slideToggle('slow');
        $(this).removeClass('big');
        $(this).find('.edit_mission_info').show();
        $(this).find('.fileToUploadLabel').hide();
        $(this).find('select').hide();

        exit_edit_mode($(this));
    });
    pos_cicked = clicked_parent.position();
    list_to_make_samll = [];
    $('.pre_missions').find('li').each(function() {
        pos = $(this).position();
        if (pos.top == pos_cicked.top){
            list_to_make_samll.push($(this))
        }
    });
    $.each(list_to_make_samll, function() {
        $(this).addClass('small');
    });
    clicked_parent.addClass('big');
    clicked_parent.find('.mission_info').slideToggle();
}

function edit_mission(){
    $('.edit_mission_info').find('.btn').click(function() {
        $(this).parents('.edit_mission_info').hide();
        clicked_parent = $(this).parents('li');
        open_close_mission(clicked_parent);
        enter_edit_mode(clicked_parent);

    });


    $('.edit_mission_btn').click(function(){
        clicked_parent = $(this).parents('li');
        if($(this).html()== 'Redigera'){
            enter_edit_mode(clicked_parent);
        }
        else{
            clicked_parent.find('.update_info').submit();
            exit_edit_mode(clicked_parent);
        }
    });
}

function enter_edit_mode(clicked_parent) {
    clicked_parent.addClass('edit');
    clicked_parent.find('.edit_mission_btn').html('Spara');
    clicked_parent.find('li').hide();
    clicked_parent.find('select').show();
    clicked_parent.find('.edit_key').show();
    clicked_parent.find('input').show();
    clicked_parent.find('.display_or_not').show();
    clicked_parent.find('.add_one_key').show();
    clicked_parent.find('.fileToUploadLabel').show();
    clicked_parent.find('.mission_link').find('a').hide();
    remove_key();
    handle_input();
    img_handleing();
}

function exit_edit_mode(clicked_parent){
    clicked_parent.find('.edit_mission_btn').html('Redigera');
    clicked_parent.find('li').show();
    clicked_parent.find('select').hide();
    clicked_parent.find('.edit_key').hide();
    clicked_parent.find('input').hide();
    clicked_parent.find('.type_container').find('input').hide();
    clicked_parent.find('.add_one_key').hide();
    clicked_parent.find('.fileToUploadLabel').hide();
    clicked_parent.find('.mission_link').find('a').show();
    clicked_parent.removeClass('edit');
}

function handle_input(){

    $('.add_one_key').click(function() {
        var num = $(this).parents('.key_continer').data('add');
        var inputNode = '<div class="edit_key" style="display:inline-block"><div class="remove_key">X</div><input type="text" value="" name="add_key_'+num+'" class="add_key" style="display:inline-block" maxlength="20" autofocus><div>';
        var add_here = $(this).siblings('.keys');
        $(inputNode).appendTo(add_here);
        $('.keys').find('input:last').focus();
    });

    $('.keys').on('keypress', '.add_key', function(key){
        if(key.which == 13) {
            var num = $(this).parents('.key_continer').data('add');
            var inputNode = '<div class="edit_key" style="display:inline-block"><div class="remove_key">X</div><input type="text" value="" name="add_key_'+num+'" class="add_key" style="display:inline-block" maxlength="20" autofocus><div>';
            var add_here = $(this).parents('.keys');
            $(inputNode).appendTo(add_here);
            $('.keys').find('input:last').focus();
          }
    });
}

function img_handleing(){
    $('.fileToUpload').change(function(){
        var parten = $(this).parents('.circle')
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function(){
                var dataURL = reader.result;
                parten.css('background-image', 'url('+dataURL+')');
            }
            reader.readAsDataURL(this.files[0])
        }
        $(this).siblings('.fileToUploadLabel').show();
      });
}

function remove_key() {
    $('.keys').on('click', '.remove_key', function(){
        $(this).parents('.edit_key').remove();
    });

    $('.keys').on('focusout', '.add_key', function(){
        if($(this).val().length == 0)
            $(this).parents('.edit_key').remove();
    });
}

function update_mission(){
    $('.edit_mission_btn').click(function(){
        if ( $(this).html() == 'Spara' ){

        }
        else{
            console.log('Något har gått fel!');
        }
      });
}

function edith_file(){
    $("input:file").change(function (){
    $('.fileToUploadLabel').hide();
    $(this).parents('.circle').css('background-image','$(this).val()');



   });

}

//Skapa annons
function createAdValid(){
    var error = document.getElementById("error");
    var ad_title = document.getElementById("ad_title");
    var ad_text = document.getElementById("ad_text");
    if(ad_title.value == ""){
        alert("Var vänlig ange en annonstitel.");
        ad_title.style.borderColor = "red";
        error.innerHTML("Var vänlig ange en annonstitel.");
        return false;
    }else if(ad_text.value == ""){
        alert("Var vänlig ange en kort beskrivande text till din annons.");
        ad_text.style.borderColor = "red";
        error.innerHTML("Var vänlig ange en kort beskrivande text till din annons.");
        return false;
    }else{
        return true;
    }
}

function menuSetUp(){
 document.getElementsByClassName("menu").style.display = "none";
}
function showHideMenu(){
    var meny = document.getElementsByClassName("menu");

    var knapp = document.getElementById("menyknapp");

    if (meny.style.display == "block"){
        meny.style.display = "none";
        knapp.src = "../img/menyicons/kryss.png";

    }else if (meny.style.display == "none"){
        meny.style.display = "block";
        knapp.src = "../img/menyicons/menyicon2.png";
    }
    alert("fgh");
}
