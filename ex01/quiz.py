import random
def main():
    seikai = shukudai()
    kaitou(seikai)

def shukudai():
    qas = [
        {"q":"サザエの旦那の名前は","a":["マスオ","ますお"]},
        {"q":"カツオの妹の名前は","a":["わかめ","ワカメ"]}
        ]
    print("問題")
    r=random.randint(0,1)
    print(qas[r]["q"])
    return  qas[r]["a"]

def kaitou(seikai):
    ans =input("答えるんだ")
    if ans in seikai:
        print("正解")
    else:
        print("失敗")

if __name__ == "__main__":
    main()
