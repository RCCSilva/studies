#include <iostream>
using namespace std;

class Node {    
  public:
    int value;
    Node* next;
    Node(int v, Node* n) {
        value = v;
        next = n;
    }
};

void removeMiddle(Node* node) {
    *node = *(node -> next);
}

int main() {
    Node n2 = Node(2, NULL);
    Node n1 = Node(1, &n2);
    Node n0 = Node(0, &n1);

    removeMiddle(&n1);

    Node *x = &n0;
    while (x) {
        cout << x -> value << "\n";
        x = x -> next;
    }   
}