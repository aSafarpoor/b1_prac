x=[1,2,3]
y=[11,22,33]
# x=np.array(a[:])
# y=np.array(b[:])
randomize = np.arange(len(x))
np.random.shuffle(randomize)
x = x[randomize]
y = y[randomize]