with open('build/index.main.mjs', 'r') as file:
    for line in file:
        if 'appApproval' in line:
            print(line)