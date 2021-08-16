const f= require("./main.js");

const test=[
    {
      "name": "Accessories",
      "id": 1,
      "parent_id": 20,
    },
    {
      "name": "Watches",
      "id": 57,
      "parent_id": 1
    },
    {
      "name": "Men",
      "id": 20,
      "parent_id": null
    },
    {
        "name": "Dress",
        "id": 51,
        "parent_id": 21,
      },
      {
        "name": "Skirt",
        "id": 67,
        "parent_id": 51
      },
      {
        "name": "Woman",
        "id": 21,
        "parent_id": null
      }
  ]

console.log(f(test));