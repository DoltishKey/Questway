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





function showHide() {
     $('.add').click(function(){
         $(this).children('.showMore').toggle();

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
