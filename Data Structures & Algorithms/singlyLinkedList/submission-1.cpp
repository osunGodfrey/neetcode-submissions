class LinkedList {
public:
    vector<int> llist;

    LinkedList() {
        this ->llist = {};

    }

    int get(int index) {
        if(index < llist.size()){
            return llist[index];
        }
        return -1;
    }

    void insertHead(int val) {
        llist.insert(llist.begin(), val);
        
    }
    
    void insertTail(int val) {
        llist.push_back(val);

    }

    bool remove(int index) {
        if(index < llist.size()){
            llist.erase(llist.begin() + index);
            return true;
        }
        return false;
        
    }

    vector<int> getValues() {
        return llist;
        
    }
};
