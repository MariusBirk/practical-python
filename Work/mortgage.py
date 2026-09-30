# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start = 61
extra_payment_end = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12)
    principal = principal - min(payment, principal)
    total_paid = total_paid + min(payment, principal)
    if months >= extra_payment_start and months <= extra_payment_end:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    months = months + 1
    print(months, total_paid, principal)

print(f'Total paid is {total_paid:0.2f} in {months} months')

s = 'hello world'
