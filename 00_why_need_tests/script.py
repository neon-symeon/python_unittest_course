def total_price(net, tax_rate, discount=False):
    if not discount:
        return int(net * (1 + tax_rate / 100))
    return int(net * (1 + tax_rate / 100) * .9)
