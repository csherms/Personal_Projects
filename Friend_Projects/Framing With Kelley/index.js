// Hours Worked
// (start date: Wednesday, 10 November)
// (starting wage: $15/hr)
// (Pay Period = bi-weekly)

week1 = {
  monday: 0,
  tuesday: 0,
  wednesday: 0,
  thursday: 0,
  friday: 0,
  saturday: 0,
  sunday: 0,
};

week2 = {
  monday: 0,
  tuesday: 0,
  wednesday: 0,
  thursday: 0,
  friday: 0,
  saturday: 0,
  sunday: 0,
};

// Values and Keys
const week1Keys = Object.keys(week1);
const week1Values = Object.values(week1);
const week1Entries = Object.entries(week1);
const week2Keys = Object.keys(week2);
const week2Values = Object.values(week2);
const week2Entries = Object.entries(week2);
const week1HoursEl = document.getElementById("week1Hours-el");
const week2HoursEl = document.getElementById("week2Hours-el");
const week1PayEl = document.getElementById("week1Pay-el");
const week2PayEl = document.getElementById("week2Pay-el");
const totalHoursEl = document.getElementById("totalHours-el");
const totalPayEl = document.getElementById("totalPay-el");
// // May not need these...
// const week1DayForm = document.getElementById("week1Day-form");
// const week2DayForm = document.getElementById("week2Day-form");
// const week1HoursForm = document.getElementById("week1Hours-form");
// const week2HoursForm = document.getElementById("week2Hours-form");
// const submitBtn1 = document.getElementById("submitBtn-1");
// const submitBtn2 = document.getElementById("submitBtn-2");
// // May not need these end...

// Get hours for week 1
let sumOfHours1 = 0;
function getHours1(a) {
  for (let i = 0; i < a.length; i++) {
    sumOfHours1 += a[i];
  }
}
// Get hours for week 2
let sumOfHours2 = 0;
function getHours2(b) {
  for (let i = 0; i < b.length; i++) {
    sumOfHours2 += b[i];
  }
}
// Get all hours for both weeks
let sumOfAllHours = 0;
function getAllHours(a, b) {
  sumOfAllHours = a + b;
}

// Display week 1 hours
getHours1(week1Values);
week1HoursEl.textContent = "Hours: " + sumOfHours1;
//Display week 2 hours
getHours2(week2Values);
week2HoursEl.textContent = "Hours: " + sumOfHours2;
//Display all hours for both weeks
getAllHours(sumOfHours1, sumOfHours2);
totalHoursEl.textContent = "Total hours: " + sumOfAllHours;

// Get pay for week 1
let sumOfPay1 = 0;
function getPay1(a) {
  for (let i = 0; i < a.length; i++) {
    sumOfPay1 += a[i] * 15;
  }
}
// Get pay for week 2
let sumOfPay2 = 0;
function getPay2(b) {
  for (let i = 0; i < b.length; i++) {
    sumOfPay2 += b[i] * 15;
  }
}
// Get all pay for both weeks
let sumOfAllPay = 0;
function getAllPay(a, b) {
  sumOfAllPay = a + b;
}

// Display week 1 pay
getPay1(week1Values);
week1PayEl.textContent = "Week pay:" + " $" + sumOfPay1;
//Display week 2 pay
getPay2(week2Values);
week2PayEl.textContent = "Week pay:" + " $" + sumOfPay2;
//Display all pay for both weeks
getAllPay(sumOfPay1, sumOfPay2);
totalPayEl.textContent = "Total pay:" + " $" + sumOfAllPay;
