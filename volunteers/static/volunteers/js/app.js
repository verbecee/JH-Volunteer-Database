//Test if JS is Working
// alert('Hi I am functioning ....')

$(document).ready(function () {
    // Select the first tab on document ready to focus
    $("#nav-profile-tab").css("borderTop", "2px solid red");
});

$(".nav-tabs").click(function () {
    $("#nav-profile-tab").css("borderTop", "");
    // alert("Handler for .click() called.");
});
$("#nav-profile-tab").click(function () {
    $("#nav-profile-tab").css("borderTop", "2px solid red");
    console.log("Hi");
});

// $(".nav-item").click(function () {
//     $(".nav-item").toggleClass("nav-items");
// });

var links = document.querySelectorAll("#nav-tab .nav-item");
// console.log(links)

var i;
for (i = 0; i < links.length; i++) {
    // console.log(i, links[i])
    this.className = "nav-item";
    links[i].addEventListener("click", function (e) {
        // console.log(e)
        // // console.log(links[i])
        console.log(this.innerText);
        console.log(i);
        this.className = "nav-items";
    });
}

// //Set the borderTop of first tab
// document.ready(function () {
// document.getElementById('nav-profile-tab').style.borderTop = "2px solid red"

// })
// fills the volunteer foreign fields with last_name and first_name from profile tab

// Change styles of tabs on click