# हमने range(10, 0, -1) का उपयोग किया है ताकि 10 से 1 तक गिनती को reverse में प्रिंट कर सकें।
# range(start, stop, step) का काम समझते हैं:
# range(10, 0, -1) में:
# start = 10 → यह गिनती 10 से शुरू होगी।
# stop = 0 → यह 0 से पहले (यानी 1 तक) चलेगी। range() stop value को include नहीं करता।
# step = -1 → इसका मतलब हर बार 1 घटाना है (reverse count के लिए)।

for i in range(10,0 ,-1):
    print(i)

for i in range(1,10,+2):
    print(f"{i} \n")