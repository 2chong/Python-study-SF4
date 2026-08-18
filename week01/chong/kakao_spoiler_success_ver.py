'''
https://school.programmers.co.kr/learn/courses/30/lessons/468370

문제에서는 '중요한 단어'의 수를 찾으라고 했음. 이때의 조건은
1. 스포일러 단어 찾기
2. 해당 단어가 스포일러가 아닌 단어여야함
3. 스포일러 중에 하나만 선택

1번은 각 단어의 start, end 인덱스와, covered라는 boolean으로 이루어진 list를 통해 any 함수를 써서 확인 가능
2번은 1번을 제외한 나머지 단어를 통해 차집합으로 제거
3번은 set를 쓰는 순간 스포일러 중복은 고려 안해도 됨

문제 설명
카카오톡은 메시지의 일부를 가려두었다가, 클릭했을 때만 공개되는 스포 방지 기능을 제공합니다. 이 기능을 활용하면 중요한 정보를 가리고 보낼 수 있습니다.

무지는 이 기능을 이용해 하나의 메시지 곳곳에 스포 방지 기능을 적용해 당신에게 보냈습니다. 당신은 메시지 시작부터 왼쪽 → 오른쪽 순서로 스포 방지 구간을 하나씩 클릭해 공개되는 단어들 중, 중요한 단어가 몇 개인지 확인하려 합니다.

단어 및 중요한 단어 규칙

단어는 공백으로 구분되며, 알파벳 소문자와 숫자로만 구성된 연속된 문자열입니다.
단어를 구성하는 문자들의 인덱스 중 하나 이상이 스포 방지 구간에 포함될 경우, 해당 단어는 스포일러 방지 단어로 간주합니다. 즉, 단어 내 일부 문자에만 스포일러 방지 기능이 적용되더라도, 해당 단어 전체를 스포일러 방지 단어로 간주합니다.
한 단어가 여러 개의 스포 방지 구간에 걸쳐 있을 수 있으며, 하나의 스포 방지 구간에 여러 단어가 포함될 수 있습니다.
스포 방지 구간을 클릭해 단어의 모든 문자가 공개되었을 때, 그 단어가 아래 조건을 모두 만족하면 중요한 단어입니다.
스포 방지 단어여야 합니다.
메시지의 스포 방지 구간이 아닌 구간(= 어떤 스포 방지 구간에도 속하지 않는 모든 구간: 각 구간의 앞·사이·뒤 포함)에 등장한 적이 없어야 합니다.
이전에 공개된 스포 방지 단어와 중복되지 않아야 합니다.
여러 단어가 동시에 공개된 경우, 왼쪽부터 순서대로 하나씩 중요한 단어인지 판단합니다.
무지가 당신에게 보내온 메시지를 나타내는 문자열 message와 스포 방지가 적용된 구간을 나타내는 2차원 정수 배열 spoiler_ranges가 매개변수로 주어질 때, 스포 방지 단어 중 중요한 단어의 수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ message의 길이 ≤ 20,000
message는 알파벳 소문자, 숫자 그리고 공백으로 이루어져 있습니다.
message는 하나 이상의 단어로 구성된 문자열입니다.
공백은 연속해서 등장하지 않습니다.
1 ≤ spoiler_ranges의 길이 ≤ 1,000
spoiler_ranges[i]는 [start, end] 형태로 스포 방지를 적용한 구간을 나타냅니다. 이때 start와 end는 문자 인덱스이며, 두 인덱스 모두 구간에 포함됩니다.
0 ≤ start ≤ end < message의 길이
모든 구간은 서로 겹치지 않으며, start 기준으로 오름차순 정렬되어 주어집니다.
'''

def solution(message, spoiler_ranges):
    n = len(message)
    covered = [False] * n
    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            covered[i] = True

    words = []  # (word, start, end)
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        start = i
        while i < n and message[i] != ' ':
            i += 1
        end = i - 1
        words.append((message[start:i], start, end))

    no_spo = set()
    important = set()
    for word, start, end in words:
        if any(covered[start:end+1]):
            important.add(word)
        else:
            no_spo.add(word)

    return len(important - no_spo)
