// when refer to property using pointer, use `->`, when directly access object's property, use `.`
// this method uses relatively more stack space, can use less space by:
// use curr pointer to go leftest at first, then only expand during `pop()` and print it out.

struct bst_node {
  int data;
  bst_node* left;
  bst_node* right;
}

void parse_bst(bst_node* t) {
  stack<pair<node*, bool>> s;
  s.emplace(t, false);
  while(!s.empty()) {
	pair<node*, bool> curr_pair = s.pop();
    bst_node* curr = curr_pair.first;
    bool visited = curr_pair.second;
    if (visited) {
      cout << curr->data;
    }
    else if (!curr->left && !curr->right) {
      cout << curr->data;
    }
    else if (curr->right) {
      s.emplace(curr->right, false);
      s.emplace(curr, true);
    }
    else if(curr->left) {
      s.emplace(curr, true);
      s.emplace(curr->left, false);
    }
  }
}