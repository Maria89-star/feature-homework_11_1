from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str:
    """Функция маскирующая счет и номер карты"""

    if "Счет" in nums:
        return "Счет" + get_mask_account(nums)
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))

date_ = input()


def get_date(date: str) -> str:
    """Функция вывода даты в общепринятом формате"""
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


print(get_date("2024-11-07T02:26:18.671407"))
