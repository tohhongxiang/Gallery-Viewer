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
