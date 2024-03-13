#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
    let x;
  while (x !== 0) {
    if (typeof theFunction === 'function') {
      theFunction();
    }
    x--;
  }
};
