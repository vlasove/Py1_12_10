cpp = set()
rust = set() 

n_cpp = int(input())
m_rust = int(input())

for _ in range(n_cpp):
    cpp.add(input())

for _ in range(m_rust):
    rust.add(input())

total = cpp.symmetric_difference(rust)
print(len(total))