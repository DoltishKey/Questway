$(document).ready(function() {
	checkLogIn();
	checkCreateEmployer();
	checkCreateStudent();
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
