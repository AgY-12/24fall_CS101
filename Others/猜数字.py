import random

def guess_number_game():
    # 生成一个1到100之间的随机数
    number_to_guess = random.randint(1, 100)
    guess_count = 0
    print("欢迎参加猜数字游戏！")
    print("我已经选好了一个1到100之间的整数。")
    print("请试着猜猜看它是多少吧！")

    while True:
        try:
            # 获取玩家输入
            player_guess = int(input("请输入你的猜测（1-100）："))
            
            # 检查输入范围
            if player_guess < 1 or player_guess > 100:
                print("请确保你的猜测在1到100之间！")
                continue
            
            # 增加猜测次数
            guess_count += 1
            
            # 判断猜测结果
            if player_guess == number_to_guess:
                print(f"恭喜你！你猜对了！答案正是{number_to_guess}！")
                print(f"你总共猜测了{guess_count}次。")
                break
            elif player_guess < number_to_guess:
                print("太低了！试试更大的数字。")
            else:
                print("太高了！试试更小的数字。")
                
        except ValueError:
            print("请输入有效的整数！")

if __name__ == "__main__":
    guess_number_game()
