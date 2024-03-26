#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const tasksCompleted = {};

  data.forEach(person => {
    if (person.completed === true) {
      if (tasksCompleted[person.userId]) {
        tasksCompleted[person.userId]++;
      } else {
        tasksCompleted[person.userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
