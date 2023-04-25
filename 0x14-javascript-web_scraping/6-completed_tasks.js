#!/usr/bin/node
/* script that computes the number of tasks
completed by user id.
*/
const request = require('request');
const webUrl = process.argv[2];
request(webUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    const completedTasksByUsers = {};
    for (let i = 0; i < body.length; i++) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
