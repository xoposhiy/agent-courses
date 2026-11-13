# Project code: stanford-oval/genie-worksheets: web/static/js/index.js

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/static/js/index.js) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/static/js/index.js)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```js
window.HELP_IMPROVE_VIDEOJS = false;


$(document).ready(function() {
    // Check for click events on the navbar burger icon

    var options = {
			slidesToScroll: 1,
			slidesToShow: 1,
			loop: true,
			infinite: true,
			autoplay: true,
			autoplaySpeed: 5000,
    }

		// Initialize all div with carousel class
    var carousels = bulmaCarousel.attach('.carousel', options);
	
    bulmaSlider.attach();

})

```
