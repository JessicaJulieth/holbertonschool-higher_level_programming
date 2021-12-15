#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const item in list) {
    if (list[item] === searchElement) {
      i++;
    }
  }
  return i;
};
