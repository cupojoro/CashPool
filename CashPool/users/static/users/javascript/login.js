window.onload = function pageLoad() {
    //Remove error messages after delay.
    setTimeout(function() {
        document.getElementById("invalid-email").innerHTML = "";
        document.getElementById("invalid-password").innerHTML = "";
    }, 7000);
}