#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  while (x !== 0) {
    if (typeof theFunction === 'function') {
      theFunction();
    }
    x--;
  }
};
