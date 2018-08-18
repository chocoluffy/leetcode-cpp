struct b_tree {
  int data;
  b_tree* left;
  b_tree* right;
  b_tree* parent;
}

void in_order_traversal(b_tree* n) {
  b_tree* prev = nullptr, curr = n, next;
  while(n) {
    if (!prev || prev->left == curr || prev->right == curr) { // normal case
      if (curr->left) {
        next = curr.left;
      } 
      else {
        cout << curr.data << endl;
        next = (curr.right ? curr.right : curr.parent);
      }
    }
    else if (curr.left == prev) { // go back from L child to parent.
      cout << curr.data << endl;
      next = (curr.right ? curr.right : curr.parent);
    }
    else { // go back from R child to parent.
      next = curr.parent;
    }
    prev = curr;
    curr = next;
  }
}