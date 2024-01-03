#!/usr/bin/node
const cd = require('cd');
cd.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
