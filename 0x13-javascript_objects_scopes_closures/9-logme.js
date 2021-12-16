#!/usr/bin/node

exports.logMe = function (item) {
    console.log(item.forEach + ': ' + item);
    item.forEach++;
}
