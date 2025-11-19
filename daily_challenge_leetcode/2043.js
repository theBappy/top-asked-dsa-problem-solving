
var Bank = function (balance) {
    this.balance = balance;
    this.n = balance.length;
};

Bank.prototype.transfer = function (account1, account2, money) {
    if (account1 > this.n || account2 > this.n || this.balance[account1 - 1] < money) {
        return false;
    }

    this.balance[account1 - 1] -= money;
    this.balance[account2 - 1] += money;
    return true;
};

Bank.prototype.deposit = function (account, money) {
    if (account > this.n) {
        return false;
    }

    this.balance[account - 1] += money;
    return true;
};


Bank.prototype.withdraw = function (account, money) {
    if (account > this.n || this.balance[account - 1] < money) {
        return false;
    }

    this.balance[account - 1] -= money;
    return true;
};
