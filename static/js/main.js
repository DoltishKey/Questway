$(document).ready(function() {
	checkLogIn();
	checkCreateEmployer();
	checkCreateStudent();
    showHide();
	give_emplyers_more_info();
	set_localstorage_val_for_ad();
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