const myEmojis = ["😎", "🤑", "🥳", "🥰"];
const emojiContainer = document.getElementById("emoji-container");
const emojiInput = document.getElementById("emoji-input");
const pushBtn = document.getElementById("push-btn");
const unshiftBtn = document.getElementById("unshift-btn");
const popBtn = document.getElementById("pop-btn");
const shiftBtn = document.getElementById("shift-btn");

function renderEmojis() {
  emojiContainer.innerHTML = "";
  for (let i = 0; i < myEmojis.length; i++) {
    const emoji = document.createElement("span");
    emoji.textContent = myEmojis[i];
    emojiContainer.append(emoji);
  }
}

renderEmojis();

// adds to end
pushBtn.addEventListener("click", function () {
  emojiInputVal = emojiInput.value;
  if (emojiInputVal) {
    myEmojis.push(emojiInputVal);
  } else {
    alert("Please enter an Emoji");
  }
  renderEmojis();
});

// adds to beginning
unshiftBtn.addEventListener("click", function () {
  emojiInputVal = emojiInput.value;
  if (emojiInputVal) {
    myEmojis.unshift(emojiInputVal);
  } else {
    alert("Please enter an Emoji");
  }
  renderEmojis();
});

// removes from end
popBtn.addEventListener("click", function () {
  myEmojis.pop();
  renderEmojis();
});

// removes from start
shiftBtn.addEventListener("click", function () {
  myEmojis.shift();
  renderEmojis();
});
