#!/usr/bin/node
exports.callMeMoby = function (num, func) {
  let i;
  for (i = 0; i < num; i++) {
    func();
  }
};
