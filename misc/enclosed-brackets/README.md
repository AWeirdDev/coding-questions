# enclosed brackets

end signal: EOF

three types of brackets:
- `()` – round brackets
- `[]` – square brackets
- `{}` – curly brackets

check if brackets are correctly enclosed. For example:
* `()[]` -> okay
* `{}(` -> not okay
* `{()}` -> okay
* `{()]}` -> not okay


## solution
i put a bunch of pairings:

```python
PAIRING = {
  "(": 1,
  "[": 2,
  "{": 3,
  ")": -1, 
  "]": -2,
  "}": -3
}
```

since we're always checking between one element and another, we can just do the paired integers LAST and CURRENT,
if we get `0` that means it's okay; if we get a non-zero, it's not okay

note that the stack may be empty and we still get a closing bracket. in that case, it's also not okay
