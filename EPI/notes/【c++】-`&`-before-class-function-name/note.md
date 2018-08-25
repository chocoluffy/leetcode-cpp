基本上就是说不希望caller改变return的值，因此返回一个reference。

例如： `const unordered_set<string> & dict` 

---

> https://stackoverflow.com/questions/8610350/implications-of-using-an-ampersand-before-a-function-name-in-c

It returns a reference to the private member.

There are many cases where this is desirable, but some care should be taken.

IMO it's generally not a good idea to return a copy of an internal object that is not an integral type, for overall performance reasons. Yes I know, premature optimization is not good, but this is not really optimization, it's just a good performance practice that allows the caller to determine the performance implications; if it wants a copy, it can just not declare the variable that it's assigning it to as a reference.

There are 2 general rules of thumb I use here:

1) If you don't want the caller to be able to modify the private object directly, declare the return value as a const reference:

inline const string& GetLabel() const{ return m_Label; }
2) A caller should never store the reference returned from a class method, it should only be used locally where the parent object is guaranteed to be in scope.

If for some reason you need callers to be able to store a reference to your internal objects, use smart pointers instead.