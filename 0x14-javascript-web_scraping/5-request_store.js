#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`The content has been saved to ${filePath}`);
    });
  } else {
    console.error(`Failed to retrieve content. Status code: ${response.statusCode}`);
  }
});
