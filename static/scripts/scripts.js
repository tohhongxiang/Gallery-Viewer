$(document).keydown(function(e) { //on keydown
if (e.keyCode === 37) { // if left arrow
   // Previous
   $(".carousel-control-prev").click(); // click previous 
   return false;
}
if (e.keyCode === 39) { // if right arrow
   // Next
   $(".carousel-control-next").click(); // click next
   return false;
}
});

$(function() {
	return $(".carousel.lazy").on("slide.bs.carousel", function(e){
		var lazy;
		lazy = $(e.relatedTarget).find("img[data-src]");
		lazy.attr("src", lazy.data("src"));
		lazy.removeAttr("data-src");
	});
});
