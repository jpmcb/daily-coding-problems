// A XOR linked list is a more memory efficient doubly linked list.
// Instead of each node holding next and prev fields, it holds a field named both, 
// which is an XOR of the next node and the previous node. 
// Implement an XOR linked list; it has an add(element) which adds the element to the end, 
// and a get(index) which returns the node at index.

#include <stdio.c>

struct Node {
    int data;
    struct Node *both;
};

struct Node * XOR(struct Node * prev, struct Node * next) {
    return prev ^ next;
}

struct Node * add(struct Node ** head, int input) {
    // Allocate a new node in the LL
    struct Node * newNode = malloc(sizeof(struct Node));
    newNode->data = input;
    
    if(*head == NULL) {
        head = newNode;
        struct Node * next = XOR()
    } else {

    }
} 

int get(int index) {

}

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
