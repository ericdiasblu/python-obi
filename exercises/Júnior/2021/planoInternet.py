megabytes = int(input())
megabytesMensal = megabytes
meses = int(input())

for i in range(meses):
    x = int(input())
    megabytes -= x
    megabytes += megabytesMensal

print(megabytes)