$(document).ready(function() {
	checkLogIn();
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
	        		$('#logIn').submit();  	
           		}
           		else{
	           		$('#error').html('Fel användarnamn eller lösenord!');	
           		}
		   	}
		});
  	});	
}

        