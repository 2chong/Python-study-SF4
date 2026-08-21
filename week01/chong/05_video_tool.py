'''
https://school.programmers.co.kr/learn/courses/30/lessons/340213

조건만 잘 따져보자!

당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

제한사항
video_len의 길이 = pos의 길이 = op_start의 길이 = op_end의 길이 = 5
video_len, pos, op_start, op_end는 "mm:ss" 형식으로 mm분 ss초를 나타냅니다.
0 ≤ mm ≤ 59
0 ≤ ss ≤ 59
분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타냅니다.
비디오의 현재 위치 혹은 오프닝이 끝나는 시각이 동영상의 범위 밖인 경우는 주어지지 않습니다.
오프닝이 시작하는 시각은 항상 오프닝이 끝나는 시각보다 전입니다.
1 ≤ commands의 길이 ≤ 100
commands의 원소는 "prev" 혹은 "next"입니다.
"prev"는 10초 전으로 이동하는 명령입니다.
"next"는 10초 후로 이동하는 명령입니다.
입출력 예
video_len	pos	op_start	op_end	commands	result
"34:33"	"13:00"	"00:55"	"02:55"	["next", "prev"]	"13:00"
"10:55"	"00:05"	"00:15"	"06:55"	["prev", "next", "next"]	"06:55"
"07:22"	"04:05"	"00:15"	"04:07"	["next"]	"04:17"

'''


def solution(video_len, pos, op_start, op_end, commands):
    def align_time(h, m):
        if m>=0:
            new_h = h + m//60
            new_m = m%60
        else:
            if h == 0:
                return 0, 0
            new_h = h - 1
            new_m = 60 + m
        return new_h, new_m
    
    def str2time(x):
        x_list = [int(i) for i in x if not i == ':']
        h = x_list[0] * 10 + x_list[1]
        m = x_list[2] * 10 + x_list[3]
        return h, m
    
    def time2str(h, m):
        if h//10 == 0:
            h = '0' + str(h)
        if m//10 == 0:
            m = '0' + str(m)
        st = str(h) + ":" + str(m)
        return st
    
    def back10(m):
        m -= 10
        return m
    
    def jump10(m):
        m += 10
        return m
    
    def is_op(op_start, op_end, h, m):
        st_h, st_m = str2time(op_start)
        end_h, end_m = str2time(op_end)
        st = st_h*100 + st_m
        end = end_h*100 + end_m
        cur = h*100 + m
        if st<=cur<=end:
            return end_h, end_m
        else:
            return h, m
    
    def fix_overflow(h, m, video_len):
        vid_h, vid_m = str2time(video_len)
        if vid_h <= h and vid_m <= m:
            return vid_h, vid_m
        elif h == 0 and m <= 0:
            return 0, 0
        else:
            return h, m
    
    def wrapper(h, m, video_len, op_start, op_end):
        h, m = align_time(h, m)
        h, m = fix_overflow(h, m, video_len)
        h, m = is_op(op_start, op_end, h, m)
        return h, m
    
    th, tm = str2time(pos)
    for cmd in commands:
        th, tm = wrapper(th, tm, video_len, op_start, op_end)
        if cmd == "next":
            tm = jump10(tm)
        else:
            tm = back10(tm)
            pass
        th, tm = wrapper(th, tm, video_len, op_start, op_end) 
    cur_pos = time2str(th,tm)
    answer = cur_pos
    return answer
