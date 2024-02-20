#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId.toString();
        if (completedTasksByUser[userId] === undefined) {
          completedTasksByUser[userId] = 1;
        } else {
          completedTasksByUser[userId]++;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Failed to retrieve todo list. Status code: ${response.statusCode}`);
  }
});
