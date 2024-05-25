import pickle
import os

def input_scores():
    l=[]
    i=1
    while True:
        n=int(input(f'#{i} '))
        if n<0:
            break
        l.append(n)
        i+=1
        
    return l

def get_average(l):
    total=0
    for n in l:
        total += n
    avr=float(total/len(l))
    return avr

def show_scores(l):
    for n in l:
        print(n,end=' ')
    print()

def save_data(filename, scores, average):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(average, file)
    
def load_data(filename):
    with open(filename, 'rb') as file:
        scores=pickle.load(file)
        average=pickle.load(file)
    return scores, average

filename='score.bin'
scores=[]

if os.path.exists(filename):
    scores, average=load_data(filename)
    print('[파일 읽기]\n')
    print()
    print('[점수 출력]\n')
    print(f'개인점수: {scores}\n')
    print(f'평균: {average}\n')
    
else:
    print('[점수 입력]')
    scores=input_scores()
    print('[점수 출력]\n개인점수:', end='')
    show_scores(scores)
    avr=get_average(scores)
    print(f'평균:{avr:1}')
    print()
    
    save_data(filename, scores, avr)

