// Approach (Simple Simulation)
//T.C. : O(n) for Bank(), O(1) for withdraw(), transfer() and deposit()
//S.C. : O(n) for storing balance for each object
class Bank {
public:
    vector<long long> balance;
    int n;

    Bank(vector<long long>& balance) {//O(n)
        n = balance.size();
        this->balance = balance;
    }
    
    bool transfer(int account1, int account2, long long money) { //O(1)
        if(account1 > n || account2 > n || balance[account1-1] < money) {
            return false;
        }

        balance[account1 - 1] -= money;
        balance[account2 - 1] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {//O(1)
        if(account > n)
            return false;
        
        balance[account - 1] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {//O(1)
        if(account > n || balance[account - 1] < money)
            return false;
        
        balance[account - 1] -= money;
        return true;
    }
};