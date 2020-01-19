import sys

record = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',
    '20': 'Twenty',
    '30': 'Thirty',
    '40': 'Forty',
    '50': 'Fifty',
    '60': 'Sixty',
    '70': 'Seventy',
    '80': 'Eighty',
    '90': 'Ninety'
    }

for line in sys.stdin:
    result = ""
    line = line[:len(line) -1].split(" ")
    for i in range(len(line)):
        try:
            int(line[i])
            if record.get(line[i]) is not None:
                if i == 0:
                    result += record.get(line[i]) + " "
                else:
                    result += record.get(line[i]).lower() + " "
            else:
                ten = line[i][0] + "0"
                one = line[i][1]
                if i == 0:
                    result += f"{record.get(ten)}-{record.get(one).lower()} "
                else:
                    result += f"{record.get(ten).lower()}-{record.get(one).lower()} "
                
        except:
            result += line[i] + " "
    print(result.strip())
