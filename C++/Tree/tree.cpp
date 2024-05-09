#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int value;
    vector<Node*> children;

    Node(int val) {
        value = val;
    }

    void addChild(Node* node) {
        children.push_back(node);
    }
};

class Tree {
public:
    Node* root;

    Tree(Node* r) {
        root = r;
    }

    void traverse(Node* node) {
        cout << node->value << " ";

        for (int i = 0; i < node->children.size(); i++) {
            traverse(node->children[i]);
        }
    }
};

int main() {
    // create nodes
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    Node* node3 = new Node(3);
    Node* node4 = new Node(4);
    Node* node5 = new Node(5);

    // create tree
    Tree* tree = new Tree(node1);

    // add children to nodes
    node1->addChild(node2);
    node1->addChild(node3);
    node2->addChild(node4);
    node3->addChild(node5);

    // traverse tree
    tree->traverse(tree->root);

    return 0;
}

