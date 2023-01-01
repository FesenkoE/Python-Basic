from main import formatted_phone, phone_valid

assert formatted_phone("0993334455") == "380993334455"
assert formatted_phone("+380993667788") == "380993667788"
assert formatted_phone("@%!991112^2f33") == "380991112233"

assert phone_valid("380993334455") is True
assert phone_valid("qqqqqqqqqqqq") is False
assert phone_valid("@%!991112^2f33") is False
assert phone_valid("0993334455") is False
