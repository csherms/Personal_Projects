let countEl = document.getElementById("count-el");
let saveEl = document.getElementById("save-el");
let count = 0;

function increment() {
  count += 1; // count = count + 1
  countEl.textContent = count;
}

function save() {
  let countStr = count + " - ";
  // let resetCount = (count *= 0);
  // countEl.textContent = resetCount;    this is my solution, and it worked also but I'm going with scrimbas
  countEl.innerText = 0;
  count = 0;
  saveEl.textContent += countStr;
  console.log(count);
}

function reset() {
  saveEl.textContent = "Saved Entries: ";
  count = 0;
}
