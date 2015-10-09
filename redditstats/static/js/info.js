/*jslint browser: true*/
/*jslint plusplus: true*/
/*global $, jQuery, alert*/



function rotateTerm() {

    "use strict";

    var ct = $("#rotate").data("term") || 0;
    $("#rotate").data("term", ct == $terms.length - 1 ? 0 : ct + 1).text($terms[ct]).fadeIn()
              .delay(6000).fadeOut(2000, rotateTerm);
}


$(document).ready(function () {
    
    
    "use strict";

    rotateTerm();
    
});
