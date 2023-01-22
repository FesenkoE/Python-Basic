"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.

    Напишите функцию, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И возвращает наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)

    [out]
    2

    [37, 38, 39, 40] , [37, 37, 40, 40] -> 3
    [37, 38, 39, 40] , [42] -> 0
    [37, 38, 39] , [37, 37, 37, 37] -> 3

    Напишите несколько тестов
"""


def main():
    def skates(skate_sizes, foot_sizes):
        sorted_skate_sizes = sorted(skate_sizes)

        max_person = 0

        for foot_size in foot_sizes:
            for idx in range(len(sorted_skate_sizes)):
                if int(foot_size) <= int(sorted_skate_sizes[idx]):
                    max_person += 1
                    sorted_skate_sizes.remove(sorted_skate_sizes[idx])
                    break

        return max_person

    assert skates([39, 38, 41, 37], [40, 39, 41]) == 2
    assert skates([37, 38, 39, 40], [37, 37, 40, 40]) == 3
    assert skates([37, 38, 39, 40], [42]) == 0
    assert skates([37, 38, 39], [37, 37, 37, 37]) == 3


if __name__ == '__main__':
    main()
