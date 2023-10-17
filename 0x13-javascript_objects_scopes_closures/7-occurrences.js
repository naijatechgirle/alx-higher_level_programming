#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let b = 0; b < list.length; b++) {
    if (list[b] === searchElement) {
      count += 1;
    }
  }
  return count;
};
