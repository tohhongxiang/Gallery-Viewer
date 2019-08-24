window.onload = () => window.scroll(0,56);

// using arrow keys to control carousel
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

// lazy loading of carousel. add .lazy to carousel to allow
$(function() {
	return $(".carousel.lazy").on("slide.bs.carousel", function(e){
		var lazy;
		lazy = $(e.relatedTarget).find("img[data-src]");
		lazy.attr("src", lazy.data("src"));
		lazy.removeAttr("data-src");
	});
});

// lazy loading everything in a card
const cards = document.querySelectorAll(".card");

// lazyloading the images
const lazyLoad = target => {
	const observer = new IntersectionObserver((entries, observer) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				const img = entry.target.querySelector("img");
				const src = img.getAttribute("data-src");
				img.setAttribute("src", src);
				observer.disconnect();
			}
		});
	});
	observer.observe(target);
};

cards.forEach(lazyLoad);

const overlay = document.querySelector(".overlay");
const overlayImg = overlay.querySelector("img");
// const overlayClose = overlay.querySelector(".close");

// When image is clicked, expand it
function handleClick(e) {
	overlayImg.src = e.target.querySelector("img").src;
	overlay.classList.add("open");
}

// handles closing the expanded image
function close() {
	overlay.classList.remove("open");
}

cards.forEach(item => item.addEventListener("click", handleClick)); // select all cards, and when click, expand the image out
overlay.addEventListener("click", close); // when any click happens on the overlay, close the overlay