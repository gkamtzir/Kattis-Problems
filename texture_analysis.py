line = input()

line_number = 1

while line != 'END':
    pattern = '*'
    changed = 0
    stop = 0
    noWhites = False
    for i in range(1, len(line)):
        if line[i] == '.' and changed == 0:
            if noWhites:
                stop = -1
                break
            stop = i - 1
            changed = 1
        if line[i] == '*' and changed == 0:
            stop = i
            noWhites = True
        if line[i] == '*' and changed == 1:
            break
        pattern += line[i]

    if stop == -1:
        print('%d NOT EVEN' % line_number)
        line_number += 1
        line = input()
        continue
    
    for i in range(len(line)):
        index = i % len(pattern)
        if index == stop:
            canQuit = True
        else:
            canQuit = False
        if pattern[index] != line[i]:
            canQuit = False
            break
    if canQuit:
        print('%d EVEN' % line_number)
    else:
        print('%d NOT EVEN' % line_number)
        
    line_number += 1     
    line = input()
