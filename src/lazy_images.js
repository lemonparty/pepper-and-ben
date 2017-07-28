import $ from "jquery";
import throttle from "throttle-debounce/throttle";

const LazyImages = {
	buffer: 500,

	init() {
		// load images onscreen at init
		this.checkScroll();

		// load additional images on scroll
		const lazyScroll = throttle(300, this.checkScroll.bind(this));

		$(document).on("scroll", () => {
			lazyScroll();
		});
	},

	checkScroll() {
		$("[data-lazy-image]:onScreen").each(function onScreen() {
			LazyImages.loadImage($(this));
		});
	},

	loadImage(el) {
		el.addClass("isLoading")
		const src = el.attr("data-lazy-image") || "http://lorempixel.com/1000/1000/animals/";
		const img = new Image();

		// remove the data attribute to keep it from loading again
		el.removeAttr("data-lazy-image");

		$(img).on("load", () => {
			el.append(img);
			$(img).css("opacity");
			el.removeClass("isLoading");
		}).attr("src", src)
	},
};

// add an onScreen selector to zepto
$.expr[":"].onScreen = (elem) => {
	const $window = $(window);

	if (!LazyImages.windowHeight) {
		LazyImages.windowHeight = $window.height();
	}

	const buffer = LazyImages.buffer || 0;
	const windowTop = $window.scrollTop();
	const windowBottom = windowTop + LazyImages.windowHeight;
	const rect = elem.getBoundingClientRect();
	const top = rect.top + windowTop;
	const bottom = rect.bottom + windowTop;

	const topIsVisible = top >= (windowTop - buffer) &&
		top < (windowBottom + buffer);

	const bottomIsVisible = bottom > (windowTop - buffer) &&
		bottom <= (windowBottom + buffer);

	const isBiggerThanScreen = (rect.height != null) &&
		rect.height > LazyImages.windowHeight &&
		top <= (windowTop - buffer) &&
		bottom >= (windowBottom + buffer);

	return topIsVisible || bottomIsVisible || isBiggerThanScreen;
};

export default LazyImages;
