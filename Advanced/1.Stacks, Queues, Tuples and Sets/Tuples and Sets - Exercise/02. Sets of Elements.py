n_lines, m_lines = list(map(int, input().split()))

n_set = {int(input()) for number in range(n_lines)}
m_set = {int(input()) for num in range(m_lines)}

print('\n'.join([str(number) for number in n_set & m_set]))



# n_lines, m_lines = list(map(int, input().split()))
# print('\n'.join([str(number) for number in {int(input()) for number in range(n_lines)} & {int(input()) for num in range(m_lines)}]))