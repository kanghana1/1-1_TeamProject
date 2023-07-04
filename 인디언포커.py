# tkinter 캔버스 만들기
import time
from tkinter import *
window=Tk()
window.title("GPTI:게임성향분석")
window.config(padx=10,pady=10)
canvas = Canvas(window,width=1038,height=720)
canvas.grid(column=0,row=1)

# 다음으로 넘어가는 버튼 만들기
def next_img():
    global list_num
    list_num = list_num + 1
    if list_num >= len(img_list)-1:
        next_button.grid_forget()
    canvas.itemconfig(canvas_img,image=img_list[list_num])

next_button = Button(window, text="다음▶",command=next_img)
next_button.grid(column=1,row=1)

# 순서대로 이미지 넣기
start_img = PhotoImage(file="start.png")
rule_img = PhotoImage(file="rule.png")
background_img = PhotoImage(file="background.png")

img_list = [start_img, rule_img, background_img]

list_num = 0
canvas_img = canvas.create_image(519,360,image=img_list[list_num])

window.mainloop()



# 상단에 중요한 내용과 간단한 룰이 보여주기
print("[규칙]"
      "\n 1. 카드는 ♠1~♠10까지 있다. (♠1=♠A로 가장 큰 카드이다.)"
      "\n 2. 기본 코인은 20개로 게임을 시작하기 위한 시작 코인은 1개이다."
      "\n 3. 게임은 마치 경매처럼 코인을 '추가하기'나 '다이'로 진행된다."
      "\n 4. 올인하거나 다이하여 코인이 모두 사라지면 카드가 오픈된다."
      "\n","="*100,"\n",
      "\n NPC1(토끼)의 카드는 ♠3이다."
      "\n NPC2(고양이)의 카드는 ♠9이다."
      "\n 게임은'NPC1(토끼)→ PLAYER → NPC2(고양이)'의 순서대로 진행된다."
      "\n","\n","="*100,"\n")

# 플레이어 이름 설정하기
PLAYER = input(" ▷ PLAYER의 이름 : ")

# GPTI 결과도출에 사용될 변수 만들기(각 질문에 선택에 따라 수가 주어지고 이를 모두 합한 값을 이용해 결과를 도출할 예정)
GPTI_result = 0



# 질문Q1, npc1의 유혹 : 각자의 카드를 알려줄래?
print("\n","시작코인을 거느라 정신없는 순간, 갑자기 NPC1(토끼/♠3)이(가) 조심스럽게 말을 건다."
      "\n ▶ NPC1(토끼/♠3): 'NPC2(고양이/♠9)가 정신없는 사이에 서로 각자가 무슨 카드를 가지고 있는지 알려줄래?'","\n")

answer1 = input(" ▷ NPC1(토끼/♠3)의 제안을 어떻게 할 것인가? (YES or NO) : ")
answer1 = answer1.upper()

if answer1 == "YES":
    print("\n", "="*100,
          "\n","▶", PLAYER, ": 너 먼저 말ㅎ..."
          "\n ▶ NPC2(고양이/♠9): 뭘 둘이서 속닥거리는 거지?",
          "\n",
          "\nNPC2(고양이/♠9)에게 NPC1(토끼/♠3)과(와) 이야기하는 모습을 들켰다. 결국 카드를 알지 못한 체 게임이 시작한다.")
    GPTI_result += 1
else:
    print("\n", "="*100, "\nNPC1(토끼/♠3)부터 게임이 시작한다.")
    GPTI_result += 2



#질문Q2, 코인의 수 : 몇 개의 코인을 걸을 것인가?
print("\n", "="* 100,
      "\nNPC1(토끼/♠3)은(는) 코인 2개를 걸었다."
      "\n","\n", PLAYER,"이(가) 걸어야 할 최소 코인의 수는 3개이다.")

answer2 = int(input(" ▷ 몇 개의 코인을 걸 것인가? (3개 or 9개, 숫자만 기입) : "))

if answer2 == 3:
    print("\n", "="*100,
          "\n","■ (", PLAYER, ") 현재 코인의 수 : 16개"
          "\n뒤이어, NPC2(고양이/♠9)는 코인 9개를 걸었다.")
    GPTI_result += 10

else:
    print("\n", "=" * 100,
          "\n", "■ (", PLAYER, ") 현재 코인의 수 : 10개"
          "\n뒤이어, NPC2(고양이/♠9)는 코인 10개를 걸었다.")
    GPTI_result += 20



# 질문Q3, 갈림길 : 올인이냐 다이냐 그것이 문제로다
print("\n", "=" * 100,"\n")
time.sleep(3)
print(" ▶ NPC1(토끼/♠3): 올인!!( •̀ ω •́ )✧"
      "\nNPC1(토끼/♠3)이(가) 갑자기 올인을 외친다."
      "\n","\n", PLAYER,"는(은) 올인 혹은 다이를 외쳐야 한다.")

answer3 = input(" ▷ 올인(ALL)을 할 것인가, 다이(DIE)를 할 것인가? (ALL or DIE) : ")
answer3 = answer3.upper()# 입력값을 모두 대문자로 바꿔주는 함수

# 대답A3, 갈림길 : 올인이다.
if answer3 == "ALL":
    print("\n", "="*100)
    time.sleep(3)
    print(" ▶ NPC2(고양이/♠9)가 다이를 외쳤다.")
    time.sleep(3)
    GPTI_result += 100


    # 질문Q4, 게임 속 다른 플레이어를 대하는 태도 : 긍정 vs 부정
    from tkinter import *

    window = Tk()
    window.title("GPTI:게임성향분석")
    window.config(padx=10, pady=10)
    canvas = Canvas(window, width=1038, height=720)

    # 승패결과를 알려주고 짋문을 하는 함수
    def next_img_win():
        canvas.itemconfig(canvas_win_img, image=win_Q_img)
        next_button_2.grid_forget()  # grid된 버튼 없애는 함수

        # GPTI의 결과를 출력하는 변수
        img_1122 = PhotoImage(file="1122.png")
        img_1121 = PhotoImage(file="1121.png")
        img_1112 = PhotoImage(file="1112.png")
        img_1111 = PhotoImage(file="1111.png")

        img_2122 = PhotoImage(file="2122.png")
        img_2121 = PhotoImage(file="2121.png")
        img_2112 = PhotoImage(file="2112.png")
        img_2111 = PhotoImage(file="2111.png")

        def happy():
            global GPTI_result
            result = GPTI_result + 1000
            if result == 1122:
                canvas.itemconfig(canvas_win_img, image=img_1122)
            if result == 1121:
                canvas.itemconfig(canvas_win_img, image=img_1121)
            if result == 1112:
                canvas.itemconfig(canvas_win_img, image=img_1112)
            if result == 1111:
                canvas.itemconfig(canvas_win_img, image=img_1111)
            angry_button.grid_forget()
            happy_button.grid_forget()

        def angry():
            global GPTI_result
            result = GPTI_result + 2000
            if result == 2122:
                canvas.itemconfig(canvas_win_img, image=img_2122)
            if result == 2121:
                canvas.itemconfig(canvas_win_img, image=img_2121)
            if result == 2112:
                canvas.itemconfig(canvas_win_img, image=img_2112)
            if result == 2111:
                canvas.itemconfig(canvas_win_img, image=img_2111)
            angry_button.grid_forget()
            happy_button.grid_forget()

        angry_button = Button(window, text="왜 저래, 짜증났다.╰（╬ ‵□′）╯", command=angry)
        angry_button.grid(column=0, row=2)
        happy_button = Button(window, text="오히려 좋아, 재미있었다.\(￣︶￣*\)", command=happy)
        happy_button.grid(column=1, row=2)

    # 다음으로 넘어가는 버튼 만들기
    next_button_2 = Button(window, text="다음▶", command=next_img_win)
    next_button_2.grid(column=2, row=1)

    win_img = PhotoImage(file="win.png")
    win_Q_img = PhotoImage(file="win_Q.png")

    canvas_win_img = canvas.create_image(519, 360, image=win_img)
    canvas.grid(column=0, row=1, columnspan=2)

    window.mainloop()

# 대답A3, 갈림길 : 다이이다.
else:
    print("\n", "=" * 100)
    time.sleep(3)
    print(" ▶ NPC2(고양이/♠9)가 다이를 외쳤다.")
    time.sleep(3)
    GPTI_result += 200


    # 질문Q4, 게임 속 다른 플레이어를 대하는 태도 : 긍정 vs 부정
    from tkinter import *

    window = Tk()
    window.title("GPTI:게임성향분석")
    window.config(padx=10, pady=10)
    canvas = Canvas(window, width=1038, height=720)

    # 승패결과를 알려주고 질문을 하는 함수
    def next_img_lose():
        canvas.itemconfig(canvas_lose_img, image=lose_Q_img)
        next_button_2.grid_forget()  # grid된 버튼 없애는 함수

        # GPTI의 결과를 출력하는 변수
        img_1222 = PhotoImage(file="1222.png")
        img_1221 = PhotoImage(file="1221.png")
        img_1212 = PhotoImage(file="1212.png")
        img_1211 = PhotoImage(file="1211.png")

        img_2222 = PhotoImage(file="2222.png")
        img_2221 = PhotoImage(file="2221.png")
        img_2212 = PhotoImage(file="2212.png")
        img_2211 = PhotoImage(file="2211.png")

        def happy():
            global GPTI_result
            result = GPTI_result + 1000
            if result == 1222:
                canvas.itemconfig(canvas_lose_img, image=img_1222)
            if result == 1221:
                canvas.itemconfig(canvas_lose_img, image=img_1221)
            if result == 1212:
                canvas.itemconfig(canvas_lose_img, image=img_1212)
            if result == 1211:
                canvas.itemconfig(canvas_lose_img, image=img_1211)
            angry_button.grid_forget()
            happy_button.grid_forget()

        def angry():
            global GPTI_result
            result = GPTI_result + 2000
            if result == 2222:
                canvas.itemconfig(canvas_lose_img, image=img_2222)
            if result == 2221:
                canvas.itemconfig(canvas_lose_img, image=img_2221)
            if result == 2212:
                canvas.itemconfig(canvas_lose_img, image=img_2212)
            if result == 2211:
                canvas.itemconfig(canvas_lose_img, image=img_2211)
            angry_button.grid_forget()
            happy_button.grid_forget()

        angry_button = Button(window, text="왜 저래, 짜증났다.╰（╬ ‵□′）╯", command=angry)
        angry_button.grid(column=0, row=2)
        happy_button = Button(window, text="오히려 좋아, 재미있었다.\(￣︶￣*\)", command=happy)
        happy_button.grid(column=1, row=2)

    canvas.grid(column=0, row=1, columnspan=2)

    # 다음으로 넘어가는 버튼 만들기
    next_button_2 = Button(window, text="다음▶", command=next_img_lose)
    next_button_2.grid(column=2, row=1)

    lose_img = PhotoImage(file="lose.png")
    lose_Q_img = PhotoImage(file="lose_Q.png")

    canvas_lose_img = canvas.create_image(519, 360, image=lose_img)

    window.mainloop()

## 실제 인디언포커 하기: 선택 불가능, 필수 참여
print("\n", "=" * 100, "\n")
input(" ▷ 고도의 심리 카드게임, 인디언 포커 더 하러가기 (YES or YES) : ")

import time
import random

# 카드 생성 및 무작위 배치
deck = [k for k in range(1, 10)]
random.shuffle(deck)
card_player = deck[0]
card_npc = deck[1]

from tkinter import *

window = Tk()
window.title("고도의 심리 카드게임, 인디언포커")
window.config(padx=10, pady=10)
canvas = Canvas(window, width=1038, height=720)
canvas.grid(column=0, row=1)


# 다음으로 넘어가는 버튼 만들기
def next_img():
    global list_num
    list_num = list_num + 1
    if list_num >= len(img_list) - 1:
        next_button.grid_forget()
    canvas.itemconfig(canvas_img, image=img_list[list_num])


next_button = Button(window, text="다음▶", command=next_img)
next_button.grid(column=1, row=1)

# 순서대로 이미지 넣기
start_img = PhotoImage(file="indian_start.png")
rule_img = PhotoImage(file="indian_rule.png")
bg_1 = PhotoImage(file="indian_bg1.png")
bg_2 = PhotoImage(file="indian_bg2.png")
bg_3 = PhotoImage(file="indian_bg3.png")
bg_4 = PhotoImage(file="indian_bg4.png")
bg_5 = PhotoImage(file="indian_bg5.png")
bg_6 = PhotoImage(file="indian_bg6.png")
bg_7 = PhotoImage(file="indian_bg7.png")
bg_8 = PhotoImage(file="indian_bg8.png")
bg_9 = PhotoImage(file="indian_bg9.png")
bg_10 = PhotoImage(file="indian_bg10.png")

bg_list = [bg_1, bg_2, bg_3, bg_4, bg_5, bg_6, bg_7, bg_8, bg_9, bg_10]
background_img = bg_list[card_npc - 1]

img_list = [start_img, rule_img, background_img]

list_num = 0
canvas_img = canvas.create_image(519, 360, image=img_list[list_num])

window.mainloop()

print("\n", "=" * 100, "\n",
      "\n 잘못된 답변의 경우 시스템 에러로 인해 강제종료될 수 있습니다."
      "\n NPC(강아지)의 카드는 ♠", card_npc, "입니다."
                                      "\n 게임은", PLAYER, "→ NPC(강아지)의 순서로 진행됩니다."
                                                        "\n", "\n", "=" * 100, "\n")
time.sleep(1)

## 첫턴 시작코인 걸기 (시작코인은 1개씩)
print('게임을 시작하기 위해서는 시작코인 1개를 걸어야합니다. 시작 코인을 걸지 않으면 게임이 종료됩니다.')
answer_1st = input('시작 코인을 걸겠습니까? (YES or NO) : ')
answer_1st = answer_1st.upper()

if answer_1st == 'NO':
    print('\n게임이 종료되었습니다.')
    exit()

if answer_1st == 'YES':
    print('\n', PLAYER, '이(가) 코인 1개를 걸었습니다.(남은 코인 개수 : 19개)')
    print('\n', 'NPC( 강아지/♠', card_npc, ')가 코인 1개를 걸었습니다.'
          "\n", PLAYER, "는(은) 1개보다 많은 코인을 걸어야 합니다.")

if answer_1st != 'NO' and answer_1st != 'YES':
    print('잘못된 답변에 의한 에러, 게임이 종료됩니다.')
    exit()

print('\n', '=' * 100)
time.sleep(1.5)


###졌을때 이미지 출력하는 함수
def lose_result():
    window = Tk()
    window.title("고도의 심리 카드게임, 인디언포커")
    window.config(padx=10, pady=10)
    canvas = Canvas(window, width=1038, height=720)
    canvas.grid(column=0, row=1)

    indian_lose_img = PhotoImage(file="indian_lose.png")

    canvas.create_image(519, 360, image=indian_lose_img)
    window.mainloop()
    exit()


###이겼을때 이미지 출력하는 함수
def win_result():
    window = Tk()
    window.title("고도의 심리 카드게임, 인디언포커")
    window.config(padx=10, pady=10)
    canvas = Canvas(window, width=1038, height=720)
    canvas.grid(column=0, row=1)

    indian_win_img = PhotoImage(file="indian_win.png")

    canvas.create_image(519, 360, image=indian_win_img)
    window.mainloop()
    exit()


### 각자의 카드를 비교하는 함수
def comparison():
    if card_player > card_npc:
        print("\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
              "\n", PLAYER, "가(이) 이겼습니다.")
        time.sleep(1.5)
        win_result()

    else:
        print("\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
              "\n", PLAYER, "가(이) 졌습니다.")
        time.sleep(1.5)
        lose_result()


## NPC의 전반경기
def first_haif():
    import random
    global answer_2nd
    global turn
    coin_npc = 19
    rnd_2nd = [a for a in range(answer_2nd + 1, answer_2nd + 6)]  # 현실성을 반영하기 위하여...
    random.shuffle(rnd_2nd)
    npc_2nd = rnd_2nd[0]

    coin_npc = coin_npc - npc_2nd
    print("\nNPC( 강아지/♠", card_npc, ")가 코인을", npc_2nd, "개 걸었습니다."
          "\n", PLAYER, "는(은)", npc_2nd, "개보다 많은 코인을 걸어야 합니다.")
    print('\n', '=' * 100)
    time.sleep(1.5)


## NPC의 후반경기
def second_haif():
    choice_list = [0, 1]  ##0은 올인, 1은 다이
    random.shuffle(choice_list)
    if choice_list[0] == 0:
        print("NPC( 강아지/♠", card_npc, ")가 코인을 올인하였습니다."
                                      "\n", PLAYER, "는(은) 올인 혹은 다이를 외쳐야 합니다.")
        last_answer = input(" ▷ 올인(ALL)을 할 것입니까, 다이(DIE)를 할 것입니까? (ALL or DIE) : ")
        last_answer = last_answer.upper()

        if last_answer == 'ALL':
            comparison()
        else:
            print("\n", PLAYER, "는(은) 다이를 선택하였습니다."
                  "\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
                  "\n", PLAYER, "가(이) 졌습니다.")
            time.sleep(1.5)
            lose_result()
    else:
        print("\nNPC( 강아지/♠", card_npc, ")가 다이를 선택하였습니다."
              "\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
              "\n", PLAYER, "가(이) 이겼습니다.")
        time.sleep(1.5)
        win_result()


coin_player = 19
turn = 1

for i in range(10):
    print('\n', '남은 코인은', coin_player, '개 입니다. 계속 베팅 하시겠습니까?')
    answer_1nd = input("계속 베팅하고 싶다면 YES, 다이하고 싶다면 NO를 입력하세요.(YES or NO) : ")
    answer_1nd = answer_1nd.upper()

    if answer_1nd == 'YES':
        turn += 1
        answer_2nd = int(input('몇 개의 코인을 베팅할 것인가요?(숫자만 기입/올인을 하고 싶다면 남은 코인을 모두 기입): '))
        print('\n', '코인을 ', answer_2nd, '개 걸었습니다.(남은 코인 개수 :', coin_player - answer_2nd, ')')
        coin_player = coin_player - answer_2nd

        if coin_player == 0:
            time.sleep(2)
            choice_list = [0, 1]  ##0은 올인, 1은 다이
            random.shuffle(choice_list)
            if choice_list[0] == 0:
                print("NPC( 강아지/♠", card_npc, ")가 올인하였습니다.")
                comparison()
            else:
                print("\nNPC( 강아지/♠", card_npc, ")가 다이를 선택하였습니다."
                      "\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
                      "\n", PLAYER, "가(이) 이겼습니다.")
                time.sleep(1.5)
                win_result()

        if turn <= 3:
            first_haif()
        else:
            second_haif()
    else:
        print("\n", PLAYER, "는(은) 다이를 선택하였습니다."
              "\n", PLAYER, "의 카드는 ♠",card_player,"였습니다."
              "\n", PLAYER, "가(이) 졌습니다.")
        time.sleep(1.5)
        lose_result()