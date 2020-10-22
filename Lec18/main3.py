# Как спровоцировать исключительную ситуацию?
balance = 51
down = 3
if balance < 50:
    balance -= down 
else:
    # Сложная логика расчета баланса которая еще не готова
    raise Exception("This code block not ready yet")
