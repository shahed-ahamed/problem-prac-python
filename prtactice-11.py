# cover USD to BDT

a = float(input("Enter USD: "))

def converter (usd_val):
    bdt_val = usd_val * 125
    print("BDT:", bdt_val, "Taka")

converter(a)