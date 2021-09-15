$(document).ready( function() {
    $(".sign-in").on("click", function() {
        $(".modal-body").load("/accounts/login");
    });
    $(".sign-up").on("click", function() {
        $(".modal-body").load("/accounts/signup");
    });
});