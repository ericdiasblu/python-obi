n = int(input())
logs = [input().split() for _ in range(n)]

current_time = 0
pending = {}  # amigo: tempo_em_que_foi_recebida
response_total = {}  # amigo: tempo_total_de_resposta

i = 0
while i < n:
    log = logs[i]

    if log[0] == 'R':
        friend = int(log[1])
        pending[friend] = current_time
        if friend not in response_total:
            response_total[friend] = 0
        current_time += 1

    elif log[0] == 'E':
        friend = int(log[1])
        if friend in pending:
            response_total[friend] += current_time - pending[friend]
            del pending[friend]
        if friend not in response_total:
            response_total[friend] = 0
        current_time += 1

    elif log[0] == 'T':
        seconds = int(log[1])
        current_time += seconds

    i += 1

# Finalizando saída
all_friends = list(response_total.keys())
all_friends.sort()
for friend in all_friends:
    if friend in pending:
        print(f"{friend} -1")
    else:
        print(f"{friend} {response_total[friend]}")