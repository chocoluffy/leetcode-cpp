push: 直接将元素append进数据结构。只允许一个argument。对于`stack<pair<int, char>>`的情况，应该在argument处使用constructor: `stack.push(std::make_pair(3, 'a'))`，以保证只有一个argument。
emplace: 将元素放进数据结构，同时call constructor，允许多个argument，相当于简化了上述必须在argument处所做的处理: `stack.emplace(3, 'a')` 即可。

---

> https://stackoverflow.com/questions/4303513/push-back-vs-emplace-back

In addition to what visitor said :

The function void emplace_back(Type&& _Val) provided by MSCV10 is non conforming and redundant, because as you noted it is strictly equivalent to push_back(Type&& _Val).

But the real C++0x form of emplace_back is really useful: void emplace_back(Args&&...);

Instead of taking a value_type it takes a variadic list of arguments, so that means that you can now perfectly forward the arguments and construct directly an object into a container without a temporary at all.

That's useful because no matter how much cleverness RVO and move semantic bring to the table there is still complicated cases where a push_back is likely to make unnecessary copies (or move). For example, with the traditional insert() function of a std::map, you have to create a temporary, which will then be copied into a std::pair<Key, Value>, which will then be copied into the map :

std::map<int, Complicated> m;
int anInt = 4;
double aDouble = 5.0;
std::string aString = "C++";

// cross your finger so that the optimizer is really good
m.insert(std::make_pair(4, Complicated(anInt, aDouble, aString))); 

// should be easier for the optimizer
m.emplace(4, anInt, aDouble, aString);