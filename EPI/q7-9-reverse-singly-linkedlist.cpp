node* reverse(node* L) {
  node* prev = NULL, curr = L;
  node* tmp = NULL;
  while(curr) {
    tmp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = tmp;
  }
  return prev;
}