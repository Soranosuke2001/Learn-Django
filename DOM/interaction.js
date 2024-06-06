// Let's type this into the console, follow along with the video lecture

const x = document.querySelector("p")

// Show Text
x.textContent

// Reassign Text
x.textContent = "new"

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>"

// Can't do that with just textContent

/////////////////
// Attributes //
///////////////

const special = document.querySelector("#special")
const specialA = y.querySelector("a")

specialA.getAttribute("href")

specialA.setAttribute("href","https://www.amazon.com")
