import random
def main():
    NUM_OF_TRIALS = 5
    NUM_OF_ALL_MISS = 2
    zyoutai=0
    for i in range(NUM_OF_TRIALS):
        seikai = shutudai()
        kaitou(seikai)
        if zyoutai==1:
            break


def shutudai():
    al=[chr(c+65) for c in range(26)]
    tenlist = random.sample(al,10)
    print("対象文字:")
    print(tenlist)

    kekkann= random.sample(tenlist,8)
    print(f"表示文字\n{kekkann}")



def kaitou(seikai):
    ans = int(input("欠陥文字はいくつあるでしょうか"))
    if ans!=2:
        print("不正解")
        zyoutai=1
    if ans ==2:
        print("正解です")
        print("次に具体的に欠陥文字を入れてください")
        for i in range(int(NUM_OF_TRIALS)):
            c= input(f"{i+1}の目の文字を入れてください:")
            if c not in tenlist:
                print("正解です")

            else:
                print("不正解です")
                zyoutai==1
                



if __name__ == "__main__":
    main()
    print("終了")
