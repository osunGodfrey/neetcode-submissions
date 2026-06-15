class DynamicArray {
public:
    int capacity;
    int size;
    int* arr;

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];

    }

    void set(int i, int n) {
        arr[i] = n;

    }

    void pushback(int n) {
        // int arr_size = getSize();
        // if(arr[arr_size - 1] == -1){
        //     arr[arr_size - 1] = n;
        // }else{
        //     resize();
        //     arr[arr_size - 1 + 1] = n;
        // }
        if(size == capacity){
            resize();
            // size++;
            arr[size] = n;
            size++;
        }else{
            // size++;
            arr[size] = n;
            size++;
        }

    }

    int popback() {
        // int arr_size = getSize();
        // int val = arr[size];
        // arr[arr_size - 1] = -1;
        size--;
        // return val;
        return arr[size];
    }

    void resize() {
        capacity *= 2;
        int* new_arr = new int[capacity];
        // int size = getSize();
        for(int i = 0; i < size; i++){
            new_arr[i] = arr[i];
        }
        delete[] arr;
        arr = new_arr;

    }

    int getSize() {
        // int size = 0;
        // int index = 0;
        // int cap  = getCapacity();
        // while(index < cap){
        //     if(arr[index] == -1){
        //         break;
        //     }
        //     index++;
        //     size++;
        // }
        return size;

    }

    int getCapacity() {
        // capacity = sizeof(*arr) / sizeof(arr[0]);
        return capacity;
    }

};
