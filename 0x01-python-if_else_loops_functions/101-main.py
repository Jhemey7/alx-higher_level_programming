#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
root@870477e8afd7:/alx-higher_level_programming/0x01-python-if_else_loops_functions# cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
