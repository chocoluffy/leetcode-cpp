// given a list <l0, l1, l2, ...>, modify it into <l0, l2, l4,..., l1, l3...> a even-odd merged list.
node* even_odd_merge(node* L) {
  node* prev_even = NULL;
  node* even = L, odd = L.next;
  node* odd_start = L.next;
  while(even && odd) {
    prev_even = even;
    even.next = odd.next;
    even = even.next;
    if(even) {
      odd.next = even.next;
      odd = odd.next;
    }
  }      
  if(even) { // case: odd number of elements in list.
    prev_even = even;
  }
  if(prev_even) { // case: empty list.
    prev_even.next = odd_start;
  }
  return L;
}   