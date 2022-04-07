#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(function (elem) {
    if (elem === searchElement) {
      counter++;
    }
  });
  return counter;
};
