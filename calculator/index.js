const addBtn = document.getElementById("add_btn");
const subBtn = document.getElementById("sub_btn");
const mulBtn = document.getElementById("mul_btn");
const divBtn = document.getElementById("div_btn");
const equalBtn = document.getElementById("equal_btn");
const numInput = document.getElementById("num_input");
const answerOutput = document.getElementById("answer_output");

let sum = 0;
let dif = 0;

function add() {
  let numsArr = [];

  numsArr.push(numInput.value);

  for (let i = 0; i < numsArr.length; i++) {
    sum += parseInt(numsArr[i]);
    answerOutput.textContent = sum;
  }
  numInput.value = "";
  return sum;
}

function sub() {
  let numsArr = [];

  numsArr.push(numInput.value);

  for (let i = 0; i < numsArr.length; i++) {
    dif = dif - numsArr[i];
    answerOutput.textContent = dif;
  }
  numInput.value = "";
  return dif;
}

function equal() {
  return answerOutput.value;
}
