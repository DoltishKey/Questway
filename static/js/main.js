$(document).ready(function() {
	checkLogIn();
	checkCreateEmployer();
	checkCreateStudent();
    showHide();
	give_emplyers_more_info();
	set_localstorage_val_for_ad();
	mission_control();
	edit_mission();
});

function checkLogIn(){
	$('#logIn').submit(function(){
		event.preventDefault();
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
           		}
           		else{
	           		$('#error').html('Något har blivit fel!');
           		}
		   	}
		});
  	});
}


function checkCreateEmployer(){
	$('#create_employer').submit(function(){
		event.preventDefault();
		//validering ska in här


		$.ajax({
			type: 'POST',
			url: '/ajax_create_user',
			data: $(this).serialize(),
			success: function(response) {
           		if (response == 'ok'){
	        		document.getElementById("create_employer").submit();
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
  	});
}


function checkCreateStudent(){
	$('#create_student').submit(function(){
		event.preventDefault();
		//validering ska in här


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




//För att dölja/visa annonser för studenter
function showHide() {
     $('.add').click(function(){
         $(this).children('.showMore').toggle();

         if ($(this).children('.showMore').is(':visible')) {
             $(this).children('.arrow').html("<");
             console.log('FUNKAR') //Test
         }
         else {
            $(this).children('.arrow').html(">");
             console.log('FUNKER EJ, NU ÄR VI PÅ ELSE-SATSEN') //Test
         }
     });
}

function set(){
    document.getElementById("meny").style.display = "none";
    document.getElementById("header").style.height = "70px";
    document.getElementById("headerbottom").style.top = "70px";
    document.getElementById("downarrow").style.top = "70px";

    document.getElementById("logo1").style.left = innerWidth/2 + "px";
    document.getElementById("headerbottom").style.borderLeft = innerWidth/2 + "px" + " solid transparent"; document.getElementById("headerbottom").style.borderRight = innerWidth/2 + "px" + " solid transparent";
}
function showHideMeny() {
    var button = document.getElementById("downarrow");
    var meny = document.getElementById("meny");
    var header = document.getElementById("header");
    var botheader = document.getElementById("headerbottom");
    var arrow = document.getElementById("downarrow");

    if (meny.style.display == "none") {
        meny.style.display = "block";
        header.style.height = "230px";
        botheader.style.top = "230px";
        arrow.style.top = "230px";
        arrow.style.textTransform = "rotate(360deg)";
    } else if (meny.style.display == "block") {
        meny.style.display = "none";
        header.style.height = "70px";
        botheader.style.top = "70px";
        arrow.style.top = "70px";
    } else {
        alert("Något gick fel!");
    }

}

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
		clicked_parent.addClass('edit');
		open_close_mission(clicked_parent);
		enter_edit_mode(clicked_parent)

	});

	$('.misson_info_control').click(function(){
		clicked_parent = $(this).parents('li');
		enter_edit_mode(clicked_parent)
	});

	$('.edit_mission_btn').click(function(){
		clicked_parent = $(this).parents('li');
		if (!clicked_parent.hasClass('edit')){
			clicked_parent.addClass('edit');
			enter_edit_mode(clicked_parent);
		}
	});
}

function enter_edit_mode(clicked_parent) {
	if (clicked_parent.hasClass('edit')){
		$('.edit_mission_btn').html('Spara');
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
		update_mission()
	}
	else{
		$('.edit_mission_btn').html('Redigera');
	}

}

function handle_input(){
	$('.add_one_key').click(function() {
		var inputNode = '<div class="edit_key" style="display:inline-block"><div class="remove_key">X</div><input type="text" value="" name="add_key" class="add_key" style="display:inline-block" maxlength="20" autofocus><div>';
		var add_here = $(this).siblings('.keys');
		$(inputNode).appendTo(add_here);
		$('.keys').find('input:last').focus();
	});

	$('.keys').on('keypress', '.add_key', function(key){
		if(key.which == 13) {
			var inputNode = '<div class="edit_key" style="display:inline-block"><div class="remove_key">X</div><input type="text" value="" name="add_key" class="add_key" style="display:inline-block" maxlength="20" autofocus><div>';
			var add_here = $(this).parents('.keys');
			$(inputNode).appendTo(add_here);
			$('.keys').find('input:last').focus();
  		}
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
			$.ajax({
				type: 'POST',
				url: '/ajax_edit_mission',
				data: $(this).parents('.update_info').serialize(),
				success: function(response) {
					alert('Funkar!')
				}
			});
		}
		else{
			console.log('Något har gått fel!');
		}
  	});
}
