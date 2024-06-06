// $("h1").click(function () {
//   console.log("There was a click!");
// });

// This will automatically add the click handler to all 'li' tags
// $("li").click(function () {
//   console.log("any li was clicked!");
// });

// This keyword refers to the current tag being referenced
$("h1").click(function () {
  $(this).text("I was changed!");
});

// Whenever a key is pressed inside the first input box
$("input")
  .eq(0)
  .keypress(function (event) {
    // Will toggle the class on any keypress
    // $('h3').toggleClass('turnBlue')

    // console.log(event)

    // Will only toggle the class when the enter key is pressed
    if (event.which === 13) {
      $("h3").toggleClass("turnBlue");
    }
  });

// Toggles the class on double click or when the mouse is hovering over the tag
$('h1').on('dblclick', function() {
  $(this).toggleClass('turnBlue')
})

$('h1').on('mouseenter', function() {
  $(this).toggleClass('turnBlue')
})

// Adding animations
$('input').eq(1).on('click', function () {
  $('.container').fadeOut(3000)
})

$('input').eq(1).on('dblclick', function () {
  $('.container').slideUp(3000)
})
