// this is how you would set up an api request
// fetch("https://reqres.in/api/users")
//   .then((res) => {
//     if (res.ok) {
//       console.log("Success");
//     } else {
//       console.log("Not successful");
//     }
//   })
//   .then((data) => console.log(data))
//   .catch((error) => console.log("Error"));

// this is how to post information
fetch("https://reqres.in/api/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: "User 1",
  }),
})
  .then((res) => {
    return res.json();
  })
  .then((data) => console.log(data))
  .catch((error) => console.log("Error"));
