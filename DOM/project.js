const boxes = document.querySelectorAll("td");
const reset = document.querySelector(".restart-button");

reset.addEventListener("click", function () {
  boxes.forEach((box) => {
    box.textContent = "";
  });
});

boxes.forEach((box) => {
  box.addEventListener("click", function () {
    if (box.textContent === "") {
      box.textContent = "X";
    } else if (box.textContent === "X") {
      box.textContent = "O";
    } else {
      box.textContent = "";
    }
  });
});
