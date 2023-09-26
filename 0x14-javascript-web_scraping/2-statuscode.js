#!/usr/bin/node

const url = process.argv[2];
const request = new Request(url, {
  method: 'GET'
});

fetch(request)
  .then((response) => {
    console.log('code: ' + response.status);
  });
