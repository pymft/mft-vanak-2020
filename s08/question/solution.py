# step 1:
fr = open('input.txt', mode='r')
text = fr.read()
n, pat = text.strip().split('\n')
n = int(n)
fr.close()

# step 2:

out_line = pat * n + '\n'
out_text = out_line * n

# step 3:
fw = open('output.txt', mode='w')
fw.write(out_text)
fw.close()