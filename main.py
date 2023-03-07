USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit():
    initial_sum = int(input("Initial sum: "))
    percent = int(input("Percent: "))
    fixed_period = int(input("Fixed period: "))
    set_period = int(input("Set period: "))
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)

    result = initial_sum * growth
    return result


def read_txt():
    r = open("recomendation.txt", 'r')
    r1 = r.read()
    print(r1)
    r.close()

def save_txt():
    data = str(deposit())
    s = open("depo_result.txt",'w')
    s.write(data)
    s.close()




if __name__ == '__main__':

    read_txt()

    save_txt()
