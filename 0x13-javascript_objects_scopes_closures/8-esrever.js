#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  const rlist = [];
  for (i = list.length - 1; i > -1; i--) {
    rlist.push(list[i]);
  }
  return rlist;
};
