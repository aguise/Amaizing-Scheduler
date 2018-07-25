// All javascript and jquery

$(document).ready(function(){

	$('.nav').on('click',function(){
		var page = $(this).attr('id');
		$('#container').load(this.id);
		
		
  	});  
});

$(document).ready(function(){
	var delay = 200;
	var duration = 400;
	$(window).scroll(function(){
		if($(this).scrollTop() > delay) {
			$('.Top').fadeIn(duration);
		} else {
			$('.Top').fadeOut('fast');
		}
	});

	$('.Top').click(function(event) {
		event.preventDefault();
		$('html, body').animate({scrollTop: 200}, duration);
		return false;
	});
});