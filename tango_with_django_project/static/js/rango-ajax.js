$(document).ready(function() {
    alert("JJJ");
    $("#about-btn").click(function(event) {
        /* Act on the event */
        alert("You clicked the button using JQuery.")
    });
    $('p').hover(function() {
        /* Stuff to do when the mouse enters the element */
        $(this).css('color', 'red');
    }, function() {
        /* Stuff to do when the mouse leaves the element */
        $(this).css('color', 'blue');
    });
});