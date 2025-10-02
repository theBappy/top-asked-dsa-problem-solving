/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function (numBottles, numExchange) {
  let empty = numBottles;
  let drunk = numBottles;
  while (empty >= numExchange) {
    empty -= numExchange;
    empty++;
    drunk++;
    numExchange++;
  }
  return drunk;
};


//  Sridhara Acharya’s / quadratic formula
var maxBottlesDrunk = function (numBottles, numExchange) {
  return Math.floor(
    numBottles +
      (-2 * numExchange +
        3 +
        Math.sqrt(
          4 * numExchange * numExchange + 8 * numBottles - 12 * numExchange + 1
        )) /
        2
  );
};
