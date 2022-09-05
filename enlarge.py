def enlarge(l:list ) ->list:
    result = []
    for line in l:
        result_line =''
        for i in line:
            result_line += i*2
        result.append(result_line)
        result.append(result_line)
    return result


def show(image):
    for line in image:
        print(line)

dot = ['@']
show(enlarge(dot))
# => @@
# => @@
frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]
show(frame)
# => ****
# => *  *
# => *  *
# => ****
show(enlarge(frame))
# => ********
# => ********
# => **    **
# => **    **
# => **    **
# => **    **
# => ********
# => ********
